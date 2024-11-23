import tkinter as tk
from tkinter import ttk


class LoginApp(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()


    def create_widgets(self):        
        self.master.title("Login")
        self.master.geometry("390x844")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Create a frame for the login form
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add the Login Title
        self.login_label = tk.Label(self.frame, text="LOGIN", font=("Helvetica", 24, "bold"), fg="black", bg="white")
        self.login_label.pack(pady=(10, 20))

        # Email Entry
        self.email_label = tk.Label(self.frame, text="Email", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.email_label.pack(fill="x")
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.pack(fill="x", pady=(5, 10))

        # Password Entry
        self.password_label = tk.Label(self.frame, text="Password", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.password_label.pack(fill="x")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.pack(fill="x", pady=(5, 10))

        # Login Button
        self.login_button = tk.Button(
            self.frame,
            text="Log in",
            bg=self.btn_color,
            fg="white",
            font=("Helvetica", 12),
            relief="flat",
            command=lambda: [self.master.show_screen2()]

            # command=self.login #
        )
        self.login_button.pack(fill="x", pady=(20, 5))

        # Forgot Password
        self.forgot_password = tk.Label(
            self.frame, text="Forgot Password?", font=("Helvetica", 10), fg="gray", bg="white", cursor="hand2"
        )
        self.forgot_password.pack()

        # Divider
        self.divider_frame = tk.Frame(self.frame, bg="white", pady=10)
        self.divider_frame.pack(fill="x", pady=10)
        tk.Frame(self.divider_frame, height=1, bg="gray").pack(side="left", expand=True, fill="x", padx=5)
        tk.Label(self.divider_frame, text="or", font=("Helvetica", 10), bg="white").pack(side="left")
        tk.Frame(self.divider_frame, height=1, bg="gray").pack(side="left", expand=True, fill="x", padx=5)

        # Create Account Button
        self.create_account_button = tk.Button(
            self.frame, text="Create Account", bg=self.btn_color, fg="white", font=("Helvetica", 12),
            relief="flat", command=self.master.show_screen3
        )
        self.create_account_button.pack(fill="x", pady=(10, 0))
        # Add more widgets here as needed

    def login(self):
        print("Login pressed")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoginApp(master=root)
#     app.pack(fill='both', expand=True)
#     root.mainloop()