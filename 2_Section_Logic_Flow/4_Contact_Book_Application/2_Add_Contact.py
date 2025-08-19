"""
Now, create the add_contact function that takes one argument: contact_book (a dictionary). The function should:

Get input for the contact's name, phone, email, and address.
Check if the name already exists in the dictionary. If it does, print: "Contact already exists!".
If not, save the contact in the following format:

contact_book[name] = {
	"phone": phone,
	"email": email,
	"address": address
}
Then print: "Contact added successfully!".
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
