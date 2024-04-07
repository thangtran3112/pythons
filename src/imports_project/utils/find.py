def find_in(iterable, finder, expected):
    for item in iterable:
        if finder(item) == expected:
            return item
    raise NotFoundError(f"Could not find {expected} in provided iterable.")


class NotFoundError(Exception):
    pass
