class Employee:
    company_name = "Sprynt"

    def __init__(self, name):
        self.name = name
        self.appraisal = 2

    def show(self):
        print("Name : ", self.name)
        print("Appraisal : ", self.appraisal)
        print("Comapny :", self.company_name, "\n")


e1 = Employee("Hariram")
# e1.show()
e1.appraisal = 1
Employee.show(e1)

e2 = Employee("Nikita")
Employee.show(e2)

e3 = Employee("Prasad")
Employee.show(e3)
