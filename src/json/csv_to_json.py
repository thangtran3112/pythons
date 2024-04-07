# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json
import os


def getFilePath(fileName):
    return os.path.dirname(os.path.realpath("__file__")) + "/src/json/" + fileName


file = open(getFilePath("csv_to_json.txt"), "r")
content = file.readlines()
file.close()

lines = [line.strip() for line in content]
split_array = list(map(lambda line: line.split(","), lines))
dict_array = []
for line in split_array:
    club, city, country = line
    dict_array.append({"club": club, "city": city, "country": country})

print(dict_array)
output_file = open(getFilePath("json_file.txt"), "w")
json.dump(dict_array, output_file)
