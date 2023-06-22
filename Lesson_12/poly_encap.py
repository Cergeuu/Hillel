class Car:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode of transport: Private usage")


class Bus:
    def wheels(self):
        print("Number of wheels: 8")

    def mode_of_transport(self):
        print("Mode of transport: Public usage")


car1 = Car()
bus1 = Bus()

vehicles = [car1, bus1]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()


class Vehicle:
    def desc(self):
        pass

    def wheels(self):
        pass


class Car(Vehicle):
    def desc(self):
        print("This is a car.")

    def wheels(self):
        print("Number of wheels: 4")


class Bicycle(Vehicle):
    def desc(self):
        print("This is a bicycle.")

    def wheels(self):
        print("Number of wheels: 2")


car2 = Car()
bicycle = Bicycle()

vehicles2 = [car2, bicycle]

for vehicle in vehicles2:
    vehicle.desc()
    vehicle.wheels()
    print()


class MyClass:
    def __init__(self):
        self._a = 10
        self.__a = 20

    def get_values(self):
        print("Accessing _a:", self._a)
        print("Accessing __a:", self.__a)


obj = MyClass()
obj.get_values()

print("Accessing _a outside the class:", obj._a)
# Наступний рядок викличе помилку, тому що __a є приватним і не доступним поза класом
print("Accessing __a outside the class:", obj.__a)
