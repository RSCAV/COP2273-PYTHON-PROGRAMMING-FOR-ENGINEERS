# File: contacts.py
# Description: This module contains functions (display(), add(), view(), remove()) for managing contacts
# By: Rocco Meyerholtz (writer), Rodrigo Casanova (observer)

from typing import List

# Define function that displays all contacts in the list
def display(contacts: List[List[str]]) -> None:
    if not contacts: # Check if the contact list is empty
        print("There are no contacts available!")
    else:
        # Loop through contacts with index startin at 1
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact[0]}") # Print index and contact's name only

# Define function that prompts user for new contact info and adds to the list
def add(contacts: List[List[str]]) -> None:
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone]) # Add as a sublist [name, email, phone]
    print(f"{name} was added.") # Confirm addition

# Define function that prompts user for a contact number and displays that contact
def view(contacts: List[List[str]]) -> None:
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(contacts):
            contact = contacts[number - 1]
            print(f"Name: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone: {contact[2]}")
        else:
            print("Invalid contact number!")
    except ValueError: # If user types something not an integer
        print("Invalid contact number!")

# Define function that prompts user for a contact number and removes that contact
def remove(contacts: List[List[str]]) -> None:
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(contacts): # Validate number is in range
            removed = contacts.pop(number - 1) # Remove that contact
            print(f"{removed[0]} was removed.")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Invalid contact number!")
