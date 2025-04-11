#create a base class for vehicles
class Vehicle:

    #__init__ method initialize the model and rental attributes
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate  # base rate per day

# define a function to calculate  rental based on days
    def calculate_rental(self, days):
        return self.rental_rate * days

# create sub class  for car
class Car(Vehicle):

    # initialise model, rate , using __init__ method
    def __init__(self, model, rental_rate, seats, ac):

        # super()  default method  use to call base class constructor
        super().__init__(model, rental_rate)
        self.seats = seats
        self.ac = ac  # True if AC is included

# calculate the rental include ac charge
    def calculate_rental(self, days):
        ac_charge = 200 if self.ac else 0
        return (self.rental_rate + ac_charge) * days

# create sub class for bike
class Bike(Vehicle):

    # intialise model, rental, helmet
    def __init__(self, model, rental_rate, helmet_included):

       #call the bese class constructor
        super().__init__(model, rental_rate)
        self.helmet_included = helmet_included

# define function for calculate rental include helmet charge
    def calculate_rental(self, days):
        helmet_charge = 50 if self.helmet_included else 0
        return (self.rental_rate + helmet_charge) * days

# same as above
#create a sub class truck
# initalize model rental and load capacity attributes
# use super() to call the base clASS constructor

class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity  # in tons

# define calculation function
    def calculate_rental(self, days):
        # Additional charge: ₹100 per ton per day
        load_charge = self.load_capacity * 100
        return (self.rental_rate + load_charge) * days


# implement polymorphism in sub class
vehicles = [
    Car("Hyundai i20", 1800, 5, ac=True),
    Bike("Honda Activa", 500, helmet_included=True),
    Truck("Tata 407", 3000, load_capacity=3)
]

# Rental duration for each vehicle
rental_days = [3, 2, 4]

# Polymorphic call to calculate rental
for vehicle, days in zip(vehicles, rental_days):
    print(f"{vehicle.model} rental for {days} days: ₹{vehicle.calculate_rental(days)}")
