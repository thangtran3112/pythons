"""
https://realpython.com/list-comprehension-python/
"""

cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]

# dictionary comprehension
city_matrix = {city: [0 for _ in range(7)] for city in cities}
print(city_matrix)
"""
{
    'Austin': [0, 0, 0, 0, 0, 0, 0],
    'Tacoma': [0, 0, 0, 0, 0, 0, 0],
    'Topeka': [0, 0, 0, 0, 0, 0, 0],
    'Sacramento': [0, 0, 0, 0, 0, 0, 0],
    'Charlotte': [0, 0, 0, 0, 0, 0, 0]
}
"""

# nested comprehension
maxtrix5 = [[number for number in range(5)] for _ in range(6)]
"""
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
"""

matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flatten = [number for row in matrix for number in row]
# [0, 0, 0, 1, 1, 1, 2, 2, 2]
print(flatten)

## equivalent approach
flat = []
for row in matrix:
    for number in row:
        flat.append(number)

print(flat)
# [0, 0, 0, 1, 1, 1, 2, 2, 2]
