def add_students():
    name = input('Enter the Student name: ')
    age = int(input('Enter the age of the Student: '))
    marks = int(input('Enter the marks of the Student: '))
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


students = []

while True:
    student = add_students()
    students.append(student)

    choice = input('\nAdd new Student detail...? (y/n): ').lower()

    if choice != 'y':
        break

print(f'\n===============STUDENT MANAGEMENT SYSTEM=======================')

for student in students:
    grade = grade_calculate(student['marks'])

    print(f'\nName: {student["name"]}')
    print(f'Age: {student["age"]}')
    print(f'Course: {student["course"]}')
    print(f'Marks: {student["marks"]}')
    print(f'Grade: {grade}')
    print(f'Contact No.: {student["contact"]}')
    print(f'Email Id: {student["email_id"]}')
    print('-'*40)

#FUNCTION FOR SEARCH STUDENT FROM STUDENTS

def search_student():
    print(f'\n\n=================SEARCH STUDENT==================')
    search_name = input("\nEnter the name of student you want to search: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            grade = grade_calculate(student['marks'])
            print("\n----------------Student Found----------------")
            print(f'Name: {student["name"]}')
            print(f'Age: {student["age"]}')
            print(f'Course: {student["course"]}')
            print(f'Marks: {student["marks"]}')
            print(f'Grade: {grade}')
            print(f'Contact No.: {student["contact"]}')
            print(f'Email Id: {student["email_id"]}')
            return

    print("\nStudent not found...")

search_student()

def update_student():
    print("\n\n===================UPDATE STUDENT DETAILS===================")
    student_name = input("\nEnter the name of student you want to update: ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            print("\nStudent found. Enter new details: ")

            update_details = {
                1 : 'name',
                2 : 'age',
                3 : 'marks',
                4 : 'course',
                5 : 'contact',
                6 : 'email_id'
            }

            choice = int(input("\nEnter the choice to update: "))

            if choice == 1:
                new_name = input("Enter the new name of student: ")
                student['name'] = new_name
            elif choice == 2:
                new_age = int(input("Enter the new age of student: "))
                student['age'] = new_age
            elif choice == 3:
                new_marks = int(input("Enter the new marks of the student: "))
                student['marks'] = new_marks
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
                
            grade = grade_calculate(student['marks'])
            print(f'Updated Name: {student["name"]}')
            print(f'Updated Age: {student["age"]}')
            print(f'Updated Course: {student["course"]}')
            print(f'Updated Marks: {student["marks"]}')
            print(f'Updated Grade: {grade}')
            print(f'Updated Contact No.: {student["contact"]}')
            print(f'Updated Email Id: {student["email_id"]}')
            return

    print("\nstudent not found")
update_student()

def delete_student():
    print("\n\n===================DELETE STUDENT DETAILS===================")
    student_name = input("\nEnter the name of student you want to delete: ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            students.remove(student)
            print(f"\nStudent {student_name} has been deleted successfully.")
            return

    print("\nStudent not found.")

delete_student()