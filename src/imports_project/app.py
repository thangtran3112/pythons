# alternative: import file_operations
# this is absolute import, which starts from root folder,
# where the file app.py is located
from utils.common.file_operations import read_file, save_to_file

save_to_file("Hello, World!", "hello_world.txt")
print(read_file("hello_world.txt"))

print(__name__)
