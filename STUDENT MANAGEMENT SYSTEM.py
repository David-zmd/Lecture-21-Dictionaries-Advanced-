students = {}
def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def validate_mark():
    while True:
        mark = int(input("Enter mark (0-100): "))
        if 0 <= mark <= 100:
            return mark
        print("Invalid mark! Try again.")


def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student already exists!")
        return

    name = input("Enter Full Name: ")
    class_name = input("Enter Class: ")

    subjects = {}
    print("Enter at least 3 subjects:")
    for i in range(3):
        subject = input(f"Subject {i+1} name: ")
        mark = validate_mark()
        subjects[subject] = mark

    students[student_id] = {
        "name": name,
        "class": class_name,
        "subjects": subjects
    }
    print("Student added successfully!")

def view_all_students():
    if not students:
        print("No students available.")
        return

    print("\nStudent List:")
    for sid, data in students.items():
        print(f"{sid} - {data['name']}")

def view_student_report():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]
    subjects = student["subjects"]

    total = sum(subjects.values())
    avg = total / len(subjects)
    grade = calculate_grade(avg)

    print("\n--- Student Report ---")
    print(f"Name: {student['name']}")
    print(f"Class: {student['class']}")
    print("Subjects & Marks:")
    for sub, mark in subjects.items():
        print(f"{sub}: {mark}")

    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

def update_marks():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print("Student not found!")
        return

    subject = input("Enter subject name to update: ")
    if subject not in students[student_id]["subjects"]:
        print("Subject not found!")
        return

    new_mark = validate_mark()
    students[student_id]["subjects"][subject] = new_mark
    print("Marks updated successfully!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def rank_students():
    if not students:
        print("No students available.")
        return

    averages = []
    for sid, data in students.items():
        avg = sum(data["subjects"].values()) / len(data["subjects"])
        averages.append((avg, data["name"]))

    averages.sort(reverse=True)

    print("\nStudent Rankings:")
    for rank, (avg, name) in enumerate(averages, 1):
        print(f"{rank}. {name} - Average: {avg:.2f}")

def top_student():
    if not students:
        print("No students available.")
        return

    top = max(
        students.items(),
        key=lambda x: sum(x[1]["subjects"].values()) / len(x[1]["subjects"])
    )

    avg = sum(top[1]["subjects"].values()) / len(top[1]["subjects"])
    print(f"Top Student: {top[1]['name']} (Average: {avg:.2f})")

def subject_averages():
    subject_totals = {}
    subject_counts = {}

    for data in students.values():
        for subject, mark in data["subjects"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + mark
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    print("\nSubject-wise Averages:")
    for subject in subject_totals:
        avg = subject_totals[subject] / subject_counts[subject]
        print(f"{subject}: {avg:.2f}")


def menu():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Report")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Rank Students")
        print("7. Top Student")
        print("8. Subject-wise Averages")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            rank_students()
        elif choice == "7":
            top_student()
        elif choice == "8":
            subject_averages()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()
