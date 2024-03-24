MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the title: ")
    director = input("Enter the director: ")
    year = input("Enter the year: ")
    movies.append({"title": title, "director": director, "year": year})


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    search_title = input("Enter the title: ")
    for movie in movies:
        if search_title == movie["title"]:
            print("Found the movie:")
            print_movie(movie)
            break
    else:
        print("Movie not found")


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")
    print("---")


user_options = {"a": add_movie, "l": list_movies, "f": find_movie}


def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")
        selection = input(MENU_PROMPT)


menu()
