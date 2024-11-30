import os

def show_options():
    print("\n--- Student Grade Tracker ---")
    print("1. Add a new grade")
    print("2. View grades list")
    print("3. Compute average score")
    print("4. Save grades to file")
    print("5. Load grades from file")
    print("6. Exit the system")

def enter_grade(grades):
    try:
        student = input("Enter student name: ")
        score = input(f"Enter the grade for {student}: ")
        score = float(score)
        grades[student] = score
        print(f"Grade for {student} has been recorded.")
    except ValueError:
        print("Oops! That's not a valid grade. Please enter a number.")
    except Exception as e:
        print(f"Something went wrong: {e}")

def display_grades(grades):
    if not grades:
        print("No grades have been entered yet.")
    else:
        print("\n--- List of All Grades ---")
        for student, grade in grades.items():
            print(f"{student}: {grade}")

def calculate_average_score(grades):
    try:
        if not grades:
            print("No grades available to compute an average.")
            return
        average = sum(grades.values()) / len(grades)
        print(f"The average grade is: {average:.2f}")
    except ZeroDivisionError:
        print("There are no grades to average.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def save_grades(grades, filename="student_grades.txt"):
    try:
        with open(filename, 'w') as file:
            for student, grade in grades.items():
                file.write(f"{student}: {grade}\n")
        print(f"Grades have been saved to {filename}.")
    except Exception as e:
        print(f"Could not save grades: {e}")

def load_grades(filename="student_grades.txt"):
    grades = {}
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
        with open(filename, 'r') as file:
            for line in file:
                try:
                    student, grade = line.strip().split(": ")
                    grades[student] = float(grade)
                except ValueError:
                    print(f"Skipping malformed line in file: {line.strip()}")
        print(f"Grades have been successfully loaded from {filename}.")
        return grades
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return grades

def run_program():
    grades = {}

    while True:
        show_options()
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            enter_grade(grades)
        elif choice == '2':
            display_grades(grades)
        elif choice == '3':
            calculate_average_score(grades)
        elif choice == '4':
            save_grades(grades)
        elif choice == '5':
            grades = load_grades()
        elif choice == '6':
            print("Goodbye! Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_program()
