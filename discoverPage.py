import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class DiscoverPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Discover")
        self.master.geometry("390x844")  # iPhone size

        # Styling
        self.bg_color = "#F5F5F5"
        self.btn_color = "#25A03D"
        self.master.configure(bg=self.bg_color)

        # Add a green bar at the top of the screen
        self.green_bar = tk.Frame(self.master, bg=self.btn_color, height=90)
        self.green_bar.pack(fill="x")

        # Add a title at the center of the top green bar
        self.title = tk.Label(self.green_bar, text="Discover", font=("Odibee Sans", 24, "bold"), fg="white", bg=self.btn_color)
        self.title.place(relx=0.5, rely=0.5, anchor="center")

        # Add a green bar at the bottom of the screen
        self.green_bar_bottom = tk.Frame(self.master, bg=self.btn_color, height=70)
        self.green_bar_bottom.pack(fill="x", side="bottom")

        # Add a scrollable box in between the green bars
        self.canvas = tk.Canvas(self.master, bg=self.bg_color)
        self.scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=(0, 15))
        self.scrollbar.pack(side="right", fill="y")

        # Add sample content to the scrollable frame
        for i in range(20):  # Add 20 labels as an example
            label = tk.Label(self.scrollable_frame, text=f"Sample content {i+1}", bg=self.bg_color)
            label.pack(pady=10)

        # Add a back button to the bottom green bar
        self.back_button = tk.Button(
            self.green_bar_bottom,
            text="Back",
            bg=self.btn_color,
            fg="white",
            font=("Helvetica", 12),
            relief="flat",
            command=self.clear_and_back
        )

        self.back_button.pack(pady=10, side="right")  # Use pack instead of place for simplicity

        
        # Load and add an image to the bottom left of the green bar
        image = Image.open("appElements\\magnifyingIconMagnifying.webp")  # Replace with your image path
        resized_image = image.resize((50, 50), Image.LANCZOS)  # Resize the image to 50x50 pixels
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label = tk.Label(self.green_bar_bottom, image=photo, bg=self.btn_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side="left", padx=10, pady=10)


    def clear_and_back(self):
        # Clear the frame
        for widget in self.master.winfo_children():
            widget.destroy()
        # Switch to the login page
        self.master.show_screen1()


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DicoverPage(master=root)
#     app.pack(fill="both", expand=True)
#     root.mainloop()
