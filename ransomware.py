import os
import tkinter as tk
from tkinter import messagebox

# Define the directories for README.txt placement
directories = [
    os.path.expanduser('~/Desktop'),
    os.path.expanduser('~/Documents'),
    os.path.expanduser('~/Downloads'),
]

readme_content = """\
========== MOCK RANSOMWARE ==========
Your files have been encrypted (SIMULATED).

To recover your data, please enter the provided DEMO KEY.
This is ONLY a harmless demonstration.

=====================================
"""

DEMO_KEY = "1234ABCD"

def place_readme_files():
    for folder in directories:
        try:
            filepath = os.path.join(folder, "README.txt")
            with open(filepath, 'w') as file:
                file.write(readme_content)
        except Exception as e:
            print(f"Failed writing README in {folder}: {e}")

def ransomware_prompt():
    window = tk.Tk()
    window.title("Files Locked (Demo)")
    window.attributes("-fullscreen", True)
    window.configure(bg="black")

    message = tk.Label(window, text="Your computer is LOCKED!\nEnter the DEMO KEY to unlock.",
                       font=("Arial", 30), fg="red", bg="black")
    message.pack(expand=True)

    entry = tk.Entry(window, font=("Arial", 24), justify='center')
    entry.pack(pady=20)

    def validate_key():
        if entry.get() == DEMO_KEY:
            messagebox.showinfo("Unlocked", "Correct key! Demo ended.")
            window.destroy()
        else:
            messagebox.showerror("Incorrect Key", "Wrong DEMO KEY! Try again.")

    submit_btn = tk.Button(window, text="Submit Key", command=validate_key,
                           font=("Arial", 20), bg="red", fg="white")
    submit_btn.pack(pady=10)

    window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable window close
    window.mainloop()

if __name__ == "__main__":
    place_readme_files()
    ransomware_prompt()
