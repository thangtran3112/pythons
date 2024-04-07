import os


# Windows require full file path
def getFilePath(file_name):
    return (
        os.path.dirname(os.path.realpath("__file__"))
        + "/src/imports_project/data/"
        + file_name
    )


def save_to_file(content, file_name):
    file_path = getFilePath(file_name)
    with open(file_path, "w") as file:
        file.write(content)


def read_file(file_name):
    file_path = getFilePath(file_name)
    with open(file_path, "r") as file:
        return file.read()


def read_file_lines(file_name):
    file_path = getFilePath(file_name)
    with open(file_path, "r") as file:
        return file.readlines()
