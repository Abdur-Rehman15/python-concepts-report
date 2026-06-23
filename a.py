print("hello world")
print(True and False)


class bank:
    def __init__(self, amount):
        self.__amount = amount


class point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return point(self.x + other.x)


p1 = point(5)
p2 = point(3)

p3 = p1 + p2

print(p3.x)

from dataclasses import dataclass


class abc:
    name: str
    age: int


class Engine:
    def start(self):
        print("engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()


car = Car()
car.start()

# class method sary objects ky liye wo value change krdeta he
