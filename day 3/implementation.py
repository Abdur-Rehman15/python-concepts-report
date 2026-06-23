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

def add_nums(*args):
    return sum(args)


print(add_nums(1, 2, 3))
print(add_nums(1, 2, 3, 4, 5, 6))


def build_profile(**kwargs):
    role = kwargs.get("role")
    guest = kwargs.get("guest")
    print(f"Role: {role}, guest: {guest}")


build_profile(username="alice", email="abc@gmail.com", role="admin")

# *args make tuple of all the passed params
# **kwargs make key values pairs of passes params

# ========Iterators========

l = [1, 2, 3, 4, 5]
iterator = iter(l)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break

# iters are used when we deal with massive dataset size. its not possible to load all of it, and then start processing. instead, we use iterators


class nums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


obj = nums()
iterator = iter(obj)

# for x in iterator:
#     print(x)


# =========generators========

def countUpto(n):
    count = 1
    while count <= n:
        yield n
        count += 1


abc = countUpto(5)
print(abc)

def my_generator():
    yield 1
    yield 2
    yield 3


gen=my_generator()

try:
        
    print(next(gen))
    print(next(gen))

    print(next(gen))
    print(next(gen))
    
except StopIteration:
      print("oops")