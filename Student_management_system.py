#===========================================================================================================

#                                       STUDENT MANAGEMENT SYSTEM

#===========================================================================================================

import json

subjects = [
    "Hindi",
    "English",
    "Maths",
    "Science",
    "Social Studies",
    "Physical Education"
]

def save_students():
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)

    print("\nStudent data saved successfully...👍")

def get_valid_number(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value
            else:
                print(
                    f"Invalid value. Please enter a number "
                    f"between {minimum} and {maximum}."
                )

        except ValueError:
            print("Invalid input. Please enter a valid number...❌")


def add_students():
    name = input('Enter the Student name: ')
    age = get_valid_number('Enter the age of the Student: ', 5, 100)
    marks = {}

    for subject in subjects:
        marks[subject] = get_valid_number(f'Enter the marks of {subject}: ', 0, 100)

    course = input('Enter the course of the student: ')
    contact = input('Enter the contact no. of student: ')
    email_id = input('Enter the Email ID of student: ')
    total_marks = sum(marks.values())
    percentage = (total_marks / (len(subjects) * 100)) * 100
    grade = grade_calculate(percentage)

    student = {
        'name': name,
        'age': age,
        'marks': marks,
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade,
        'course': course,
        'contact': contact,
        'email_id': email_id
    }

    return student

def grade_calculate(marks):

    if marks >= 90:
        return 'A+'

    elif marks >= 80:
        return 'A'

    elif marks  >= 70:
        return 'B'

    elif marks >= 60:
        return 'C'

    elif marks >= 50:
        return 'D'

    else:
        return 'F'


#FUNCTION FOR SEARCH STUDENT FROM STUDENTS

def search_student():
    print(f'\n=================SEARCH STUDENT==================')
    search_name = input("\nEnter the name of student you want to search: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found...☑️")
            display_student(student)            
            return

    print("\nStudent not found...❌")



def update_student():

    print("\n===================UPDATE STUDENT DETAILS===================")

    student_name = input(
        "\nEnter the name of student you want to update: "
    )

    for student in students:

        if student["name"].lower() == student_name.lower():

            print("\nStudent found. Enter new details: 👇")

            while True:

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Subject Marks")
                print("4. Update Course")
                print("5. Update Contact")
                print("6. Update Email")

                choice = get_valid_number("\nEnter your choice: ", 1, 6)

                if choice == 1:
                    new_name = input("\nEnter new name: ")
                    student["name"] = new_name
                    print("\nName updated successfully...☑️")

                elif choice == 2:
                    new_age = get_valid_number("\nEnter new age: ", 0, 150)
                    student["age"] = new_age
                    print("\nAge updated successfully...☑️")

                elif choice == 3:

                    # YOUR SUBJECT CODE HERE

                    for index, subject_name in enumerate(subjects, start=1):
                        print(f"{index}. {subject_name}")

                    subject_choice = get_valid_number("\nEnter the subject number: ", 1, len(subjects))

                    subject_name = subjects[subject_choice - 1]

                    new_marks = get_valid_number(f"\nEnter new marks for {subject_name}: ", 0, 100)

                    student["marks"][subject_name] = new_marks

                    total_marks = sum(student["marks"].values())

                    percentage = (total_marks /(len(subjects) * 100)) * 100

                    student["total_marks"] = total_marks
                    student["percentage"] = percentage
                    student["grade"] = grade_calculate(percentage)

                    print(f"\n{subject_name} marks updated successfully...☑️")

                elif choice == 4:
                    new_course = input("Enter new course: ")
                    student["course"] = new_course
                    print("\nCourse updated successfully...☑️")

                elif choice == 5:
                    new_contact = input("Enter new contact number: ")
                    student["contact"] = new_contact
                    print("\nContact updated successfully...☑️")

                elif choice == 6:
                    new_email = input("Enter new email ID: ")
                    student["email_id"] = new_email
                    print("\nEmail ID updated successfully...☑️")

                again_choice = input("\nDo you want to update another detail? (y/n): ").lower()

                if again_choice != "y":
                    break

            display_student(student)
            return

    print("\nStudent not found...❌")

def delete_student():
    print("\n===================DELETE STUDENT DETAILS===================")
    student_name = input("\nEnter the name of student you want to delete: ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            students.remove(student)
            print(f"\nStudent {student_name} has been deleted successfully...☑️")
            return

    print("\nStudent not found...❌")

def display_student(student):

    print(f'Name: {student["name"]}')
    print(f'Age: {student["age"]}')
    print(f'Course: {student["course"]}')
    print("\n-------------- MARKS ----------------")

    for subject, marks in student["marks"].items():
        print(f"{subject:<20}: {marks}")

    print("--------------------------------------")
    print(f"Total      : {student['total_marks']} / {len(subjects) * 100}")
    print(f"Percentage : {student['percentage']:.2f}%")
    print(f"Grade      : {student['grade']}")
    
    print(f'Contact No.: {student["contact"]}')
    print(f'Email Id: {student["email_id"]}')
    print("-" * 40)

def load_students():
    try:
        with open("student.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

students = load_students()

while True:
    print("\n======================================================================")
    print("\n                    STUDENT MANAGEMENT SYSTEM")
    print("\n======================================================================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")

    
    choice = get_valid_number("\nEnter your choice: ", 1, 6)

    if choice == 1:
        student = add_students()
        students.append(student)
        save_students()
        print("\nStudent added successfully...☑️")

    elif choice == 2:
        search_student()
    
    elif choice == 3:
        update_student()
        save_students()

    elif choice == 4:
        delete_student()
        save_students()

    elif choice == 5:

        if not students:
            print("\nNo students found...❌")

        else:
            print("\n================ ALL STUDENTS ================")

            for student in students:
                display_student(student)

    elif choice == 6:
        print("\nExiting the program...")
        break

    else:
        print("\nInvalid choice. Please try again...❌")

