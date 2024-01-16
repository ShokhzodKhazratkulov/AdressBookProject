import pandas as pd
from contact import Contact


class AddressBook:

    def __init__(self, csv_file_name="csv_file.csv"):
        self.csv_file = csv_file_name
        self.contacts = self.load_address_book()

    def load_address_book(self):
        try:
            df = pd.read_csv(self.csv_file)

        except FileNotFoundError:
            return []
        else:
            contacts = [Contact(row["Name"], row["Phone"], row["Email"]) for _, row in df.iterrows()]
            return contacts

    def save_address_book(self):
        data = {"Name": [], "Phone": [], "Email": []}
        for contact in self.contacts:
            data["Name"].append(contact.name)
            data["Phone"].append(contact.phone)
            data["Email"].append(contact.email)
        df = pd.DataFrame(data)
        df.to_csv(self.csv_file, index=False)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_address_book()

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_address_book()



