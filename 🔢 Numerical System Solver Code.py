import tkinter as tk
from tkinter import messagebox, ttk

def Solve_number():
    try:
        number = entry_number.get()
        base = int(base_var.get())

        decimal_number = int(number, base)
        binary = bin(decimal_number)[2:]
        octal = oct(decimal_number)[2:]
        hexadecimal = hex(decimal_number)[2:].upper()

        result_decimal.config(text=f"{decimal_number}")
        result_binary.config(text=f"{binary}")
        result_octal.config(text=f"{octal}")
        result_hex.config(text=f"{hexadecimal}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number and base.")

def Delete_fields():
    entry_number.delete(0, tk.END)
    result_decimal.config(text="")
    result_binary.config(text="")
    result_octal.config(text="")
    result_hex.config(text="")

                                                ####### GUI #######
myApp = tk.Tk()
myApp.title("Numerical System Solver")
myApp.geometry("650x520")
myApp.configure(bg="AntiqueWhite")  


font_style = ("Comic Sans MS", 14, "bold")
button_color = "HotPink"
text_color = "FireBrick"


tk.Label(myApp, text="Numerical Systems Solver", font=("Segoe UI", 18, "bold"), fg=text_color, bg="AntiqueWhite").grid(row=0, column=0, columnspan=2, pady=15)


tk.Label(myApp, text="Enter the number:", font=font_style, fg=text_color, bg="AntiqueWhite").grid(row=1, column=0, sticky="w", padx=30, pady=5)
entry_number = ttk.Entry(myApp, font=font_style, width=25, justify="center")
entry_number.grid(row=1, column=1, pady=5)


tk.Label(myApp, text="Select the base:", font=font_style, fg=text_color, bg="AntiqueWhite").grid(row=2, column=0, sticky="w", padx=30, pady=5)
base_var = tk.StringVar(value="000")
base_options = ["2", "8", "10", "16"]
base_menu = ttk.Combobox(myApp, textvariable=base_var, values=base_options, font=font_style, width=23)
base_menu.grid(row=2, column=1, pady=5)


Solve_button = tk.Button(myApp, text="SOLVE", command=Solve_number, font=font_style, bg=button_color, fg="white", width=18, relief="flat")
Solve_button.grid(row=3, column=0, columnspan=2, pady=15)


Delete_button = tk.Button(myApp, text="Delete", command=Delete_fields, font=font_style, bg="white", fg="black", width=18, relief="flat")
Delete_button.grid(row=4, column=0, columnspan=2, pady=5)


tk.Label(myApp, text="Decimal:", font=font_style, fg="Crimson", bg="AntiqueWhite").grid(row=5, column=0, sticky="e", padx=30, pady=5)
result_decimal = tk.Label(myApp, text="", font=font_style, fg="Crimson", bg="AntiqueWhite")
result_decimal.grid(row=5, column=1, sticky="w")

tk.Label(myApp, text="Binary:", font=font_style, fg="Teal", bg="AntiqueWhite").grid(row=6, column=0, sticky="e", padx=30, pady=5)
result_binary = tk.Label(myApp, text="", font=font_style, fg="Teal", bg="AntiqueWhite")
result_binary.grid(row=6, column=1, sticky="w")

tk.Label(myApp, text="Octal:", font=font_style, fg="DarkOrange", bg="AntiqueWhite").grid(row=7, column=0, sticky="e", padx=30, pady=5)
result_octal = tk.Label(myApp, text="", font=font_style, fg="DarkOrange", bg="AntiqueWhite")
result_octal.grid(row=7, column=1, sticky="w")

tk.Label(myApp, text="Hexadecimal:", font=font_style, fg="Purple", bg="AntiqueWhite").grid(row=8, column=0, sticky="e", padx=30, pady=5)
result_hex = tk.Label(myApp, text="", font=font_style, fg="Purple", bg="AntiqueWhite")
result_hex.grid(row=8, column=1, sticky="w")

myApp.mainloop()