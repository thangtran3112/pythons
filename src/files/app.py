import os

path = os.path.dirname(os.path.realpath("__file__")) + "/src/files/data.txt"
print(path)
my_file = open(path, "r")
file_content = my_file.read()

my_file.close()
print(file_content)

my_file_writing = open(path, "w")  # erase the file
my_file_writing.write("Hello, World!")
my_file_writing.close()
