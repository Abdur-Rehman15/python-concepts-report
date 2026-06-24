# =======first class functions========


def square(x):
    return x * x


def my_map(func, my_list):
    new_list = []
    for i in my_list:
        new_list.append(func(i))

    return new_list


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text


print_h1 = html_tag("h1")
print_h1("hellooo")


# ==========closures==========
# (concept of free variables..one use case of closures is logging)

