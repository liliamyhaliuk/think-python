"""
Command-line address-book program.
Using which you can browse, add, modify, delete or search for your contacts such as friends,
family and colleagues and their information such as email address and/or phone number.
Details must be stored for later retrieval.
"""

import os
import pickle
from class_Contact import Contact

# Check if the address_book file already exists
if os.path.isfile("address_book\\address_book.pkl"):
    with open("address_book\\address_book.pkl", 'rb') as f:
        address_book = pickle.load(f)
else:
    # Create new address book
    address_book = {
        'friends' : {},
        'family' : {},
        'colleagues' : {}
    }

def search_contact(contact_name):
    '''Function search for an instance of the contact with passed name'''
    for contact_group in address_book.keys():
        if address_book[contact_group].get(contact_name) is not None:
            return address_book[contact_group].get(contact_name)
    return "Contact doesn't exist."

# Main menu
while True:
    # Get the number of action from the user
    action = input('''
    Address book menu: 
        1 - Browse in address book
        2 - Add new contact
        3 - Modify a contact
        4 - Delete a contact
        5 - Search a contact
        0 - Exit
        Your action: ''')

    # Display all contacts from the address book (browse action)
    if action == "1":
        for key, value in address_book.items():
            # Print group of contacts
            print(f"{key}: ")

            for contact in value.values():
                # Print all contacts in the current group
                print(f" {contact}")

    # Add new contact of the address book (add action)
    if action == "2":

        # Get all attributes of contact from the user
        cont_name = input("Name of the new contact: ")
        cont_email = input("Email of the new contact: ")
        cont_adress = input("Address of the new contact: ")
        cont_phone_number = input("Phone number for the new contact: ")
        cont_group = input("Group of the contact(friends, family, colleagues): ")

        # Create new contact
        new_contact = Contact(cont_name, cont_email, cont_adress, cont_phone_number)

        # Check correctnes of the entered group name
        ERRORS = 0
        while True:
            try:
                # Add new contact to the address book
                address_book[cont_group][new_contact.name] = new_contact
                print("Contact was added!")
                break
            except KeyError:
                ERRORS += 1
                # Check amount of errors
                if ERRORS > 2:
                    print("Contact wasn't added!")
                    break
                cont_group = input("Enter correct group!(friends, family, colleagues): ")          

    # Modify contact from contact book (modify action)
    if action == "3":
        # Get the name of the contact for search
        mod_contact = input("Modify the contact (Enter name): ")
        # Search for the contact with name that user entered
        res = search_contact(mod_contact)
       
        # Check if the contact was found
        if isinstance(res, Contact):
            mod_contact = res
            # Show all information of the found contact to the user
            print(mod_contact)

            # Start process of modifing contact
            # Continue the process of modifing until user pass no
            USER_INPUT = "yes"
            while USER_INPUT == "yes":

                mod_attr = input("What field do you want to modify?: ")
                # Modify name of the contact
                if mod_attr == "name":                  
                    new_name = input("Enter new name: ")

                    # Change the key (name of the contact) in address book dict
                    for key in address_book.keys():
                        if address_book[key].get(mod_contact.name) is not None:
                            # Add contact with new name to the dict
                            address_book[key][new_name] = address_book[key].get(mod_contact.name)
                            # Delete item with old name of the contact
                            del address_book[key][mod_contact.name]
                            mod_contact.name = new_name
                            break

                    USER_INPUT = input('Name was modified. Do you want to modified another field? (yes/no): ' )
                    continue
                # Modify email of the contact
                elif mod_attr == "email":
                    mod_contact.email = input("Enter new email: ")
                    USER_INPUT = input('Email was modified. Do you want to modified another field? (yes/no): ' )
                    continue
                # Modify address of the contact
                elif mod_attr == "address":
                    mod_contact.address = input("Enter new address: ")
                    USER_INPUT = input('Address was modified. Do you want to modified another field? (yes/no): ' )
                    continue
                # Modify phone number of the contact
                elif mod_attr == "phone number":
                    mod_contact.phone_number = input("Enter new phone number: ")
                    USER_INPUT = input('Address was modified. Do you want to modified another field? (yes/no): ' )
                    continue
                else:
                    print("Not valid field. Enter correct modified field!")
        else:
            # Contact wasn't found. Print >> Contact does't exist
            print(res)

    # Delete a contact from address book
    if action == "4":
        # Get the name of the contact that has to be deleted
        del_contact = input("Delete contact (Enter name): ")
        
        # Find a contact in the groups of contacts
        for key in address_book.keys():
            if address_book[key].get(del_contact) is not None:
                del address_book[key][del_contact]
                print("Contact was deleted!")
                break
        else:
            print("Contact doesn't exist.")
  
    # Search a contact in address book
    if action == "5":
        s_name = input("Search for the contact (Enter name): ")
        print(search_contact(s_name))

    # Exit from the programm
    if action == "0":
        break


# Save address book for later retrieval
with open("address_book\\address_book.pkl", "wb+") as f:
    pickle.dump(address_book, f)
