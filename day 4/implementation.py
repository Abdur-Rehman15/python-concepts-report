# =======first class functions========


def square(x):
    return x * x


def my_map(func, my_list):
    new_list = []
    for i in my_list:
        new_list.append(func(i))

    return new_list


squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)


def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


# print_h1 = html_tag("h1")
# print_h1("hellooo")


# ==========closures==========
# (concept of free variables..one use case of closures is logging)

import logging

logging.basicConfig(filename="example.log", level=logging.INFO)


def add(*args):
    return sum(args)


def sub(x, y):
    return x - y


def logger(func):
    def log_func(*args):
        logging.info(f"Running {func.__name__} with arguments {args}")
        print(func(*args))

    return log_func


add_logger = logger(add)
sub_logger = logger(sub)

# add_logger(1, 2, 7)
# sub_logger(10, 5)
# add_logger(4, 10)


# =========decorators===========


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"executed wrapper function before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


# @decorator_function
# def display():
#     print("display function ran")


# @decorator_function
# def display_info(name, age):
#     print(f"{name } is {age} years old.")


# display()
# display_info("john", 25)


from functools import wraps


def my_logger(orig_func):
    import logging

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.basicConfig(
            filename=f"{orig_func.__name__}.log", level=logging.INFO, force=True
        )

        logging.info(f"ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} executed in", t2, "sec")
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    print(f"{name } is {age} years old.")


display_info("abdur", 22)
