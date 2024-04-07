import json
import os


def getFilePath(fileName):
    return os.path.dirname(os.path.realpath("__file__")) + "/src/json/" + fileName


## automatically close the file after the block done
with open(getFilePath("friends_json.txt"), "r") as file:
    file_contents = json.load(file)  # reads file and turns it to dictionary

print(file_contents["friends"][0])


cars = [{"make": "Ford", "model": "Fiesta"}, {"make": "Ford", "model": "Focus"}]

## keeping the context open when operating inside the block
with open(getFilePath("cars_json.txt"), "w") as file:
    json.dump(cars, file)


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]["name"])
