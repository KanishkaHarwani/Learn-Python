"""
contact_book — A contact book using a dict of dicts (name -> {phone, email}), with add/search/delete functionality.
"""
# Include section
import sys
import re

# Below is the contact book and all numbers are 5 digits and the emails are non-working
contacts = {
    "kka": {"Phones" : "929478281", "email" : "kk@kanishk.com"},
    "shi": {"Phones" : "782164985", "email" : "shi@meanperson.com"},
    "mn": {"Phones" : "864351257", "email" : "mn@coolpeep.com"}
}

def starting_message():
    print("Welcome to the contact book")
    print("you can access the contacts using commands: add/search/delete")
    print("you can access the full contacts list use command: fulldir")
    print("to know your commands type help")
    print("you can quit the contacts using exit as commands")
def help_commands():
    print("you can access the contacts using commands: add/search/delete")
    print("you can access the full contacts list use command: fulldir")
    print("you can quit the contacts using exit as commands")
def add_contact():
    valid_n, name, ctc_n = get_name()
    if valid_n is True and ctc_n is True:
        print("Name already exists in contact list")
        add_contact()
    elif valid_n is True and ctc_n is not True:
        valid_p, phone, ctc_p = get_phone()
        if valid_p is True and ctc_p is True:
            print("Phone already exists in contact list")
            add_contact()
        elif valid_p is True and ctc_p is False:
            valid_e, email, ctc_e = get_email()
            if valid_e is True and ctc_e is True:
                print("Email already exists in contact list")
                add_contact()
            elif valid_e is True and ctc_e is False:
                contacts[name] = {"Phones" : phone, "email" : email}
                temp_phone = contacts[name]["Phones"]
                temp_email = contacts[name]["email"]
                print("Details successfully to the contact list")
                print(f"name: {name}, Phone: {temp_phone}, Email: {temp_email}")
            else:
                print("Entered email is not valid")
                add_contact()
        else:
            print("Entered number is not valid")
            add_contact()
    else:
        print("Entered name is invalid")
        add_contact()
def search_contact():
    valid, name, ctc = get_name()
    if valid is True and ctc is True:
        phone_s = contacts[name]["Phones"]
        email_s = contacts[name]["email"]
        print("print contacts here")
        print(f"name: {name}, Phone: {phone_s}, Email: {email_s}")
    else:
        print("Entered name is not valid or not in the list")
        search_contact()
def delete_contact():
    valid, name, ctc = get_name()
    if valid is True and ctc is True:
        permission = input("press 'y' or 'n' to confirm/reject the deletion of contact.").lower()
        if permission == "y":
            contacts.pop(name)
        else:
            print("deletion rejected")
    else:
        print("Invalid details provided for deletion")
def full_directory():
    print("Here is the full directory")
    for name in contacts:
        temp_phone = contacts[name]["Phones"]
        temp_email = contacts[name]["email"]
        print(f"name: {name}, Phone: {temp_phone}, Email: {temp_email}")
def get_name():
    name = input("Please enter name or 'exit' to exit the program: ").lower()
    check_end_program(name)
    if name.isalpha() and name in contacts:
        return True, name, True
    elif name.isalpha() and name not in contacts:
        return True, name, False
    else:
        return False, name, False
def get_phone():
    phone = input("Please enter your phone number or 'exit' to exit the program: ").lower()
    check_end_program(phone)
    if len(phone) == 9 and phone.isdigit():
        for name, details in contacts.items():
            if details["Phones"] == phone:
                ctc_p = True
                break
        else:
            ctc_p = False
        return True, phone, ctc_p
    else:
        return False, phone, False
def get_email():
    email_e = input("Please enter your email ID or 'exit' to exit the program: ").lower()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid_e =  re.match(pattern, email_e) is not None
    for name, details in contacts.items():
        if details["email"] == email_e:
            ctc_e = True
            break
    else:
        ctc_e = False
    return valid_e, email_e, ctc_e
def check_end_program(name):
    if name == "exit":
        print("ending program")
        sys.exit()
def main():
    while True:
        command = input("Please enter your command: ").lower()
        match command:
            case "add":
                add_contact()
            case "search":
                search_contact()
            case "delete":
                delete_contact()
            case "exit":
                check_end_program("exit")
            case "help":
                help_commands()
            case "fulldir":
                full_directory()
            case _:
                print("Please enter a valid command")

if __name__ == "__main__":
    starting_message()
    main()
