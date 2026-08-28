class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


# Create objects
car1 = Car("Toyota", "Fortuner", 7)
bike1 = Bike("Honda", "Shine", 125)

print("Car:")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Seats:", car1.seats)