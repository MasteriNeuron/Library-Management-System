from abc import ABC, abstractmethod
from datetime import datetime

# Base class for Library Items
class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_available = True

    @abstractmethod
    def display_info(self):
        pass

# Subclass for Book
class Book(LibraryItem):
    def __init__(self, title, author, item_id, isbn):
        super().__init__(title, author, item_id)
        self.isbn = isbn

    def display_info(self):
        return f"Book - Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

# Subclass for Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine - Title: {self.title}, Author: {self.author}, Issue: {self.issue_number}, Available: {self.is_available}"

# User class
class User:
    def __init__(self, name, user_id, is_member):
        self.name = name
        self.user_id = user_id
        self.is_member = is_member
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.is_available:
            item.is_available = False
            self.borrowed_items.append(item)
            return f"{self.name} borrowed {item.title}."
        return f"{item.title} is not available."

    def return_item(self, item):
        if item in self.borrowed_items:
            item.is_available = True
            self.borrowed_items.remove(item)
            return f"{self.name} returned {item.title}."
        return f"{self.name} did not borrow {item.title}."

# Decorators for logging and validation
def log_action(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_message = f"{datetime.now()} - {action}: {result}"
            with open("library.log", "a") as log_file:
                log_file.write(log_message + "\n")
            print(log_message)  # Optional: Print log to console
            return result
        return wrapper
    return decorator

def membership_required(func):
    def wrapper(*args, **kwargs):
        # The second argument is the user when the method is bound to a class
        user = args[1]
        if not isinstance(user, User) or not user.is_member:
            return "Action denied. Membership required."
        return func(*args, **kwargs)
    return wrapper

# Library class
class Library:
    def __init__(self):
        self.items = []
        self.members = []

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, user):
        self.members.append(user)

    def search_items(self, **criteria):
        results = self.items
        for key, value in criteria.items():
            value_lower = value.lower()
            results = [
                item for item in results
                if getattr(item, key, None) and value_lower in getattr(item, key, "").lower()
            ]
        return results


    def display_items(self):
        if not self.items:
            return "No items available in the library."
        return [item.display_info() for item in self.items]

    @membership_required
    @log_action("Borrow")
    def borrow_item(self, user, item_id):
        item = next((i for i in self.items if i.item_id == item_id), None)
        if item:
            return user.borrow_item(item)
        return "Item not found."

    @membership_required
    @log_action("Return")
    def return_item(self, user, item_id):
        item = next((i for i in self.items if i.item_id == item_id), None)
        if item:
            return user.return_item(item)
        return "Item not found."

# CLI-based interaction for user-friendliness
def main():
    library = Library()

    # Predefined items and members
    library.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", 1, "9780743273565"))
    library.add_item(Magazine("National Geographic", "Various", 2, "2023-05"))

    # Adding books by Chetan Bhagat
    library.add_item(Book("Five Point Someone", "Chetan Bhagat", 3, "9788129115300"))
    library.add_item(Book("2 States", "Chetan Bhagat", 4, "9788129115301"))
    library.add_item(Book("The 3 Mistakes of My Life", "Chetan Bhagat", 5, "9788129115233"))
    library.add_item(Book("One Night @ the Call Center", "Chetan Bhagat", 6, "9788129117206"))

    # Adding books by Dr. A.P.J. Abdul Kalam
    library.add_item(Book("Wings of Fire", "Dr. A.P.J. Abdul Kalam", 7, "9788173711466"))
    library.add_item(Book("Ignited Minds", "Dr. A.P.J. Abdul Kalam", 8, "9780143424123"))
    library.add_item(Book("India 2020", "Dr. A.P.J. Abdul Kalam", 9, "9780143423683"))
    library.add_item(Book("My Journey: Transforming Dreams into Actions", "Dr. A.P.J. Abdul Kalam", 10, "9788129124914"))

    # Adding other famous Indian books
    library.add_item(Book("The God of Small Things", "Arundhati Roy", 11, "9788172234980"))
    library.add_item(Book("Midnight's Children", "Salman Rushdie", 12, "9780099578512"))
    library.add_item(Book("Train to Pakistan", "Khushwant Singh", 13, "9780143065883"))
    library.add_item(Book("The White Tiger", "Aravind Adiga", 14, "9781416562603"))

    # Adding famous magazines during independence
    library.add_item(Magazine("Harijan", "Mahatma Gandhi", 15, "1947-01"))
    library.add_item(Magazine("The Modern Review", "Ramananda Chatterjee", 16, "1947-02"))
    library.add_item(Magazine("Young India", "Mahatma Gandhi", 17, "1947-03"))
    library.add_item(Magazine("The Pioneer", "George Allen", 18, "1947-04"))

    library.add_member(User("Shubham", 101, True))
    library.add_member(User("Naina", 102, True))
    library.add_member(User("Abhishek", 103, False))
    library.add_member(User("Ashu", 104, False))

    while True:
        print("<====================================================================================>")
        print("\nLibrary Management System")
        print("1. Display all items")
        print("2. Search items")
        print("3. Borrow an item")
        print("4. Return an item")
        print("5. Exit")
        print("<====================================================================================>") 
        choice = input("Enter your choice: ")

        if choice == "1":
            items = library.display_items()
            if isinstance(items, str):
                print(items)
            else:
                for item in items:
                    print(item)

        elif choice == "2":
            search_key = input("Search by (title/author): ").strip().lower()
            search_value = input(f"Enter {search_key}: ").strip()
            results = library.search_items(**{search_key: search_value})
            if results:
                for item in results:
                    print(item.display_info())
            else:
                print("No items found.")

        elif choice == "3":
            user_id = int(input("Enter your user ID: "))
            item_id = int(input("Enter item ID to borrow: "))
            user = next((u for u in library.members if u.user_id == user_id), None)
            if user:
                print(library.borrow_item(user, item_id))
            else:
                print("User not found.")

        elif choice == "4":
            user_id = int(input("Enter your user ID: "))
            item_id = int(input("Enter item ID to return: "))
            user = next((u for u in library.members if u.user_id == user_id), None)
            if user:
                print(library.return_item(user, item_id))
            else:
                print("User not found.")

        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
