import tkinter as tk
from tkinter import messagebox
import json
 
 
class ConfirmEmailScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Confirm Email")
        self.master.geometry("390x934")

        self.label = tk.Label(self, text="Enter your one-time code:")
        self.label.pack(pady=10)

        self.code_entry = tk.Entry(self)
        self.code_entry.pack(pady=10)

        self.confirm_button = tk.Button(self, text="Confirm", command=self.confirm_code)
        self.confirm_button.pack(pady=10)

    def add_user_to_json(self, user_email):
        # Load the existing data from the JSON file
        try:
            with open("myEvents.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []  # If file doesn't exist, start with an empty list

        # Check if user already exists in the data
        user_found = False
        for user in data:
            if user['email'] == user_email:
                user_found = True
                break
        
        # If user doesn't exist, create a new entry
        if not user_found:
            data.append({
                "email": user_email,
                "favorites": []
            })

            # Write the updated data back to the file
            with open("myEvents.json", "w") as f:
                json.dump(data, f, indent=4)

    def confirm_code(self):
        code = self.code_entry.get()
        if self.validate_code(code):
            messagebox.showinfo("Success", "Email confirmed successfully!")

            email = self.master.email

            # add the user to the json file
            self.add_user_to_json(email)

            # go back to the survey screen
            self.master.show_screen5()
        else:
            messagebox.showerror("Error", "Invalid code")

    def validate_code(self, code):
        with open("confirmation_codes.json", "r+") as f:
            codes = json.load(f)
            if code not in codes:
                return False
            # remove the code from the json file
            codes.pop(code)
            f.seek(0)
            f.truncate()
            json.dump(codes, f, indent=4)
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfirmEmailScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()