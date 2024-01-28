def calculate_gpa(course_data):
    total_credits = 0
    total_grade_points = 0

    for course in course_data:
        credit_hours = course['credit_hours']
        grade = course['grade']

        total_credits += credit_hours
        total_grade_points += credit_hours * get_grade_point(grade)

    if total_credits == 0:
        return 0  # Avoid division by zero

    return total_grade_points / total_credits

def get_grade_point(grade):
    grade_points = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
    return grade_points.get(grade.upper(), 0.0)

def get_course_data():
    num_courses = int(input("Enter the number of courses: "))

    course_data = []
    for _ in range(num_courses):
        course_name = input("Enter course name: ")
        credit_hours = int(input("Enter credit hours for {}: ".format(course_name)))
        grade = input("Enter grade (A, A-, B+, etc.) for {}: ".format(course_name))

        course_data.append({'name': course_name, 'credit_hours': credit_hours, 'grade': grade})

    return course_data

def main():
    print("Welcome to the GPA Calculator!")

    course_data = get_course_data()

    gpa = calculate_gpa(course_data)

    print("\nYour GPA is: {:.2f}".format(gpa))

if __name__ == "__main__":
    main()
