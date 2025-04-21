# School-System

# Simple School Management System in Python

This is a basic project in Python that implements a simple school management system. It allows managing information about students, teachers, subjects, classes, and enrollments through an interactive terminal menu.

## Main Features:

* **Main Menu:** Offers options to access the management of different school entities.
* **Generic List Management:** A `gerenciar_lista` function is used to perform CRUD (Create, Read, Update, Delete) operations on lists of dictionaries, representing students, teachers, subjects, classes, and enrollments.
* **Include:** Adds a new item (student, teacher, etc.) to the corresponding list, prompting for relevant information such as registration number, name, CPF (Brazilian national ID), and class for students.
* **List:** Displays all items present in the selected list, showing their details.
* **Update:** Allows modifying the details of an existing item in the list, searching for it by registration number (in the case of students).
* **Delete:** Removes an item from the list, requesting confirmation before deletion (searches by registration number for students).
* **Data Structure:** Uses a Python list (`lista`) to store data as dictionaries.

## How to Run:

1.  Make sure you have Python installed on your system.
2.  Save the code in a file with the `.py` extension (for example, `school_management.py`).
3.  Open your terminal or command prompt, navigate to the directory where you saved the file.
4.  Run the script using the command: `python school_management.py`
5.  Follow the instructions in the interactive menu to manage the information.

## Notes:

* The `gerenciar_lista` function is generic and could be enhanced to handle specific attributes for each entity (students, teachers, etc.).
* Error handling is basic and can be expanded for greater robustness.
