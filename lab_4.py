class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"
    
class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"
    
class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"