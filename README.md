# 🔢 Numerical System Solver

A sleek and interactive **Numerical System Solver** built with Python and Tkinter.  
This tool converts numbers between binary, octal, decimal, and hexadecimal systems with ease, providing instant results and an elegant user experience.

---

## 🔍 Features

✨ **Instant Conversion Between Number Systems**  
🎯 **Dropdown Base Selector for Easy Input**  
🎨 **Color-coded Output for Clear Visualization**  
🧹 **Clear Button to Reset Input and Results**  
⚠️ **Error Handling with Friendly Alerts**  
💻 **Modern UI Design with Custom Fonts and Colors**

---

## 🎯 Supported Number Bases

The app supports input in:

- Binary (Base 2)  
- Octal (Base 8)  
- Decimal (Base 10)  
- Hexadecimal (Base 16)

Enter your number, select its base, and press **SOLVE** to see all equivalent forms.

---

## 📸 Preview

> *(Insert screenshot of the app here if available)*

---

## 🚀 How to Run

1. Ensure **Python 3.x** is installed on your system.  
2. Save the script as `numerical_system_solver.py`.  
3. Run it via terminal or command prompt:

   ```bash
   python numerical_system_solver.py
🧰 Requirements
Python 3.6 or higher

Built-in tkinter module (usually included by default)

Built-in messagebox and ttk modules for UI components

No external dependencies required!

🧠 Logic Overview
The app reads the number as a string along with its base.

Converts the input number to decimal using Python's int(number, base).

Uses built-in functions to convert decimal to other bases:

bin() for binary

oct() for octal

hex() for hexadecimal

Displays all results in a color-coded manner for easy distinction.

🎨 User Interface
The interface boasts a warm AntiqueWhite background and uses Comic Sans MS font in bold for clarity and friendliness. Buttons and labels have vibrant colors for each number system:

System	Color
Decimal	Crimson
Binary	Teal
Octal	DarkOrange
Hexadecimal	Purple

🧼 File Structure

numerical_system_solver/
├── numerical_system_solver.py    # Main GUI script
└── README.md                     # This file
💡 Future Enhancements (Ideas)
Add support for arbitrary bases beyond 2, 8, 10, and 16

Copy-to-clipboard functionality for results

Batch conversion for multiple numbers

Dark mode toggle for user preference

Input validation improvements with real-time feedback

🤝 Author
Created with ❤️ using Python & Tkinter
[Zeinab Talaat] – [https://github.com/ZeinabTalaat]
[Zeinab Samaha] – [https://www.linkedin.com/in/zeinab-samaha-8887b332a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app]

📜 License
This project is licensed under the MIT License.
