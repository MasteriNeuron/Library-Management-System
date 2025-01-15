# Library Management System
![image](https://github.com/user-attachments/assets/14013e23-c9e8-46d0-818e-985a6d976dec)

## Project Overview
The **Library Management System** is a non-UI-based software solution designed to manage library operations programmatically. Built using Python, it leverages core Object-Oriented Programming System (OOPS) principles to provide a robust, modular, and scalable platform for handling library items, members, and transactions.

## Key Features
1. **Add Library Items**
   - Librarians can add items like books and magazines.

2. **Borrow and Return Items**
   - Members can borrow and return available items, subject to membership validation.

3. **Membership Management**
   - Validates membership before allowing borrowing.

4. **Search and Display Items**
   - Search for items by title, author, or type.
   - View all available items in the library.

5. **Logging and Reporting**
   - Maintains logs for borrowing and returning actions.

## User Roles
1. **Librarian**
   - Add, view, and manage library items.
   - View logs of borrowing and returning actions.

2. **Member**
   - Search for library items.
   - Borrow and return items.

3. **Visitor**
   - Search for items but cannot borrow or return.

## Technical Features
- **Object-Oriented Design:**
  - Encapsulation, inheritance, polymorphism, and abstraction for a modular and reusable structure.
- **Dunder (Magic) Methods:**
  - `__str__`, `__getitem__`, and `__eq__` to enhance object interactions.
- **Decorators:**
  - Logging actions and validating membership dynamically.
- **Property Decorators:**
  - Read-only computed attributes for items.

## Project Structure
### Classes and Relationships
- **LibraryItem (Base Class):**
  - Encapsulates shared attributes and methods for library items.
- **Book and Magazine (Subclasses):**
  - Inherit from `LibraryItem` to handle specific item types.
- **User:**
  - Manages members and their privileges.
- **Library:**
  - Handles library operations like adding items, borrowing, and returning.

### Workflow
1. **Initialization:**
   - Prepopulate the library with predefined items (books and magazines).
   - Add members with membership statuses.
2. **Add Items:**
   - Use `add_item()` to programmatically add new items.
3. **Search Items:**
   - Search by attributes like title or author.
4. **Borrow and Return:**
   - Validate membership before borrowing.
   - Log all borrowing and returning actions.
5. **Logs and Reporting:**
   - View borrowing and returning logs for auditing.

## Setup and Usage
### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MasteriNeuron/Library-Management-System.git
   cd library-management-system
   ```
2. Ensure Python dependencies are installed (if any).

### Running the Application
1. Open a terminal and navigate to the project directory.
2. Run the Python script:
   ```bash
   python library_management_system.py
   ```
3. Follow the CLI prompts to interact with the system:
   - **Display all items**
   - **Search for items**
   - **Borrow an item**
   - **Return an item**
   - **Exit the system**

### Sample Commands
1. **Display All Items:**
   - Choose option `1` from the menu.
2. **Search Items:**
   - Choose option `2` and specify the search criteria (e.g., title or author).
3. **Borrow Items:**
   - Choose option `3`, enter user ID and item ID.
4. **Return Items:**
   - Choose option `4`, enter user ID and item ID.
5. **Exit:**
   - Choose option `5`.

### Sample Output
Here is an example interaction with the system:

```plaintext
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 1
Book - Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 9780743273565, Available: True
Magazine - Title: National Geographic, Author: Various, Issue: 2023-05, Available: True
Book - Title: Five Point Someone, Author: Chetan Bhagat, ISBN: 9788129115300, Available: True
Book - Title: 2 States, Author: Chetan Bhagat, ISBN: 9788129115301, Available: True
Book - Title: The 3 Mistakes of My Life, Author: Chetan Bhagat, ISBN: 9788129115233, Available: True
Book - Title: One Night @ the Call Center, Author: Chetan Bhagat, ISBN: 9788129117206, Available: True
Book - Title: Wings of Fire, Author: Dr. A.P.J. Abdul Kalam, ISBN: 9788173711466, Available: True
Book - Title: Ignited Minds, Author: Dr. A.P.J. Abdul Kalam, ISBN: 9780143424123, Available: True
Book - Title: India 2020, Author: Dr. A.P.J. Abdul Kalam, ISBN: 9780143423683, Available: True
Book - Title: My Journey: Transforming Dreams into Actions, Author: Dr. A.P.J. Abdul Kalam, ISBN: 9788129124914, Available: True
Book - Title: The God of Small Things, Author: Arundhati Roy, ISBN: 9788172234980, Available: True
Book - Title: Midnight's Children, Author: Salman Rushdie, ISBN: 9780099578512, Available: True
Book - Title: Train to Pakistan, Author: Khushwant Singh, ISBN: 9780143065883, Available: True
Book - Title: The White Tiger, Author: Aravind Adiga, ISBN: 9781416562603, Available: True
Magazine - Title: Harijan, Author: Mahatma Gandhi, Issue: 1947-01, Available: True
Magazine - Title: The Modern Review, Author: Ramananda Chatterjee, Issue: 1947-02, Available: True
Magazine - Title: Young India, Author: Mahatma Gandhi, Issue: 1947-03, Available: True
Magazine - Title: The Pioneer, Author: George Allen, Issue: 1947-04, Available: True
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 2
Search by (title/author): author
Enter author: Khushwant Singh
Book - Title: Train to Pakistan, Author: Khushwant Singh, ISBN: 9780143065883, Available: True
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 3
Enter your user ID: 102
Enter item ID to borrow: 13
2025-01-15 11:45:30.238505 - Borrow: Naina borrowed Train to Pakistan.
Naina borrowed Train to Pakistan.
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 3
Enter your user ID: 101
Enter item ID to borrow: 11
2025-01-15 11:45:53.490194 - Borrow: Shubham borrowed The God of Small Things.
Shubham borrowed The God of Small Things.
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 3
Enter your user ID: 103
Enter item ID to borrow: 14
Action denied. Membership required.
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 3
Enter your user ID: 102
Enter item ID to borrow: 11
2025-01-15 11:47:33.904193 - Borrow: The God of Small Things is not available.
The God of Small Things is not available.
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 4
Enter your user ID: 101
Enter item ID to return: 11
2025-01-15 11:47:54.114846 - Return: Shubham returned The God of Small Things.
Shubham returned The God of Small Things.
<====================================================================================>

Library Management System
1. Display all items
2. Search items
3. Borrow an item
4. Return an item
5. Exit
<====================================================================================>
Enter your choice: 5
Exiting Library Management System. Goodbye!
```

## Logging
- All borrowing and returning actions are logged with timestamps in `library.log`.
- Example log entry:
  ```
   2025-01-15 11:45:30.238505 - Borrow: Naina borrowed Train to Pakistan.
   2025-01-15 11:45:53.490194 - Borrow: Shubham borrowed The God of Small Things.
   2025-01-15 11:47:33.904193 - Borrow: The God of Small Things is not available.
   2025-01-15 11:47:54.114846 - Return: Shubham returned The God of Small Things.


  ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!

