import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Entry widget to display input and result
        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Create and place buttons
        for i, button in enumerate(self.buttons):
            row = i // 4 + 1
            col = i % 4
            tk.Button(master, text=button, padx=20, pady=10, command=lambda b=button: self.handle_click(b)) \
                .grid(row=row, column=col)

        self.clear = False

    def handle_click(self, value):
        current = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            if self.clear:
                self.entry.delete(0, tk.END)
                self.clear = False
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
