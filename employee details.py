# create a base class for employee details
class Employee:
    def __init__(self, name, salary):
        # init-- initialize the name and salary
        self.name = name
        self.salary = salary

#define a function for salary calculation
    def calculate_salary(self):
        # This method is meant to be overridden
        return self.salary

# create a  1st subclass for permenant employee
class PermanentEmployee(Employee):
    # initialise name ,salary, bonus
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

# define func for caculate the salary
    def calculate_salary(self):
        return self.salary + self.bonus

# create a  2ndsubclass  for contract employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        # init with hourly rate
        # We don't use salary directly here
        #super () to call the base class constructor
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked


# declare a func to calcule salary for hourly basis
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# create a  3rd subclass for manager
class Manager(Employee):
    def __init__(self, name, salary, bonus, allowance):
        #init with name,salary,bonus and allowance
        # super () to call the base class constructor
        super().__init__(name, salary)
        self.bonus = bonus
        self.allowance = allowance

#declare func to calculate salary with allowance
    def calculate_salary(self):
        return self.salary + self.bonus + self.allowance

# Create objects of different types of the employees
emp1 = PermanentEmployee("Arun", 30000, 5000)
emp2 = ContractEmployee("Bala", 200, 160)   # 200/hour × 160 hours
emp3 = Manager("Chitra", 50000, 10000, 8000)

# List of base class references
employees = [emp1, emp2, emp3]

# implement Polymorphism we get output
for emp in employees:
    print(f"{emp.name}'s salary: {emp.calculate_salary()}")
