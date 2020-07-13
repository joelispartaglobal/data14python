# Create a car class
# Doors, model,, make
# Speed
# Acceleration and brake methods
# Maximum speed

class Car:
    def __init__(self, make):
        self.make = make
        self._speed = 0
        self.maxspeed = 200

    def acceleration(self, increase: int):
        self._speed = self._speed + increase * 10
        if self._speed > 200:
            self._speed = 200
        return self._speed

    def brake(self, decrease: int):
        self._speed = self._speed - decrease * 20
        if self._speed < 0:
            self._speed = 0
        return self._speed

my_car = Car("Toyota")
print(my_car.acceleration(30))