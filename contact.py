class Contact:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

def add_contact(contacts):
    while True:
        print("\nADD A NEW CONTACT")
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        address = input("Address: ")

        new_contact = Contact(name, phone_number, address)
        contacts.append(new_contact)

        print("\nNew Contact added successfully.")
        print("\nALL CONTACTS\n")
        for contact in contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Address: {contact.address}")

        user_choice = input("\nPress 'q' to add another contact, 'm' to return to the main menu or 'e' to exit: ").lower()
        if user_choice == 'q':
            continue
        elif user_choice == 'm':
            return
        elif user_choice == 'e':
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

def search_contact(contacts):
    pass # implement search_contact functionality here

def delete_contact(contacts):
    pass # implement delete_contact functionality here

def display_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Address: {contact.address}")

contacts = []
while True:
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        search_contact(contacts)
    elif choice == '3':
        delete_contact(contacts)
    elif choice == '4':
        display_contacts(contacts)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid choice.")