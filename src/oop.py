# my_students = {"name": "Rolf Smith", "grades": [70, 88, 90, 99]}


# def average_grade(student):
#     return sum(student["grades"]) / len(student["grades"])


# ### print(average_grade(my_students))


# class Student:
#     def __init__(self, new_name, new_grades):
#         self.name = new_name
#         self.grades = new_grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# student_one = Student("Rolf Smith", [70, 88, 90, 99])
# student_two = Student("Jose", [50, 60, 70, 80])
# print(f"{student_one.name} has an average grade of {student_one.average()}")
# print(f"{student_two.name} has an average grade of {student_two.average()}")
# print(f"Student.average(student_one) is {Student.average(student_one)}")


# def average(student):
#     return sum(student.grades) / len(student.grades)


# print(f"Average grade of {student_one.name} is {average(student_one)}")


# class Movie:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year


# matrix = Movie("The Matrix", 1999)
# print(matrix.name)


# class Student:
#     def __init__(self, name):
#         self.name = name


# movies = ["Matrix", "Finding Nemo"]
# print(movies.__class__)
# print("Matrix".__class__)


# class Garage:
#     def __init__(self):
#         self.cars = []

#     ### supply definition for len method toward Garage object
#     def __len__(self):
#         return len(self.cars)

#     ### this method is considered indexing an object
#     def __getitem__(self, i):
#         return self.cars[i]

#     ### __repr__ returns a string representation of this object
#     def __repr__(self):
#         return f"Garage with {len(self.cars)} cars"

#     ### a readable string representation of this object for the user
#     # def __str__(self):
#     #     return f'Garage with {len(self.cars)} cars: {", ".join(self.cars)}'


# ford = Garage()
# ford.cars.append("Fiesta")
# ford.cars.append("Focus")
# print(ford.cars)
# print(len(ford))  # Garage .__len__(ford)
# print(ford[0])  # Garage .__getitem__(ford, 0)

# ### Only works when __getitem__ and __len__ are defined inside the class
# for car in ford:
#     print(car)

# ### only when __str__ or __repr__ is defined, __str__ takes precedence
# print(ford)


# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []

#     def average(self):
#         return sum(self.marks) / len(self.marks)


# ### inherit from Student
# class WorkingStudent(Student):
#     def __init__(self, name, school, salary):
#         super().__init__(name, school)
#         self.salary = salary

#     ### use the @ property decorator only when there are no other actions on the method
#     ### communicating with external services, databases are not recommended
#     @property
#     def weekly_salary(self):
#         return self.salary * 37.5


# rolf = WorkingStudent("Rolf", "MIT", 15.50)
# print(rolf.salary)
# rolf.marks.append(25)
# rolf.marks.append(75)
# print(rolf.marks)
# print(rolf.average())
# print(f"rofl.weekly_salary: {rolf.weekly_salary}")


class Foo:

    ### cls is a parameter, represent the class itself
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()


class Bar:

    @staticmethod
    def hi():
        print("Hello, I don't take any parameters.")


another_object = Bar()
another_object.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.amount:.2f}>"

    @staticmethod
    ### define a static method without self
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)


number = FixedFloat(42.1337)
print(number)
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.symbol}{self.amount:.2f}>"


money = Euro(18.786)
print(money)
new_money = Euro.from_sum(11.22, 9.99)
print(f"new_money: {new_money}")  # Euro.from_sum(11.22, 9.99) -> FixedFloat(21.21)


class FixedFloat2:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.amount:.2f}>"

    @classmethod
    ### It is recommended to use @classmethod instead of @staticmethod
    ### the class method will be propagated to the child instance with cls properly
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class EuroClass2(FixedFloat2):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.symbol}{self.amount:.2f}>"


new_money = EuroClass2.from_sum(11.22, 9.99)
print(f"new_money: {new_money}")  #  EuroClassMethod(21.21)
second_money = FixedFloat2.from_sum(33.22, 44.44)
print(f"second_money: {second_money}")  #  FixedFloatClassMethod(77.66)
