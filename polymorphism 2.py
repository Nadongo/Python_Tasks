class Vehicle:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")

class Car(Vehicle):
        pass

class Boat(Vehicle):
        def move(self):
            print("Sail")

class Plane(Vehicle):
        def move(self):
            print("Fly")

car1 = Car ("Range", "Rover")
boat1 = Boat ("Ibiza","Tour")
plane1 = Plane ("Airbus", "A380")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move