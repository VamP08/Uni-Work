def display_marksheet(students, roll_no):
    found_student = next((s for s in students if s["roll_no"] == roll_no), None)

    if found_student:
        name = found_student["name"]
        roll_no = found_student["roll_no"]
        marks = found_student["marks"]
        average_marks = sum(marks) / len(marks)

        print(f"Name: {name}, Roll No: {roll_no}")
        print("Marks:")
        for mark in marks:
            print(mark, end=" ")
        print("\n")

        grade = None
        if 90 <= average_marks <= 100:
            grade = "A+"
        elif 80 <= average_marks < 90:
            grade = "A"
        elif 70 <= average_marks < 80:
            grade = "B"
        elif 60 <= average_marks < 70:
            grade = "C"
        elif 50 <= average_marks < 60:
            grade = "D"
        else:
            grade = "F"

        print(f"Grade: {grade}")
    else:
        print("No student found with the given roll number.")

students = [
    {"roll_no": 1, "name": "Garv", "marks": [80, 70, 85]},
    {"roll_no": 2, "name": "Pratham", "marks": [90, 80, 85]},
    {"roll_no": 3, "name": "Prince", "marks": [75, 70, 75]},
    {"roll_no": 4, "name": "Mohammed", "marks": [90, 95, 80]},
]

roll_no = int(input("Enter the roll number: "))

display_marksheet(students, roll_no)


def display_marksheet(students, roll_no):
    found_student = next((s for s in students if s["roll_no"] == roll_no), None)

    if found_student:
        name = found_student["name"]
        roll_no = found_student["roll_no"]
        marks = found_student["marks"]
        average_marks = sum(marks) / len(marks)

        print(f"Name: {name}, Roll No: {roll_no}")
        print("Marks:")
        for mark in marks:
            print(mark, end=" ")
        print("\n")

        grade = None
        if 90 <= average_marks <= 100:
            grade = "A+"
        elif 80 <= average_marks < 90:
            grade = "A"
        elif 70 <= average_marks < 80:
            grade = "B"
        elif 60 <= average_marks < 70:
            grade = "C"
        elif 50 <= average_marks < 60:
            grade = "D"
        else:
            grade = "F"

        print(f"Grade: {grade}")
    else:
        print("No student found with the given roll number.")

students = [
    {"roll_no": 1, "name": "Garv", "marks": [80, 70, 85]},
    {"roll_no": 2, "name": "Pratham", "marks": [90, 80, 85]},
    {"roll_no": 3, "name": "Prince", "marks": [75, 70, 75]},
    {"roll_no": 4, "name": "Mohammed", "marks": [90, 95, 80]},
]

roll_no = int(input("Enter the roll number: "))

display_marksheet(students, roll_no)

