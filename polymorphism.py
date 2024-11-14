class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("range", "Rover")
boat1 = Boat("Ibiza", "Ibiza")
plane1 = Plane("Airway", "fly101")

for x in (car1, boat1, plane1):
    x.move()