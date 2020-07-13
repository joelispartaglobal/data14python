# class Gooddog:
#
#     animal_type = "canine"  # Attribute (Variable)
#
#     def bark(self):  # Method (function)
#         return "Woof!"
# # You can take out self but the IDE will not like it
#
# fluffy = Gooddog()  # Created an instance of class (an Object)
# print(fluffy.animal_type)
# print(fluffy.bark())
#
# fido = Gooddog()
#
# lassie = Gooddog()
#
# print(fido.animal_type)
# print(lassie.bark())
#
# fido.animal_type = "Bird"
# print(fido.animal_type)
#
# print(lassie.animal_type)
#
# print("----- horrible curse -----")
# Gooddog.animal_type = "arachnid"
# # We can change the attributes of a class
#
# print(lassie.animal_type)
# print(fido.animal_type)
# print(fluffy.animal_type)

# One problem is that we tied the attribute to the class
# We should tie it to the instance instead

# class Dog:
#
#     def __init__(self):  # Initialisation
#         self.name = "Jimmy"
#         self.legs = 4
#         self.animal_kind = "canine"
#
#     def bark(self):
#         return "WOOF!"
#
# big_dog = Dog()
#
# small_dog = Dog()
#
# print(big_dog.name)
# print(small_dog.legs)
# print(big_dog.animal_kind)
#
# print("-------- HORRIBLE CURSE --------")
# Dog.animal_kind = "arachnids"
# Dog.legs = 8
#
# print(big_dog.animal_kind)
# print(small_dog.legs)

class Dog:

    def __init__(self, name):  # Initialisation (runs on instantiation)
        self.name = name
        self.legs = 4
        self.animal_kind = "canine"
        self._secret = "I can't eat chocolate"  # Private variable | The underscore hides it from the IDE

    def __bark(self):
        return "WOOF!"

    def intro(self):
        return f"Woof! My name is {self.name}"

    def get_secret(self):  # Getter
        return self._secret

    def set_secret(self, secret):  # Setter
        self._secret = secret

big_dog = Dog("Jimmy")
# print(big_dog.name)
# print(big_dog.intro())  # Remember to add in brackets
# print(big_dog.reveal_secret())

print(big_dog.get_secret())
big_dog.set_secret("I hid my bone in the garden")
print(big_dog.get_secret())