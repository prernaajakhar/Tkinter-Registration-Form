import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    if not name or not email or not age:
        messagebox.showerror("Input Error", "All fields are required.")
        return
    
    # You can add code here to handle the form data (e.g., save to a file or database)
    
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}")
    clear_form()

# Function to clear the form fields
def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place labels and entry fields for Name, Email, and Age
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
