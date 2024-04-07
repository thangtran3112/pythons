import os


def getFilePath(fileName):
    return os.path.dirname(os.path.realpath("__file__")) + "/src/csv/" + fileName


file = open(getFilePath("csv_data.txt"), "r")
lines = file.readlines()
file.close()

# get index 1 onward
lines = [line.strip() for line in lines[1:]]  # lines[1:]

for line in lines:
    person_data = line.split(",")
    name, age, university, degree = person_data
    print(
        f"{name.title()} is {age} years old, and studies {degree.capitalize()} at {university.title()}."
    )

sample_csv_value = ",".join(["john", "25", "MIT", "computer science"])
print(sample_csv_value)
