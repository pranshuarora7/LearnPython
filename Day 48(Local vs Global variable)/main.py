x = 10  # global variable


def my_function():
    global x
    x = 5


my_function()
print(x)
