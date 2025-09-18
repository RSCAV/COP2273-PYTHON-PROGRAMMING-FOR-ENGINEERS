# File: rc_PCA4.py
# Description: This program manages contacts using the contacts module
# Input(s): User commands and contact information (name, email, phone)
# Output(s): Displayed contact list, messages confirming add/view/remove actions
# By: Rocco Meyerholtz (Writer), Rodrigo Casanova (Observer)
#
# Three things I learned:
# 1. How to work with lists of lists to store data/Users/rodrigocasanovaaleman/Downloads/contacts.py
# 2. How to use enumerate() to number items in a list starting from 1 instead of 0.
# 3. How to validate user input with try/except and handle ValueError.
# 4. How pop() removes and returns an item from a list.

import contacts

# Define function that displays a title string
def display_title(title: str) -> None:
    print()
    print(f"Contact Manager: {title}")

# Define function that displays available commands from a tuple
def display_menu(menu: tuple) -> None:
    print("\nCOMMAND MENU")
    for item in menu: # Loop through each item in tuple
        print(item)

# Define main() function
def main():
    contacts_list = [] # Initialize empty list that stores all contacts
    # Define available menu commands as tuple of strings
    menu = (
        "display - Display all contacts",
        "view    - View a contact",
        "add     - Add a contact",
        "remove  - Remove a contact",
        "exit    - Exit program"
    )

    display_title("Publisher")
    display_menu(menu)

    # Start infinite loop to keep prompting user until exit 
    while True:
        command = input("\nCommand: ").strip()
        if command == "display":
            contacts.display(contacts_list) # Call display() in contacts module
        elif command == "add":
            contacts.add(contacts_list) # Call add() in contacts module
        elif command == "view":
            contacts.view(contacts_list) # Call view() in contacts module
        elif command == "remove":
            contacts.remove(contacts_list) # Call remove() in contacts module
        elif command == "exit":
            print()
            print("Thank you for using the program. Goodbye!")
            break # Break loop to end program
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
