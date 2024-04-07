import json
import os


def getFilePath(fileName):
    return os.path.dirname(os.path.realpath("__file__")) + "/src/json/" + fileName


file = open(getFilePath("friends_json.txt"), "r")

file_contents = json.load(file)  # read file and turn into dictionary

file.close()

print(file_contents["friends"][0])

cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"},
]

file = open(getFilePath("cars_json.txt"), "w")
json.dump(cars, file)
file.close()

my_json_string = '{"friends":[{"name": "John", "age": 30, "city": "New York"}, {"name": "Jane", "age": 25, "city": "Paris"}]}'
people_json = json.loads(my_json_string)  # turn into dictionary
print(people_json)
