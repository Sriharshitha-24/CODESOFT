import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Fonts and Colors
        self.font = ("Helvetica", 12)
        self.bg_color = "#f0f0f0"
        self.button_bg = "#4CAF50"
        self.button_fg = "white"
        self.text_bg = "white"

        # Task Entry
        self.task_entry = tk.Entry(master, width=30, font=self.font)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # Add Task Button
        add_image = Image.open("plus.png").resize((20, 20), Image.ANTIALIAS)
        self.add_icon = ImageTk.PhotoImage(add_image)
        self.add_button = tk.Button(master, image=self.add_icon, bg=self.button_bg, fg=self.button_fg,
                                    font=self.font, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(master, width=30, height=10, font=self.font, bg=self.text_bg)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Mark Complete Button
        complete_image = Image.open("checked.png").resize((20, 20), Image.ANTIALIAS)
        self.complete_icon = ImageTk.PhotoImage(complete_image)
        self.complete_button = tk.Button(master, image=self.complete_icon, bg=self.button_bg, fg=self.button_fg,
                                            font=self.font, command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        # Remove Task Button
        remove_image = Image.open("remove.png").resize((20, 20), Image.ANTIALIAS)
        self.remove_icon = ImageTk.PhotoImage(remove_image)
        self.remove_button = tk.Button(master, image=self.remove_icon, bg=self.button_bg, fg=self.button_fg,
                                        font=self.font, command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks.remove(task)
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks.remove(task)
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def load_tasks(self):
        try:
            with open("todo.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    self.tasks.append(task)
            self.refresh_tasks()
        except FileNotFoundError:
            pass

    def refresh_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    root.geometry("350x300")
    root.configure(bg="#f0f0f0")
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
