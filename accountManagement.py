import tkinter as tk
import json
import os
from tkinter import messagebox

class AccountManagementScreen(tk.Frame):
    def __init__(self, master=None, email=None):
        super().__init__(master)
        self.master = master
        self.email = email
        self.user_data = None
        self.load_user_data()
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self, bg="green")
        title_frame.pack(fill=tk.X)

        self.title = tk.Label(title_frame, text="Account Management", font=("Helvetica", 24, "bold"), fg="white", bg="green")
        self.title.pack(expand=True)

        self.username_label = tk.Label(self, text="Username:", font=("Helvetica", 14))
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Helvetica", 14))
        self.username_entry.pack(pady=5)

        self.email_label = tk.Label(self, text="Email:", font=("Helvetica", 14))
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self, font=("Helvetica", 14))
        self.email_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:", font=("Helvetica", 14))
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=5)

        self.load_user_info()

        tk.Button(
            self, text="Done", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20,
            command=self.save_user_data
        ).pack(pady=20)

        tk.Button(
            self, text="Back", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20,
            command=self.master.switch_to_profile_page
        ).pack(pady=20)

    def load_user_data(self):
        user_data = []
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                user_data = json.load(file)

        user = next((u for u in user_data if u["email"] == self.email), None)

        if user and 'username' in user and 'email' in user and 'password' in user:
            self.user_data = {
                "username": user['username'],
                "email": user['email'],
                "password": user['password']
            }
        else:
            print("Error: Missing keys in user data")

    def load_user_info(self):
        if self.user_data:
            self.username_entry.insert(0, self.user_data["username"])
            self.email_entry.insert(0, self.user_data["email"])
            self.password_entry.insert(0, self.user_data["password"])
        else:
            tk.Label(self, text="User data not found", font=("Helvetica", 14)).pack(pady=5)

    def save_user_data(self):
        new_username = self.username_entry.get()
        new_email = self.email_entry.get()
        new_password = self.password_entry.get()

        if not new_username or not new_email or not new_password:
            messagebox.showerror("Error", "All fields are required")
            return

        if os.path.exists("users.json"):
            with open("users.json", "r+") as file:
                users = json.load(file)
                for user in users:
                    if user["email"] == self.email:
                        user["username"] = new_username
                        user["email"] = new_email
                        user["password"] = new_password
                        break
                file.seek(0)
                file.truncate()
                json.dump(users, file, indent=4)

        messagebox.showinfo("Success", "User data updated successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountManagementScreen(master=root, email="josebolanos1229@gmail.com")
    app.pack(fill="both", expand=True)
    root.mainloop()