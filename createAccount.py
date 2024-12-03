import tkinter as tk
from tkinter import ttk
import json
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
 
class CreateAccount(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Create Account")
        self.master.geometry("390x934")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Create a frame for the create account form
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Create an Account", font=("Helvetica", 16, "bold"), bg="green", fg="white")
        title_label.pack(pady=10)

        # Add the Username Entry
        self.username_label = tk.Label(self.frame, text="USERNAME", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.username_label.pack(fill="x")
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack(fill="x", pady=(5, 10))

        # Date of Birth Entry
        self.dob_label = tk.Label(self.frame, text="DATE OF BIRTH (YYYY-MM-DD)", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.dob_label.pack(fill="x")
        self.dob_entry = tk.Entry(self.frame)
        self.dob_entry.pack(fill="x", pady=(5, 10))
        self.dob_entry.bind("<FocusOut>", self.validate_dob)

        # Email Entry
        self.email_label = tk.Label(self.frame, text="EMAIL", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.email_label.pack(fill="x")
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(fill="x", pady=(5, 10))

        # Confirm Email Entry
        self.confirm_email_label = tk.Label(self.frame, text="CONFIRM EMAIL", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.confirm_email_label.pack(fill="x")
        self.confirm_email_entry = tk.Entry(self.frame)
        self.confirm_email_entry.pack(fill="x", pady=(5, 10))

        # Password Entry    
        self.password_label = tk.Label(self.frame, text="PASSWORD", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.password_label.pack(fill="x")
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack(fill="x", pady=(5, 10))

        # Confirm Password Entry
        self.confirm_password_label = tk.Label(self.frame, text="CONFIRM PASSWORD", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.confirm_password_label.pack(fill="x")
        self.confirm_password_entry = tk.Entry(self.frame, show="*")
        self.confirm_password_entry.pack(fill="x", pady=(5, 10))

        # Add a button to save the data
        self.save_button = tk.Button(self.frame, text="Create Account", bg=self.btn_color, fg="white", command=self.save_user_data)
        self.save_button.pack(fill="x", pady=(10, 0))

    def validate_dob(self, event):
        dob = self.dob_entry.get()
        if not re.match(r"\d{4}-\d{2}-\d{2}", dob):
            self.error_label = tk.Label(self.frame, text="Invalid date format. Use YYYY-MM-DD.", font=("Helvetica", 12), fg="red", bg="white")
            self.error_label.pack(fill="x", pady=(5, 10))
        else:
            if hasattr(self, 'error_label'):
                self.error_label.destroy()

    def save_user_data(self):
        username = self.username_entry.get()
        dob = self.dob_entry.get()
        email = self.email_entry.get()
        confirm_email = self.confirm_email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not dob or not email or not confirm_email or not password or not confirm_password:
            if hasattr(self, 'error_label'):
                self.error_label.destroy()
            self.error_label = tk.Label(self.frame, text="Please fill in all fields", font=("Helvetica", 12), fg="red", bg="white")
            self.error_label.pack(fill="x", pady=(5, 10))
            return
        
        if password != confirm_password:
            if hasattr(self, 'error_label'):
                self.error_label.destroy()
            self.error_label = tk.Label(self.frame, text="Passwords do not match", font=("Helvetica", 12), fg="red", bg="white")
            self.error_label.pack(fill="x", pady=(5, 10))
            return

        if email != confirm_email:
            if hasattr(self, 'error_label'):
                self.error_label.destroy()
            self.error_label = tk.Label(self.frame, text="Emails do not match", font=("Helvetica", 12), fg="red", bg="white")
            self.error_label.pack(fill="x", pady=(5, 10))
            return

        user_data = {
            "username": username,
            "dob": dob,
            "email": email,
            "password": password
        }

        if not os.path.exists('users.json'):
            with open('users.json', 'w') as file:
                json.dump([], file)

        with open('users.json', 'r+') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
            users.append(user_data)
            file.seek(0)
            json.dump(users, file, indent=4)

        print("User data saved successfully")
        self.send_confirmation_email(email)

        #save the email to the master
        self.master.email = email

        # confirm email screen
        self.master.show_screen4()


    def generate_confirmation_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def send_confirmation_email(self, to_email):
        from_email = "arlette.diaz35@gmail.com"
        from_password = "ttyc xthn wpml yuwm"
        subject = "Account Confirmation"
        confirmation_code = self.generate_confirmation_code()
        body = f"Thank you for creating an account. Your confirmation code is: {confirmation_code}"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print("Confirmation email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")

        # Save the confirmation code to a file or database
        with open('confirmation_codes.json', 'r+') as file:
            try:
                codes = json.load(file)
            except json.JSONDecodeError:
                codes = {}
            codes[confirmation_code] = to_email
            file.seek(0)
            json.dump(codes, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateAccount(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()