def find_in(iterable, finder, expected):
    for item in iterable:
        if finder(item) == expected:
            return item
    raise NotFoundError(f"Could not find {expected} in provided iterable.")


class NotFoundError(Exception):
    pass


print(__name__)

## Only run when executing this file as a script
if __name__ == "__main__":
    print(find_in(["Rolf", "Jen", "Anna"], lambda x: x, "Jen"))
