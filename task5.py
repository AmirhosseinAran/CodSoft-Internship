class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact for {name} added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
                results.append(contact)
        return results

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
                contact['address'] = new_address
                print(f"Contact information for {name} updated successfully!")
                return
        print(f"Contact with name {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print(f"Contact with name {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if search_results:
                print("Search Results:")
                for result in search_results:
                    print(result)
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
