class math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(a, b):
        return a + b


a = math(7)
print("Addition of 4 and 3 is :", math.add(4, 3))
# calling the static method directly from the class
print("Value of number in object a is :", a.num)
