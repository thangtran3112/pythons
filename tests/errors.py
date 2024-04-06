class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.make} {self.model}>"


class Garage:
    def __init__(self):
        self.cars = []

    ### supply definition for len method toward Garage object
    def __len__(self):
        return len(self.cars)

    def add_car_impl_error(self, car):
        raise NotImplementedError("We cannot add car to the garage yet!")

    def add_car_checking_type(self, car):
        if not isinstance(car, Car):
            raise TypeError(
                f"Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Cars` objects."
            )
        self.cars.append(car)


ford = Garage()
fiesta = Car("Ford", "Fiesta")

# ford.add_car_checking_type("Fiesta")
# ford.add_car_impl_error("Fiesta")

# if isinstance(fiesta, Car):
#     ford.add_car_checking_type(fiesta)
# else:
#     print("Your car was not a `Car` object")

try:
    ford.add_car_checking_type(Car("Ford", "Fiesta"))
    ford.add_car_checking_type("Truck")
except TypeError as err:
    print(err)
except ValueError as err:
    print("Something went wrong: ", err)
finally:
    print(f"There are now {len(ford.cars)} cars in the garage")
# print(len(ford))


class MyCustomError(TypeError):
    """
    Error Doc: Exception raise when a custom error occurs
    """

    def __init__(self, message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code = code


err = MyCustomError("Ouch! An error happens", 500)
print(err.__doc__)
raise err
