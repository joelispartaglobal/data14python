class Animal:

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self._hunger = 5
        print("I exist.")

    def breathe(self):
        print("Breathing in...")
        print("Breathing out...")
        self._hunger += 0.1

    def eat(self):
        print("nom nom nom")
        self._hunger = 0

class Mammal(Animal):
    # We want to use the init from Animal class and this class
    def __init__(self, name, colour):
        super().__init__(name, 4)
        self.colour = colour

    def give_birth(self):
        print("I have produced a child. It is not in an egg")

    # We can inherit methods from other classes

class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def wag_tail(self):
        print("swish swish")
        self._hunger += 1

class Labrador(Dog):
    def bark(self):
        print("Woof woof!")
        self._hunger += 0.1

class Bat(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.legs = 2

class Platypus(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def give_birth(self):
        print("I have laid an egg")

# my_mammal = Mammal()
# my_mammal.give_birth()
# my_mammal.breathe()
# print(my_mammal._hunger)

# my_dog = Dog()
# my_dog.breathe()
# my_dog.give_birth()
# my_dog.wag_tail()

# my_labrador = Labrador()
# my_labrador.bark()
# my_labrador.breathe()

# new_dog = Dog("steve", "brown")

perry = Platypus("Perry", "Teal")
perry.give_birth()
