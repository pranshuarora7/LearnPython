s = {1, 2, 3, 4, 5, 2, 3}
print(s)

test = {}
test2 = set()
print(type(test), type(test2))


s1 = {1, 2, 3, 4, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s1.add("5")
print(s1)
s1.pop()
print(s1)
