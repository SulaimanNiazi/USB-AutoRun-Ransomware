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

def find_py_file():
    # Enter path automatically
    py_file = "ransomware.py"
    
    current_path = os.path.abspath(".")
    py_file = os.path.join(current_path, py_file)

    if(os.path.isfile(py_file)):
        return py_file
    else:
        # If path is not set in this .py file
        for file in os.listdir(current_path):
            if file.endswith(".py") and file != "convert_py_to_exe.py":
                py_file = os.path.join(current_path, file)
    
    if(os.path.isfile(py_file)):
        return py_file
    else:
        # Enter Manually if no .py file is found
        for x in range(6):    
            py_file = input("Enter the path to your Python (.py) file: ").strip()
            if os.path.isfile(py_file):
                return py_file
            else:
                print(f"Error: The specified Python file does not exist.\n{5-x} tries left")
        return None

if __name__ == "__main__":
    py_file = find_py_file()
    convert_to_exe(py_file)
