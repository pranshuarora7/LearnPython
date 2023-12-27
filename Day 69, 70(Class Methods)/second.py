class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")


string = "Harri-10000"
e1 = Employee.fromStr(string)
e1.show()
