# Polymorphism

class Vehicle:
     def __init__(self, brand, model, year):
          self.brand = brand
          self. model = model
          self.year = year

     def start(self):
          print("Vehicle is starting.")
     def stop(self):
          print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")

class Plane(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Plane is starting.")

    def stop(self):
        print("Plane is stopping.")


vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2008),
    Plane("Boeing", "747", 2015)
]

for vehicle in vehicles:
          print(f"inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
          vehicle.start()
          vehicle.stop()
          
# Loop through list of vehicles and inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#                 print(f"inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#                 vehicle.start_bike()
#                 vehicle.stop_bike

#     else:
#          raise Exception("Obect is not a valid vehicle")

