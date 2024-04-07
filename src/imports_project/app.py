# alternative: import file_operations
from utils.file_operations import read_file, save_to_file

save_to_file("Hello, World!", "hello_world.txt")
print(read_file("hello_world.txt"))
