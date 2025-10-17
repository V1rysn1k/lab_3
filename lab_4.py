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
    
    def __len__(self):
        return self.seats

    def __eq__(self, other):
        return self.speed == other.speed

    def __add__(self, other):
        return self.speed + other.speed
    
class Bike(Transport):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"
    
transport = Transport("Tini&A", 330)
car1 = Car("BaraUber", 1000, 1)
car2 = Car("TuskBall", 200, 4)
bike = Bike("Hook&Q", 500, "mountain")

print(transport)
print(car1)
print(car2)
print(bike)

transport.move()
car1.move()
bike.move()
car1.honk()

print(f"Количество мест в car1: {len(car2)}")

print(f"car1 и car2 имеют одинаковую скорость? {'да' if car1 == car2 else 'нет'}")

print(f"Суммарная скорость car1 и car2: {car1 + car2}")

try:
    result = car1 + bike
    print(f"Результат сложения car1 и bike: {result}")
except TypeError as e:
    print(f"Ошибка при сложении car1 и bike: {e}")