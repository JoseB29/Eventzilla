import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("390x844")  # iPhone size 


# Styling
bg_color = "#F5F5F5"
btn_color = "#25A03D"
root.configure(bg=bg_color)

# Create a frame for the login form
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Add the Login Title
login_label = tk.Label(frame, text="LOGIN", font=("Helvetica", 24, "bold"), fg="black", bg="white")
login_label.pack(pady=(10, 20))

# Email Entry
email_label = tk.Label(frame, text="Email", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
email_label.pack(fill="x")
email_entry = ttk.Entry(frame)
email_entry.pack(fill="x", pady=(5, 10))

# Password Entry
password_label = tk.Label(frame, text="Password", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
password_label.pack(fill="x")
password_entry = ttk.Entry(frame, show="*")
password_entry.pack(fill="x", pady=(5, 10))

# Login Button
login_button = tk.Button(
    frame,                      # Parent widget
    text="Log in",              # Text to display on the button
    bg=btn_color,               # Background color
    fg="white",                 # Text color
    font=("Helvetica", 12),     # Font of the text
    relief="flat",              # Flat relief style to remove border
    command=lambda: print("login")  # Command when button is clicked
)
login_button.pack(fill="x", pady=(20, 5))

# Forgot Password
forgot_password = tk.Label(frame, text="Forgot Password?", font=("Helvetica", 10), fg="gray", bg="white", cursor="hand2")
forgot_password.pack()

# Divider
divider_frame = tk.Frame(frame, bg="white", pady=10)
divider_frame.pack(fill="x", pady=10)
tk.Frame(divider_frame, height=1, bg="gray").pack(side="left", expand=True, fill="x", padx=5)
tk.Label(divider_frame, text="or", font=("Helvetica", 10), bg="white").pack(side="left")
tk.Frame(divider_frame, height=1, bg="gray").pack(side="left", expand=True, fill="x", padx=5)

# Create Account
create_account_button = tk.Button(
    frame, text="Create Account", bg=btn_color, fg="white", font=("Helvetica", 12),
    relief="flat", command=lambda: print("Create Account Pressed")
)
create_account_button.pack(fill="x", pady=(10, 0))

# Run the application
root.mainloop()