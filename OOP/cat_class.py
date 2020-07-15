# A Cat class

# Attributes
# Probably hidden
# Mood
# Hunger
# Energy
# Which hidden attributes should be changed 0<=x<=10


# Methods
# Sleep
# Play
# Feed

# Hidden method:
# Meow

# Hidden attributes because we don't want the users to change them

class Cat:

    def __init__(self):
        self._mood = 0
        self._hunger = 0
        self._energy = 0
        self._maxmood = 10
        self._maxhunger = 10
        self._maxenergy = 10

    def sleep(self):
        self._meow()
        self._hunger = self._hunger + 5
        if self._hunger > 10:
            self._hunger = self._maxhunger
        self._energy = self._energy + 10
        if self._energy > 10:
            self._energy = self._maxenergy

    def play(self):
        self._meow()
        self._hunger = self._hunger + 5
        if self._hunger > 10:
            self._hunger = self._maxhunger
        self._energy = self._energy - 5
        if self._energy < 0:
            self._energy = 0

    def feed(self):
        self._meow()
        self._hunger = self._hunger - 10
        if self._hunger < 0:
            self._hunger = 0
        self._mood = self._mood + 10
        if self._mood > 10:
            self._mood = self._maxmood
        self._energy = self._energy + 5
        if self._energy > 10:
            self._energy = self._maxenergy

    def _meow(self):
        print("Meeoow")

    def get_cat_stat(self):
        print(f"Mood = {self._mood}, Hunger = {self._hunger}, Energy = {self._energy}")

test_cat = Cat()
# print(test_cat.get_cat_stat())
test_cat.feed()