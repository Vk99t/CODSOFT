import tkinter as tk
import tkinter.messagebox

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        tkinter.messagebox.showerror("Error", "Please enter valid numeric values.")
        return
    
    operation = operation_var.get()

    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            tkinter.messagebox.showerror("Error", "Division by zero is not allowed.")

# Create a Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Set the background color for the entire application
window.configure(bg="lightgray")

label_num1 = tk.Label(window, text="Enter first number:", font=("Helvetica", 24), bg="lightblue")
label_num1.pack()

# Entry widget
entry_num1 = tk.Entry(window, width=30, font=("Helvetica", 14))
entry_num1.pack(pady=10)

label_num2 = tk.Label(window, text="Enter second number:", font=("Helvetica", 24), bg="lightblue")
label_num2.pack()

# Entry widget
entry_num2 = tk.Entry(window, width=30, font=("Helvetica", 14))
entry_num2.pack(pady=10)

# Create a dropdown menu for selecting the operation
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.config(width=5)
operation_menu.pack()

# Create a Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate, font=("Helvetica", 24), bg="lightblue")
calculate_button.pack(pady=5)

result_label = tk.Label(window, text="Result:", font=("Helvetica", 24))
result_label.pack(pady=10)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Helvetica", 24))  # Set the font size here (adjust as needed)
result_label.pack()

# Run the main loop
window.mainloop()
