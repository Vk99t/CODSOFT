import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = entry.get()
    if task:
        task_number = len(task_list.get(0, tk.END)) + 1
        task_with_number = f"{task_number}. {task}"
        task_list.insert(tk.END, task_with_number)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
        
        # Update the task numbers in the listbox after deletion
        for i in range(selected_task_index, task_list.size()):
            task = task_list.get(i)
            task_number = i + 1
            updated_task = f"{task_number}. {task.split('. ', 1)[1]}"
            task_list.delete(i)
            task_list.insert(i, updated_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        
        # Add the completed task to the completed list without the number
        completed_list.insert(tk.END, task.split('. ', 1)[1])
        
        # Update the task numbers in the listbox after marking as completed
        for i in range(selected_task_index, task_list.size()):
            task = task_list.get(i)
            task_number = i + 1
            updated_task = f"{task_number}. {task.split('. ', 1)[1]}"
            task_list.delete(i)
            task_list.insert(i, updated_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = task_list.curselection()[0]
        updated_task = entry.get()
        if updated_task:
            task_number = selected_task_index + 1
            task_with_number = f"{task_number}. {updated_task}"
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, task_with_number)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")


# Set the background color for the entire application
app.configure(bg="lightgray")

# Create a title label with an increased font size
title_label = tk.Label(app, text="To-Do List", font=("Helvetica", 24))
title_label.pack()

# Entry widget to add new tasks or update existing tasks
entry = tk.Entry(app, width=40, font=("Helvetica", 14))
entry.pack(pady=10)

# Button to add a new task
add_button = tk.Button(app, text="Add Task", command=add_task, font=("Helvetica", 12))
add_button.pack(pady=5)  # Add space (break) below the button

# Listbox to display tasks
task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, font=("Helvetica", 12))
task_list.pack(pady=10)

# Button to delete a task
delete_button = tk.Button(app, text="Delete Task", command=delete_task, font=("Helvetica", 12))
delete_button.pack(pady=5)  # Add space (break) below the button

# Button to mark a task as completed
complete_button = tk.Button(app, text="Mark as Completed", command=mark_completed, font=("Helvetica", 12))
complete_button.pack(pady=5)  # Add space (break) below the button

# Button to update a task
update_button = tk.Button(app, text="Update Task", command=update_task, font=("Helvetica", 12))
update_button.pack(pady=5)  # Add space (break) below the button

# Listbox to display completed tasks
completed_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, font=("Helvetica", 12))
completed_list.pack(pady=10)


# Calculate the center position for the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = app.winfo_reqwidth()
window_height = app.winfo_reqheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window to be centered
app.geometry("+{}+{}".format(x, y))

# Run the application
app.mainloop()
