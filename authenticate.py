import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pickle
import os

def authenticate_user(username):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Authenticating {username}... Please speak.")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)  # Capture the audio input
        print("Audio captured for authentication!")

        try:
            # Transcribe speech to text
            spoken_words = recognizer.recognize_google(audio_data)
            print(f"Words spoken: {spoken_words}")

            # Load the registered words and pin
            user_file = f"data/users/{username}_data.pkl"
            if os.path.exists(user_file):
                with open(user_file, "rb") as f:
                    user_data = pickle.load(f)

                registered_words = user_data["words"]
                registered_pin = user_data["pin"]

                # Compare spoken words with registered words
                if spoken_words.lower() == registered_words.lower():
                    print("Words match. Authentication successful!")
                    messagebox.showinfo("Success", "Voice match. Authentication successful!")
                else:
                    print("Words do not match. Asking for PIN...")
                    messagebox.showwarning("Warning", "Voice does not match. Please enter your PIN.")
                    ask_for_pin(username, registered_pin)  # Ask for PIN if words do not match
            else:
                print("No registered data found for this username.")
                messagebox.showerror("Error", "No registered data found for this username.")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio. Please try again.")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results from the speech recognition service. Check your network connection.")

def ask_for_pin(username, registered_pin):
    # Create a new Toplevel window for the PIN entry
    pin_window = tk.Toplevel()
    pin_window.title("Enter PIN")
    pin_window.geometry("400x200")
    pin_window.config(bg="#2C3E50")

    # Style settings
    label_font = ("Arial", 12)
    button_font = ("Arial", 12, "bold")

    # Title
    title_label = tk.Label(pin_window, text=f"Enter your 4-digit PIN for {username}:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
    title_label.pack(pady=20)

    # PIN entry
    entry_pin = tk.Entry(pin_window, font=label_font, width=30, show='*')
    entry_pin.pack(pady=5)

    def check_pin():
        pin = entry_pin.get()
        # Check if a PIN was provided and validate it
        if pin == registered_pin:
            print("Pin match. Authentication successful!")
            messagebox.showinfo("Success", "Pin match. Authentication successful!")
            pin_window.destroy()  # Close the PIN window
        else:
            print("Authentication failed. Incorrect PIN.")
            messagebox.showerror("Error", "Authentication failed. Incorrect PIN.")

    # Authenticate button
    auth_button = tk.Button(pin_window, text="Authenticate", font=button_font, bg="#3498DB", fg="#FFFFFF",
                            activebackground="#2980B9", activeforeground="#FFFFFF", command=check_pin)
    auth_button.pack(pady=20)

    # Center the window on the screen
    pin_window.eval('tk::PlaceWindow . center')

def on_authenticate():
    username = entry_name.get()

    # Check if username is provided
    if username:
        authenticate_user(username)  # Authenticate with username only
    else:
        messagebox.showerror("Error", "Please provide a valid name.")

# Tkinter GUI for authentication
root = tk.Tk()
root.title("Voice Authentication")
root.geometry("400x300")
root.config(bg="#2C3E50")

# Style settings
title_font = ("Helvetica", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Title
title_label = tk.Label(root, text="Voice Authentication", font=title_font, bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=20)

# Name label and entry
label_name = tk.Label(root, text="Enter your name:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
label_name.pack(pady=10)

entry_name = tk.Entry(root, font=label_font, width=30)
entry_name.pack(pady=5)

# Authenticate button
auth_button = tk.Button(root, text="Authenticate", font=button_font, bg="#3498DB", fg="#FFFFFF", 
                        activebackground="#2980B9", activeforeground="#FFFFFF", command=on_authenticate)
auth_button.pack(pady=20)

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

root.mainloop()
