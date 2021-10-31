class Car:
    
    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color


Car_1 = Car()
Car_2 = Car()

Bike_1 = Motorcycle()
Bike_2 = Motorcycle()

change_color(Car_1,"red")
change_color(Car_2,"white")
change_color(Bike_1,"black")
change_color(Bike_2,"orange")

print("---------------------")
print(f"Color of Car_1 is {Car_1.color}")
print("---------------------")
print(f"Color of Car_2 is {Car_2.color}")
print("---------------------")
print(f"Color of Bike_1 is {Bike_1.color}")
print("---------------------")
print(f"Color of Bike_2 is {Bike_2.color}")
print("---------------------")


