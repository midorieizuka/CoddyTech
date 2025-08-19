"""
The next step is to create the list_all_contacts function.
This function will allow users to view all the contacts stored in the Contact Book along with their details.

Your Task:
Create a function named list_all_contacts that takes one argument: contact_book (a dictionary).
Check if the contact_book is empty:
If it is empty, print: "No contacts available.".
If it is not empty:
Loop through each contact in the dictionary and print their name, phone, email, and address in a readable format.
Expected Behavior:
For a contact_book containing:

{
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    "Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}
}
The output should be:

Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St

Name: Bob
Phone: 234-567-8901
Email: bob@example.com
Address: 456 Oak Ave
"""

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if name in contact_book:
        print("Contact already exists!")
    if name not in contact_book:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")


def view_contact(contact_book):
    contact_name = input()
    if contact_name not in contact_book:
        print("Contact not found!")
    else:
        contact_details = contact_book[contact_name]
        print(f"Name: {contact_name}")
        print(f"Phone: {contact_details['phone']}")
        print(f"Email: {contact_details['email']}")
        print(f"Address: {contact_details['address']}")

def edit_contact(contact_book):
    contact_name = input()
    if contact_name in contact_book:
        contact_details = contact_book[contact_name]
        new_phone = input()
        new_email = input()
        new_address = input()
        if new_phone == "":
            contact_book[contact_name]["phone"] = contact_details["phone"]
        else:
            contact_book[contact_name]["phone"] = new_phone
        if new_email == "":
            contact_book[contact_name]["email"] = contact_details["email"]
        else:        
            contact_book[contact_name]["email"] = new_email
        if new_address == "":
            contact_book[contact_name]["address"] = contact_details["address"]
        else:
            contact_book[contact_name]["address"] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    contact_name = input()
    if contact_name in contact_book:
        del contact_book[contact_name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for contact_name in contact_book.keys():
            contact_details = contact_book[contact_name]
            print(f"Name: {contact_name}")
            print(f"Phone: {contact_details['phone']}")
            print(f"Email: {contact_details['email']}")
            print(f"Address: {contact_details['address']}")
            print()

