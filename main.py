import tkinter as tk
from tkinter import simpledialog
from address_book import AddressBook
from contact import Contact

class AddressBookApp:
    def __init__(self, address_book):
        self.address_book = address_book

        self.root = tk.Tk()
        self.root.title("Address Book")

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.display_button = tk.Button(self.root, text="Display Contacts", command=self.display_contacts)
        self.display_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        self.root.mainloop()



    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter contact phone:")
        email = simpledialog.askstring("Input", "Enter contact email:")

        new_contact = Contact(name, phone, email)
        self.address_book.add_contact(new_contact)

    def display_contacts(self):
        self.address_book.display_contacts()

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        self.address_book.delete_contact(name)

if __name__ == "__main__":
    address_book = AddressBook()
    app = AddressBookApp(address_book)

