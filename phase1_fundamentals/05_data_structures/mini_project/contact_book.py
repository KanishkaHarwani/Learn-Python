"""
contact_book — A contact book using a dict of dicts (name -> {phone, email}), with add/search/delete functionality.
thi code was optimized using AI, though it follows the same main structure the inner workings are more refined.
"""
import sys
import re

# All numbers are 9 digits and the emails are non-working (sample data)
contacts = {
    "kka": {"phone": "929478281", "email": "kk@kanishk.com"},
    "si": {"phone": "782164985", "email": "si@meanperson.com"},
    "mn": {"phone": "864351257", "email": "mn@coolpeep.com"},
}

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def starting_message():
    print("Welcome to the contact book")
    print("you can access the contacts using commands: add/search/delete")
    print("you can access the full contacts list use command: full_dir")
    print("to know your commands type help")
    print("you can quit the contacts using exit as command")

def help_commands():
    print("you can access the contacts using commands: add/search/delete")
    print("you can access the full contacts list use command: full_dir")
    print("you can quit the contacts using exit as command")

def check_end_program(value):
    if value == "exit":
        print("ending program")
        sys.exit()

def phone_owner(phone):
    """Return the name that owns this phone number, or None."""
    for name, details in contacts.items():
        if details["phone"] == phone:
            return name
    return None

def email_owner(email):
    """Return the name that owns this email, or None."""
    for name, details in contacts.items():
        if details["email"] == email:
            return name
    return None

# ---------- Field collectors: each loops on its own until valid input ----------
def get_name(must_exist=None):
    """
    must_exist=True  -> keep asking until name IS in contacts (for search/delete)
    must_exist=False -> keep asking until name is NOT in contacts (for add)
    must_exist=None  -> just return the first syntactically valid name
    """
    while True:
        name = input("Please enter name or 'exit' to exit the program: ").strip().lower()
        check_end_program(name)
        if not name.isalpha():
            print("Name must contain letters only. Try again.")
            continue
        exists = name in contacts
        if must_exist is True and not exists:
            print("No contact found with that name. Try again.")
            continue
        if must_exist is False and exists:
            print("That name already exists in the contact list. Try again.")
            continue
        return name

def get_phone():
    while True:
        phone = input("Please enter your phone number or 'exit' to exit the program: ").strip().lower()
        check_end_program(phone)
        if not (len(phone) == 9 and phone.isdigit()):
            print("Phone must be exactly 9 digits. Try again.")
            continue
        owner = phone_owner(phone)
        if owner is not None:
            print(f"That phone number is already used by {owner}. Try again.")
            continue
        return phone

def get_email():
    while True:
        email = input("Please enter your email ID or 'exit' to exit the program: ").strip().lower()
        check_end_program(email)
        if re.match(EMAIL_PATTERN, email) is None:
            print("That doesn't look like a valid email. Try again.")
            continue
        owner = email_owner(email)
        if owner is not None:
            print(f"That email is already used by {owner}. Try again.")
            continue
        return email

# ---------- Commands ----------
def add_contact():
    name = get_name(must_exist=False)
    phone = get_phone()
    email = get_email()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")
    print(f"name: {name}, Phone: {phone}, Email: {email}")

def search_contact():
    name = get_name(must_exist=True)
    details = contacts[name]
    print(f"name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def delete_contact():
    name = get_name(must_exist=True)
    permission = input(f"Delete '{name}'? (y/n): ").strip().lower()
    if permission == "y":
        contacts.pop(name)
        print(f"'{name}' has been deleted.")
    else:
        print("Deletion cancelled.")

def full_directory():
    if not contacts:
        print("Contact list is empty.")
        return
    print("Here is the full directory")
    for name, details in contacts.items():
        print(f"name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def main():
    while True:
        command = input("Please enter your command: ").strip().lower()
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
            case "full_dir":
                full_directory()
            case _:
                print("Please enter a valid command")

if __name__ == "__main__":
    starting_message()
    main()
