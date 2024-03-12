import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.password_length_label = ttk.Label(master, text="Password Length:")
        self.password_length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.password_length_entry = ttk.Entry(master, width=10)
        self.password_length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.complexity_label = ttk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.complexity_combobox = ttk.Combobox(master, values=["Low", "Medium", "High"], width=10, state="readonly")
        self.complexity_combobox.current(0)
        self.complexity_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = ttk.Label(master, text="Your Password:")
        self.password_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.password_entry = ttk.Entry(master, width=30, state="readonly")
        self.password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def generate_password(self):
        length = int(self.password_length_entry.get())
        complexity = self.complexity_combobox.get()

        if complexity == "Low":
            chars = string.ascii_letters + string.digits
        elif complexity == "Medium":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
