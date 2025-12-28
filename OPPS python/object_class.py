# Base class Car
class Car:
    # Class variable (shared by all objects)
    total_car = 0

    # Constructor method
    def __init__(self, brand, model):
        # Private variables (name mangling)
        self.__brand = brand
        self.__model = model

        # Increment total car count whenever a new object is created
        Car.total_car += 1

    # Getter method for brand
    def get_brand(self):
        return self.__brand + " !"

    # Returns full name of the car
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Method to show fuel type
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Static method (does not depend on object or class variables)
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # Property decorator to access model like an attribute
    @property
    def model(self):
        return self.__model
    

# Child class inheriting from Car
class ElectricCar(Car):
    # Constructor for ElectricCar
    def __init__(self, brand, model, battery_size):
        # Calling parent class constructor
        super().__init__(brand, model)
        self.battery_size = battery_size

    # Method overriding (polymorphism)
    def fuel_type(self):
        return "Electric charge"


# -----------------------------
# Multiple Inheritance Example
# -----------------------------

# Battery class
class Battery:
    def battery_info(self):
        return "this is battery"

# Engine class
class Engine:
    def engine_info(self):
        return "This is engine"

# ElectricCarTwo inherits from Battery, Engine, and Car
class ElectricCarTwo(Battery, Engine, Car):
    pass   # No extra methods, uses parent class methods


# Creating object of ElectricCarTwo
my_new_tesla = ElectricCarTwo("Tesla", "Model S")

# Calling method from Engine class
print(my_new_tesla.engine_info())

# Calling method from Battery class
print(my_new_tesla.battery_info())
