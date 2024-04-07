import os

## You will not be able to run this file directly as a script with relative import
# from ..find import NotFoundError
from utils.find import NotFoundError


# Windows require full file path
def getFilePath(file_name):
    return (
        os.path.dirname(os.path.realpath("__file__"))
        + "/src/imports_project/data/"
        + file_name
    )


def save_to_file(content, file_name):
    file_path = getFilePath(file_name)
    throw_if_file_does_not_exist(file_name)
    with open(file_path, "w") as file:
        file.write(content)


def read_file(file_name):
    file_path = getFilePath(file_name)
    throw_if_file_does_not_exist(file_name)
    with open(file_path, "r") as file:
        return file.read()


def read_file_lines(file_name):
    file_path = getFilePath(file_name)
    throw_if_file_does_not_exist(file_name)
    with open(file_path, "r") as file:
        return file.readlines()


def throw_if_file_does_not_exist(file_name):
    if not os.path.exists(getFilePath(file_name)):
        raise NotFoundError(f"File {file_name} does not exist.")


print(__name__)
