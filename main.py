import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pickle
import os

def register_user(username, pin):
    recognizer = sr.Recognizer()

    # Check if the microphone is available
    try:
        with sr.Microphone() as source:
            print(f"Registering {username}... Please speak.")
            audio_data = recognizer.listen(source)  # Capture the audio input
            print("Audio captured for registration!")

            try:
                # Transcribe speech to text
                spoken_words = recognizer.recognize_google(audio_data)
                print(f"Words registered: {spoken_words}")

                # Save the transcribed words and the pin
                user_data = {"words": spoken_words, "pin": pin}
                user_file = f"data/users/{username}_data.pkl"
                os.makedirs(os.path.dirname(user_file), exist_ok=True)
                with open(user_file, "wb") as f:
                    pickle.dump(user_data, f)

                messagebox.showinfo("Success", f"Registration complete. Name: {username}, Pin: {pin}")
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Could not understand the audio. Please try again.")
            except sr.RequestError:
                messagebox.showerror("Error", "API request failed. Please check your internet connection.")
    except OSError as e:
        print(f"Microphone access error: {e}")
        messagebox.showerror("Error", "Microphone not found. Please connect a microphone and try again.")

def on_register():
    username = entry_name.get().strip()  # Strip whitespace
    pin = entry_pin.get()

    if username and pin.isdigit() and len(pin) == 4:
        register_user(username, pin)
    else:
        messagebox.showerror("Error", "Please provide a valid name and a 4-digit pin.")

# Tkinter GUI for registration
root = tk.Tk()
root.title("Register User")
root.geometry("400x300")
root.config(bg="#2C3E50")

# Style settings
title_font = ("Helvetica", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Title
title_label = tk.Label(root, text="Voice Registration", font=title_font, bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=20)

# Name label and entry
label_name = tk.Label(root, text="Enter your name:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
label_name.pack(pady=10)

entry_name = tk.Entry(root, font=label_font, width=30)
entry_name.pack(pady=5)

# Pin label and entry
label_pin = tk.Label(root, text="Enter a 4-digit pin:", font=label_font, bg="#2C3E50", fg="#ECF0F1")
label_pin.pack(pady=10)

entry_pin = tk.Entry(root, font=label_font, width=30, show="*")
entry_pin.pack(pady=5)

# Register button
register_button = tk.Button(root, text="Register", font=button_font, bg="#3498DB", fg="#FFFFFF",
                            activebackground="#2980B9", activeforeground="#FFFFFF", command=on_register)
register_button.pack(pady=20)

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

root.mainloop()