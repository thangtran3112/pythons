my_students = {"name": "Rolf Smith", "grades": [70, 88, 90, 99]}


def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])


### print(average_grade(my_students))


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Rolf Smith", [70, 88, 90, 99])
student_two = Student("Jose", [50, 60, 70, 80])
print(f"{student_one.name} has an average grade of {student_one.average()}")
print(f"{student_two.name} has an average grade of {student_two.average()}")
