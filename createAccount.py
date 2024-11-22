import tkinter as tk
from tkinter import ttk

class CreateAccount(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Create Account")
        self.master.geometry("390x844")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Create a frame for the create account form
        self.frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Add the First Name Title
        self.first_name_label = tk.Label(self.frame, text="FIRST NAME", font=("Helvetica", 24, "bold"), fg="black", bg="white")
        self.first_name_label.pack(pady=(10, 20))

        # Last Name Entry
        self.last_name_label = tk.Label(self.frame, text="LAST NAME", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.last_name_label.pack(fill="x")
        self.last_name_entry = tk.Entry(self.frame)
        self.last_name_entry.pack(fill="x", pady=(5, 10))

        # Email Entry
        self.email_label = tk.Label(self.frame, text="EMAIL", font=("Helvetica", 12), fg="black", bg="white", anchor="w")
        self.email_label.pack(fill="x")
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack(fill="x", pady=(5, 10))

        # Next Button
        self.next_button = tk.Button(
            self.frame, text="NEXT (GOES BACK TO LOGIN)", bg=self.btn_color, fg="white", font=("Helvetica", 12, "bold"),
            command=self.master.show_screen1
        )
        self.next_button.pack(pady=(20, 10))

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CreateAccount(master=root)
#     app.pack(fill='both', expand=True)
#     root.mainloop()