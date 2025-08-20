"""
The next step is to create the delete_contact function. This function will allow users to remove a specific contact from the Contact Book.

Your Task:
Create a function named delete_contact that takes one argument: contact_book (a dictionary).
Get input for the contact's name that the user wants to delete.
Check if the name exists in the contact_book:
If it exists, remove the contact from the dictionary.
Print: "Contact deleted successfully!".
If the contact does not exist, print: "Contact not found!".
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