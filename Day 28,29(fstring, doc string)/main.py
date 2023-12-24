# Old Way
message = "Hello {}, Good {}"
name = " Ram"
Greeting = "morning"
print(message.format(name, Greeting))

# New Way
print(f"Hello {name}, Good {Greeting}")


def add(a, b):
    """Adds two numbers"""
    print(a + b)
    """ this is not a docstring"""


add(5, 7)
print(add.__doc__)
