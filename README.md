# USB-AutoRun-Ransomware

**A Python-based ransomware simulator for educational and cybersecurity awareness purposes**

---

## 🔎 Purpose

This project demonstrates how a USB-based executable can simulate ransomware behavior in a safe, controlled, and non-destructive manner. It is designed for:

- Cybersecurity education and awareness
- Ethical hacking and penetration testing training
- Demonstrations in classrooms or workshops on ransomware tactics
- Showcasing system vulnerability via USB autorun payloads (historically exploitable)

---

## 🚩 WARNING

> **This project is for educational use only.**

- It does not perform any real malicious actions like stealing data or spreading.
- It **simulates** encryption by modifying dummy files and displaying a mock lock screen.
- Misuse of this tool outside educational environments may violate laws or institutional policies.

You are fully responsible for how you use this software.

---

## 🚀 How It Works

When a USB containing the executable and `autorun.inf` is inserted (on systems that still support autorun), the program:

1. Creates `README.txt` warning files on the Desktop, Documents, and Downloads folders.
2. Simulates encryption of a dummy folder using symmetric encryption.
3. Displays a fullscreen lock screen demanding a key.
4. Blocks certain system keys like `Windows` and `Alt` to simulate lock-down.

> Note: Autorun is disabled by default on modern Windows versions. Manual execution may be required.

---

## 📆 Requirements

Before using, ensure you have:

- Python 3.7+
- `cryptography` library
- `keyboard` library
- `tkinter` (usually included with Python on Windows)

Install dependencies:
```bash
pip install -r requirements.txt
```

To create an executable:
```bash
python convert_py_to_exe.py
```
The `.exe` will appear in the `dist` folder.

---

## 🚓 Applications

- Cybersecurity demonstrations in school/university settings
- Training exercises for red-team/blue-team environments
- Showing how unprotected USB usage can lead to security risks
- General awareness for non-technical audiences

---

## 🔢 Safety Precautions

- Always run this demo on test systems or virtual machines
- Do not use in production or live environments
- Ensure sensitive data is not present in the test folder (`Dummy folder`)
- Clearly inform users this is a **simulation** before running

---

## 📂 Files Included

- `ransomware.py` - Main ransomware simulation script
- `autorun.inf` - Optional autorun file for legacy Windows systems
- `convert_py_to_exe.py` - Script to package `.py` into `.exe`
- `requirements.txt` - List of required Python libraries

---

## 🌟 License

This project is provided "as is" for educational purposes only. The author holds no responsibility for misuse.

Stay ethical. Stay secure.

---

**Created for cybersecurity education and awareness.**