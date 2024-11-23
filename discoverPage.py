import tkinter as tk
from tkinter import ttk
# import ticketMasterDMA as tm

class DicoverPage(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):        
        self.master.title("Discover")
        self.master.geometry("390x844")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        #add a green bar at the top of the screen
        self.green_bar = tk.Frame(self.master, bg=self.btn_color, height=90)
        self.green_bar.pack(fill="x")

        #add a title at the center of the top green bar
        self.title = tk.Label(self.green_bar, text="Discover", font=("Odibee Sans", 24, "bold"), fg="white", bg=self.btn_color)
        self.title.place(relx=0.5, rely=0.5, anchor="center")
        #now add one at the bottom
        self.green_bar_bottom = tk.Frame(self.master, bg=self.btn_color, height=70)
        self.green_bar_bottom.pack(fill="x", side="bottom")

        #add a back button to the log in page
        self.back_button = tk.Button(
            self.master,
            text="Back",
            bg=self.btn_color,
            fg="white",
            font=("Helvetica", 12),
            relief="flat",
            command=lambda: [self.master.show_screen1()]
        )
        self.back_button.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = DicoverPage(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
