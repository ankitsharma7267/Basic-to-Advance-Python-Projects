#===========================================================================================================

#                                       STUDENT MANAGEMENT SYSTEM

#===========================================================================================================



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
            print("Invalid input. Please enter a valid number.")


def add_students():
    name = input('Enter the Student name: ')
    age = get_valid_number('Enter the age of the Student: ', 5, 100)
    marks = get_valid_number('Enter the marks of the Student: ', 0, 100)
    course = input('Enter the course of the student: ')
    contact = input('Enter the contact no. of student: ')
    email_id = input('Enter the Email ID of student: ')

    student = {
        'name': name,
        'age': age,
        'marks': marks,
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
    elif marks >= 70:
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
            print("\nStudent Found...")
            display_student(student)            
            return

    print("\nStudent not found...")



def update_student():
    print("\n===================UPDATE STUDENT DETAILS===================")
    student_name = input("\nEnter the name of student you want to update: ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            print("\nStudent found. Enter new details: ")

            while True:

                choice = get_valid_number("Enter your choice: ", 1, 6)

                if choice == 1:
                    new_name = input("Enter the new name of student: ")
                    student['name'] = new_name
                elif choice == 2:
                    student['age'] = get_valid_number("Enter the new age of student: ", 5, 100)

                elif choice == 3:
                    student['marks'] = get_valid_number("Enter the new marks of the student: ", 0, 100)
                    
                elif choice == 4:
                    new_course = input("Enter the new course of the student: ")
                    student['course'] = new_course
                elif choice == 5:
                    new_contact = input("Enter the new contact detail of student: ")
                    student['contact'] = new_contact
                elif choice == 6:
                    new_email_id = input("Enter the new Email ID of the student: ")
                    student['email_id'] = new_email_id
                else:
                    print("Invalid choice")
                    continue

                again_choice = input("\nDo you want to update another detail? (y/n): ").lower()
                if again_choice != 'y':
                    break
                
            display_student(student)
            return
    print("\nStudent not found.")

def delete_student():
    print("\n===================DELETE STUDENT DETAILS===================")
    student_name = input("\nEnter the name of student you want to delete: ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            students.remove(student)
            print(f"\nStudent {student_name} has been deleted successfully.")
            return

    print("\nStudent not found.")

def display_student(student):
    grade = grade_calculate(student["marks"])

    print(f'Name: {student["name"]}')
    print(f'Age: {student["age"]}')
    print(f'Course: {student["course"]}')
    print(f'Marks: {student["marks"]}')
    print(f'Grade: {grade}')
    print(f'Contact No.: {student["contact"]}')
    print(f'Email Id: {student["email_id"]}')
    print("-" * 40)

students = []

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
        print("\nStudent added successfully!")

    elif choice == 2:
        search_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        if not students:
            print("\nNo students found.")
        else:
            print("\n================ ALL STUDENTS ================")
            for student in students:
                display_student(student)

    elif choice == 6:
        print("\nExiting the program...")
        break

    else:
        print("\nInvalid choice. Please try again.")

