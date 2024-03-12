import tkinter as tk
from tkinter import ttk

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.name_label = ttk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = ttk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ttk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = ttk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = ttk.Entry(master, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.contacts_listbox = tk.Listbox(master, width=50)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.search_label = ttk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.search_entry = ttk.Entry(master, width=30)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)
        self.search_button = ttk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = ttk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.populate_contacts_listbox()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone or not email or not address:
            self.show_warning("Please fill in all fields.")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        self.populate_contacts_listbox()

        self.clear_entries()

    def search_contact(self):
        query = self.search_entry.get().lower()
        results = []

        for contact in self.contacts:
            if query in contact["Name"].lower() or query in contact["Phone"]:
                results.append(contact)

        self.populate_contacts_listbox(results)

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.populate_contacts_listbox()

    def populate_contacts_listbox(self, contacts=None):
        self.contacts_listbox.delete(0, tk.END)
        if contacts is None:
            contacts = self.contacts
        for contact in contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def show_warning(self, message):
        tk.messagebox.showwarning("Warning", message)

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()
