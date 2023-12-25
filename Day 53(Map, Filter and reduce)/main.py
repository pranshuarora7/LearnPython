l = [1, 2, 3, 4, 5]

new = list(map(lambda x: x * 2, l))
print(new)


def filter_function(a):
    return a > 2


new2 = list(filter(filter_function, l))
print(new2)

from functools import reduce

sum = reduce(lambda x, y: x + y, l)
print(sum)
