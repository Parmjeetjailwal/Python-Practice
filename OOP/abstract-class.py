# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but doesn't have an implementation

# prevents a user from creating an object methods in a child class
# and also compels a user to override abstract methods in a child class

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
        print("----------------")

    def stop(self):
        print("This car is stopped")
        print("----------------")
        
class Train(Vehicle):

    def go(self):
        print("This train has to go")
        print("----------------")

    def stop(self):
        print("This train is stopped")
        print("----------------")

# vehicle = Vehicle()
car = Car()
train = Train()

# vehicle.go()
car.go()
train.go()

# vehicle.stop()
car.stop()
train.stop()
        