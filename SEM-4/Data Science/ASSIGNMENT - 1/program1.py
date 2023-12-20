
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif 80 < mark < 90:
        return "B"
    elif 70 < mark < 80:
        return "C"
    elif 60 < mark < 70:
        return "D"
    else:
        return "E"

marks = []
for i in range(5):
    n = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(n)

individual_grades = list(filter(lambda x: True if calculate_grade(x) else False, marks))

print("\nIndividual Grades:")
for idx, grade in enumerate(individual_grades, start=1):
    print(f"Subject {idx}: Grade {calculate_grade(grade)}")

total_marks = sum(marks)
average_marks = total_marks / 5

overall_grade = calculate_grade(average_marks)
print(f"\nOverall Grade based on average marks: {overall_grade}")
