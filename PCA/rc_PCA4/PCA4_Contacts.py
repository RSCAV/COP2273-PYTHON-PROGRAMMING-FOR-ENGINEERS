from typing import list

def display(book: List[List[str]]) -> None:
    if not book:
        print("There are no contacts available!")
        return

    for i, contact in enumerate(book, start=1):
        print(f"{i}. {contact[0]}")


def add(book: List[List[str]]) -> None:
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    book.append([name, email, phone])
    print(f"{name} was added.")


def view(book: List[List[str]]) -> None:
    try:
        n = int(input("Number: "))
    except ValueError:
        print("Invalid contact number!")
        return

    if 1 <= n <= len(book):
        name, email, phone = book[n - 1]
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
    else:
        print("Invalid contact number!")


def remove(book: List[List[str]]) -> None:
    try:
        n = int(input("Number: "))
    except ValueError:
        print("Invalid contact number!")
        return

    if 1 <= n <= len(book):
        name = book[n - 1][0]
        del book[n - 1]
        print(f"{name} was removed.")
    else:
        print("Invalid contact number!")
