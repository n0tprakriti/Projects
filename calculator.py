import tkinter as tk
from tkinter import messagebox
import math

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        # Only get second number if operation needs it
        operation = operation_var.get()

        if operation != '√':
            num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            result = num1 // num2
        elif operation == '√':
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number")
            result = math.sqrt(num1)
        else:
            result_label.config(text="Invalid Operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x360")
root.resizable(False, False)

# First number input
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# Second number input
tk.Label(root, text="Enter second number (skip for √):").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Operation selector
tk.Label(root, text="Choose Operation:").pack(pady=5)
operation_var = tk.StringVar(root)
operation_var.set('+')
operations = ['+', '-', '*', '/', '%', '**', '//', '√']
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result: ", font=('Arial', 14), fg='blue')
result_label.pack(pady=10)

# Footer
tk.Label(root, text="Created with ♥ in Python", font=("Arial", 10, "italic")).pack(pady=10)

# Run the application
root.mainloop()
