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

    def confirm_code(self):
        code = self.code_entry.get()
        if self.validate_code(code):
            messagebox.showinfo("Success", "Email confirmed successfully!")
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