import json
print("=" * 50)
print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
print("=" * 50)
# Load students from file
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except:
        return []

# Save students to file
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student["ID"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")

# View students
def view_students():
    students = load_students()

    if len(students) == 0:
        print("No student records found.")

    else:
        print("\n===== STUDENT RECORDS =====")

        for student in students:
            print("=" * 35)
            print(f"Student ID : {student['ID']}")
            print(f"Name       : {student['Name']}")
            print(f"Age        : {student['Age']}")
            print(f"Course     : {student['Course']}")
            print("=" * 35)

# Update student
def update_student():
    students = load_students()

    student_id = input("Enter Student ID to update: ")

    found = False

    for student in students:
        if student["ID"] == student_id:
            print("\nStudent Found!")

            student["Name"] = input("Enter new Name: ")
            student["Age"] = input("Enter new Age: ")
            student["Course"] = input("Enter new Course: ")

            save_students(students)

            print("Student updated successfully!")
            found = True
            break

    if not found:
        print("Student ID not found.")

# Delete student
def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to delete: ")

    found = False

    for student in students:
        if student["ID"] == student_id:
            students.remove(student)

            save_students(students)

            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("Student ID not found.")
# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()
    
    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("Feature coming next...")