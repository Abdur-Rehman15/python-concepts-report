# =======practice 1==========
# Implement a BankAccount class supporting deposits, withdrawals, and validation logic.


class BankAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.balance = 0

    def __validateAmount(self, x):
        if not isinstance(x, int):
            raise TypeError
        elif x < 0:
            raise ValueError

    def __validateWithdrawal(self, amount):
        if self.balance < amount:
            raise ValueError

    def depositAmount(self, amount):
        try:
            self.__validateAmount(amount)
            self.balance += amount
            print("amount deposited successfully")

        except TypeError:
            print("invalid data type entered")

        except ValueError:
            print("entered amount less than 0")

    def withdrawAmount(self, amount):
        try:
            self.__validateAmount(amount)
            self.__validateWithdrawal(amount)
            self.balance -= amount
            print("amount withdrawn successfully. remaining balance: ", self.balance)

        except ValueError:
            print("balance not sufficient")


person1 = BankAccount("abdur", "abc@gmail.com")

person1.depositAmount(100)
person1.withdrawAmount(20)
person1.depositAmount("abc")

# =======practice 2==========
# Write a generator yielding the Fibonacci sequence.


def fibonacciSequence(n):
    first = 1
    second = 1
    while first <= n:
        yield first
        temp = first
        first = second
        second = first + temp


for x in fibonacciSequence(15):
    print(x)


# =======practice 3==========
# Write a generator handling line-by-line reads of a large file.


def fileRead_by_Generator():
    with open("large.txt", "r") as f:
        for line in f:
            yield line


for x in fileRead_by_Generator():
    print(x)

# =========checkpoint=========
# Construct a Shape base class extended by Circle and Rectangle subclasses, each implementing a distinct area() computation.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


sq = Square(5)
print("square area:", sq.area())

rec = Rectangle(2, 3)
print("rectangle area:", rec.area())
