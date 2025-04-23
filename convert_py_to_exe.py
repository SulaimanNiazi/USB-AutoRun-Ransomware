import subprocess
import os

def convert_to_exe(py_file):
    if not os.path.isfile(py_file):
        print("Error: The specified Python file does not exist.")
        return

    command = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        py_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"\nSuccessfully converted {py_file} to .exe.")
        print("Check the 'dist' folder in the current directory.")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)

if __name__ == "__main__":
    py_file = input("Enter the path to your Python (.py) file: ").strip()
    convert_to_exe(py_file)
