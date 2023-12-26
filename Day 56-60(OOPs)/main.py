# class Person:
#     name = "Harry"
#     occupation = "SDE"

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a1 = Person()
# a1.name = "fdf"
# a1.info()

# print(Person.name)  # Accessing the attribute using class name


class Information:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        print(f"Name : {self.name}, Age : {self.age}")


a = Information("ABC", "14")
a.disp()


class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
