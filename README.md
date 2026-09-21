# Student Management System

A simple Python-based Student Management System for storing, searching, updating, and deleting student records.

This project helps manage student information such as name, age, marks, course, contact number, and email address, and also calculates a grade based on the marks obtained.

## Features

- Add new student records
- View all students in the system
- Search for a student by name
- Update student details
- Delete a student record
- Automatic grade calculation based on marks
- Simple console-based interface

## Grade System

The system assigns grades using the following rules:

- 90 and above: A+
- 80 to 89: A
- 70 to 79: B
- 60 to 69: C
- 50 to 59: D
- Below 50: F

## Project Files

- [Student_management_system.py](Student_management_system.py) - Main Python script

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the script:

```bash
python Student_management_system.py
```

## Example Workflow

When you run the program, it will prompt you to enter student information such as:

- Student name
- Age
- Marks
- Course
- Contact number
- Email ID

After that, it will display the student details and calculated grade.

You can also search for a student, update their details, or remove them from the records.

## Example Output

```text
Enter the Student name: John
Enter the age of the Student: 18
Enter the marks of the Student: 92
Enter the course of the student: Computer Science
Enter the contact no. of student: 9876543210
Enter the Email ID of student: john@example.com

===============STUDENT MANAGEMENT SYSTEM=======================

Name: John
Age: 18
Course: Computer Science
Marks: 92
Grade: A+
Contact No.: 9876543210
Email Id: john@example.com
```

## Future Improvements

- Add student ID support
- Store records in a database instead of memory
- Add menu-driven navigation for better usability
- Add file-based persistence using JSON or CSV
- Create a graphical user interface (GUI)

## License

This project is open for learning and educational purposes.

## Author

Created as a beginner-friendly Python project for student record management.
