import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eracoding Calculator")

        self.entry_var = tk.StringVar()

        self.entry = ttk.Entry(root, textvariable=self.entry_var, justify="right", font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(root, text=button, command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_entry = self.entry_var.get()

        if value == '=':
            try:
                result = eval(current_entry)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            current_entry += value
            self.entry_var.set(current_entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
