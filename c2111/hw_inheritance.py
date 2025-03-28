# Завдання 1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

cat=Cat("Барсик",3)
print(cat.name)

# Завдання 2
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Я рухаюся зі швидкістю {self.speed} км/год."


class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)


class Plane(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)


car = Car(120)
plane = Plane(800)

print(car.move())
print(plane.move())
