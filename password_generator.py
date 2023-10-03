import tkinter as tk
import tkinter.messagebox
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
    except ValueError:
        tkinter.messagebox.showerror("Error", "Please enter a valid integer length.")
        return
    
    if password_length <= 0:
        tkinter.messagebox.showerror("Error", "Please enter a valid positive length.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    result_var.set(password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(app, text="Enter Password Length:", font=("Helvetica", 16))
length_label.pack(pady=10)

length_entry = tk.Entry(app, font=("Helvetica", 16))
length_entry.pack(pady=10)

# Button to generate password with blue color
generate_button = tk.Button(app, text="Generate Password", command=generate_password, font=("Helvetica", 16), bg="blue",fg="white")
generate_button.pack(pady=10)

# Entry to display the generated password
result_var = tk.StringVar()
result_entry = tk.Entry(app, textvariable=result_var, state="readonly", font=("Helvetica", 16))
result_entry.pack(pady=10)

# Run the Tkinter main loop
app.mainloop()
