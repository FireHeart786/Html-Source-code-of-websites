import tkinter as tk

import urllib.request

class SimpleBrowser(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master

        self.master.title("Simple Browser")

        self.master.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):

        # Create URL entry field

        self.url_label = tk.Label(self.master, text="URL:")

        self.url_label.pack(side=tk.TOP, padx=(10, 0), pady=(10, 0))

        self.url_entry = tk.Entry(self.master, width=50)

        self.url_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 0), pady=(10, 0))

        # Create "Go" button

        self.go_button = tk.Button(self.master, text="Go", command=self.get_webpage)

        self.go_button.pack(side=tk.TOP, padx=(10, 0), pady=(10, 0))

        # Create Text widget for displaying web page

        self.text = tk.Text(self.master)

        self.text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 0))

    def get_webpage(self):

        # Get URL from entry field

        url = self.url_entry.get()

        # Check if URL is valid

        if not url.startswith("http"):

            url = "http://" + url

        try:

            # Open URL and read contents

            with urllib.request.urlopen(url) as response:

                html = response.read().decode()

        except:

            html = "Error loading webpage."

        # Display webpage in Text widget

        self.text.delete(1.0, tk.END)

        self.text.insert(tk.END, html)

root = tk.Tk()

app = SimpleBrowser(master=root)

app.mainloop()

