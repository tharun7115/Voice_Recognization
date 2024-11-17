#Voice Recognition
This project is a secure voice authentication system developed using Python. The application aims to recognize the voice of a registered owner for authentication purposes. The primary features include:

Voice Recognition:

The system is designed to identify and authenticate users based on their unique voice patterns.
During the registration process, the user records their voice, which is stored securely in the database.
PIN Backup:

In cases where the system fails to recognize the owner's voice, a secondary layer of security is implemented.
The user is prompted to enter a predefined four-digit PIN as a backup authentication method.
Secure Registration:

Each user must register both their voice and a unique PIN.
During the authentication process, if the voice does not match the stored sample, the system requests the PIN for verification.
Error Handling:

If both voice recognition and PIN authentication fail, access is denied to ensure security

#process of the Voice Recognization
Main File (Registration)
User Registration:
The user starts by entering their name and a unique four-digit PIN.
Voice Data Collection:
The user is prompted to speak specific words to record their voice sample.
The voice data is processed and securely stored for future verification.
Authentication File
User Input:
The system asks the user to input their registered name.
The user is prompted to speak to authenticate using the stored voice sample.
Voice Recognition:
If the voice matches the stored sample, access is granted.
PIN Verification (Fallback):
If the voice does not match the stored sample, the system prompts the user to enter the previously registered four-digit PIN.
If the correct PIN is provided, access is granted. Otherwise, access is denied.
