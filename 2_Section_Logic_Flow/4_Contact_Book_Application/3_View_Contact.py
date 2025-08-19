"""
Create a function named view_contact that displays details of a specific contact.

Your function should:

Take a contact book dictionary as input
Ask the user to enter a contact name
Display the contact's details if found
Print "Contact not found!" if the contact doesn't exist
When displaying a contact, use this exact format:

Name: [name]
Phone: [phone]
Email: [email]
Address: [address]

If the contact book contains Alice's information and the user enters "Alice", output:

Name: Alice
Phone: 123-456-7890
Email: alice@example.com
Address: 123 Main St
If the user enters "Bob" (who doesn't exist), output:

Contact not found!

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
        
