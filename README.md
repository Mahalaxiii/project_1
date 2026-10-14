Project 1 — Student Management System
##What the project does
The Student Management System is an object-oriented Python console application designed to efficiently manage student records. It seamlessly integrates with the student_records_100.csv data file to ensure permanent storage and easy retrieval of student details.

##How the Project Works
Data Initialization: Upon starting, the application reads the linked CSV file (student_records_100.csv) using the pandas library, converting rows into structured Student object instances stored inside a central StudentManager dictionary.

Interactive Menu: The program runs a continuous loop presenting a 7-option console menu. Users select options by typing numbers (1 through 7).

Persistent Operations: Any modifications (adding, updating, or deleting students) instantly update internal data structures and rewrite changes back to the CSV file.

Error & Exception Handling: Input prompts are safeguarded with try-except blocks to handle invalid numeric inputs or file errors gracefully without crashing.

##How to Run the Project
Prerequisites
Ensure you have Python 3.x and the pandas library installed. If pandas is missing, install it via your terminal:

Bash
pip install pandas
Execution Steps
Place the Python script (student_management_csv.py) and the data file (student_records_100.csv) in the same directory.

Open your terminal or command prompt in that folder.

Run the script using the following command:

Bash
python student_management_csv.py
Follow the interactive console instructions.

##The Classes Used
Person (Abstract Base Class):

Utilizes Python's abc module.

Defines a common blueprint with an abstract method display_details() to enforce inheritance standards.

Student (Subclass):

Inherits from Person.

Encapsulates private attributes (__student_id, __marks) and provides secure getter/setter methods.

Includes helper methods to compute individual student averages.

StudentManager (Controller Class):

Manages the collection of all student records.

Handles file input/output operations (load_from_csv and save_to_csv).

Implements core CRUD features and class-level summary statistics.

##Main Features Implemented
Add Student: Register a new student profile with a unique ID, name, and marks.

Display Students: List current student records alongside calculated averages.

Search Student: Look up a student instantly using their unique Student ID.

Update Student Records: Modify student names or scores dynamically.

Delete Student: Remove student records permanently from the system and file.

Calculate Class Average: Compute and display the overall average score across all students.

File Handling & Exception Control: Robust CSV reading/writing with input validation for marks and menu selections.