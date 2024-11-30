# In this program we first need to press 1 to add the name of the students and grade simultaneously after that we can move on to the furthur options like enter 2 to view all the grades of the students the rest given in the output

# We have enahnced the readability of the program here from the third question

# Module for Grade Management

# Function to display the menu
def display_menu():
    print("\nGrade Management System")
    print("1. Add Student Grades")
    print("2. View All Student Grades")
    print("3. Calculate Average Grade")
    print("4. Determine Pass/Fail")
    print("5. Exit")

# Function to add student grades
def add_grades(grades):
    student_name = input("Enter student name: ")
    grade = float(input(f"Enter grade for {student_name}: "))
    grades[student_name] = grade
    print(f"Grade for {student_name} added successfully.")

# Function to view all student grades
def view_grades(grades):
    if not grades:
        print("No grades available.")
    else:
        print("\nStudent Grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")

# Function to calculate the average grade
def calculate_average(grades):
    if not grades:
        print("No grades available to calculate the average.")
    else:
        avg_grade = sum(grades.values()) / len(grades)
        print(f"The average grade of all students is: {avg_grade:.2f}")

# Function to determine pass/fail for students
def determine_pass_fail(grades, passing_grade=50):
    if not grades:
        print("No grades available to determine pass/fail status.")
    else:
        print("\nPass/Fail Status:")
        for student, grade in grades.items():
            status = "Pass" if grade >= passing_grade else "Fail"
            print(f"{student}: {status} (Grade: {grade})")

# Main function to run the application
def main():
    grades = {}  # Dictionary to store student names and their grades
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_grades(grades)
        elif choice == '2':
            view_grades(grades)
        elif choice == '3':
            calculate_average(grades)
        elif choice == '4':
            determine_pass_fail(grades)
        elif choice == '5':
            print("Exiting the Grade Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Start the program
if __name__ == "__main__":
    main()
