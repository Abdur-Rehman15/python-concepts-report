# ==========practice 1===========
# Implement a @retry decorator to re-execute a function upon failure up to N times

import random
from functools import wraps
import time


def retry(N):
    def original(original_func):
        @wraps(original_func)
        def wrapper(*args, **kwargs):
            attempts = N
            while attempts > 0:
                if original_func(*args, **kwargs) == True:
                    break
                attempts -= 1

        return wrapper

    return original


@retry(5)
def generate_random(target):
    num = random.randint(1, 10)
    print("num generated:", num)
    if num != target:
        print("didnt match with", target, "\n")
        return False
    print("matched with target")
    return True


generate_random(5)

# ==========practice 2===========
# Build a custom context manager measuring the execution time of a code block.


class MeasureTime:
    def __init__(self):
        pass

    def __enter__(self):
        self.time1 = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.time2 = time.time()
        print("Execution time:", self.time2 - self.time1, "secs")
        return self


def printNums(n):
    for i in range(n):
        print(i)


with MeasureTime():
    printNums(5)

# ==========practice 3=============
# Perform read/transform/write operations on a JSON file.

import json

try:
    with open("inventory_data.json", "r") as file:
        data = json.load(file)

    # i'm taking example that double the quantity of each item
    for item in data:
        item["quantity"] *= 2

    with open("inventory_data.json", "w") as file:
        json.dump(data, file, indent=4)

except FileNotFoundError:
    print("File not found")

# ==========checkpoint=============
# Develop a @cache_result decorator caching and returning prior computed values for identical inputs (memoization)


def cache_result(original_func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache:
            result = cache[args]
            print("cache hit")
        else:
            result = original_func(*args, **kwargs)
            cache[args] = result
            print("cache miss")
        return result

    return wrapper


@cache_result
def add(x, y):
    return x + y


print(add(1, 2))
print(add(1, 2))

# ==============numpy practice 1=============
# Normalize a numeric array and extract data points above the statistical mean utilizing a boolean mask.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

normalized = (arr - arr.min()) / (arr.max() - arr.min())
mask = normalized > normalized.mean()

filtered = normalized[mask]
print(filtered)

# ==============pandas practice 1==============

import pandas as pd
df=pd.read_csv('employee_data.csv')
print(df)

# row filtering
experienced = df[df['Experience_Years'] > 3]
print(experienced)

# groupby
salary_mean = df.groupby('Department').agg({
    'Salary':'mean'
})

print(salary_mean)