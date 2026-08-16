import json
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

 # Functions    
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_name = input("Enter the name of the contact to search: ")
    found_contacts = [contact for contact in contacts if contact['name'].lower() == search_name.lower()]
    if not found_contacts:
        print("No contacts found with that name.")
    else:
        print("Found Contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def remove_contact():
    if not contacts:
        print("No contacts found")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

        try:
            contact_number = int(input("Enter the contact number you want to remove: "))
        except ValueError:
            print("Invalid input. Please try again")
            return

        if contact_number < 1 or contact_number > len(contacts):
            print("Invalid Input. Please try again")
        else:
            contact_index = contact_number - 1
            removed_contact = contacts[contact_index]
            contacts.pop(contact_index)
            save_contacts()
            print(f"{removed_contact['name']} was removed successfully!")

# Program Start
contacts = load_contacts()
choice = ""

# Menu
while choice != "5":
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")