class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()


# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
class cat:
    def __init__(self, name, color):
        Animal.__init__(self, name, "Cat")
        self.color = color

    def sleeping(self):
        return f"{self.name} is sleeping."


c1 = cat("Whiskers", "Black")
print(c1.sleeping())
