def interac():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        else:
            print(
                "{} is {}".format(user_input, "even" if user_input % 2 == 0 else "odd")
            )
        finally:
            user_input = input("Do you want to play again? (y/n) ")
            if user_input != "y":
                print("Goodbye!")
                break


interac()
