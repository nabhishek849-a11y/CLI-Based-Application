# CLI Based Application

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    
    student = {
        "name": name,
        "roll": roll,
        "course": course
    }
    
    students.append(student)
    print("\n Student added successfully!\n")

# Function to view students
def view_students():
    if not students:
        print("\n No students found.\n")
        return
    
    print("\n Student List:")
    print("-" * 40)
    
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name   : {student['name']}")
        print(f"   Roll   : {student['roll']}")
        print(f"   Course : {student['course']}")
        print("-" * 40)

# Function to delete student
def delete_student():
    view_students()
    
    if not students:
        return
    
    try:
        index = int(input("Enter student number to delete: "))
        if 1 <= index <= len(students):
            removed = students.pop(index - 1)
            print(f"\n {removed['name']} deleted successfully!\n")
        else:
            print("\n Invalid number!\n")
    except ValueError:
        print("\n Please enter a valid number!\n")

# Main menu loop
def main():
    while True:
        print("\n====== Student Manager ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("\n Exiting... Thank you!\n")
            break
        else:
            print("\n Invalid choice! Try again.\n")

# Run program
main()