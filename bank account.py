# create a base class for bank account
class BankAccount:

    # initialize account number, balance attributes
    def __init__(self, account_number, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance

    #  define func for Get account number
    def get_account_number(self):
        return self.__account_number

    # define func for balance
    def get_balance(self):
        return self.__balance

# function for deposit  and check the amount invested and print
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")


  # define function for withdraw amount
    def withdraw(self, amount):

        # use if else statement to get withdraw output
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")

#create a sub class saving account
class SavingsAccount(BankAccount):
   #initialise the attributes account number , balance and interest
    def __init__(self, account_number, balance=0.0, interest_rate=0.03):
        #super() to call base class constructor
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

# declare a function for interest calculation
    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        print(f"Interest calculated: ₹{interest:.2f}")
        return interest

    def apply_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)  # Reuse deposit method to update balance
        print("Interest applied.")

#create a sub class for current account
#initalize attributes account number , balance, minimum balance
#super() to call the base class constructor

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, minimum_balance=1000):
        super().__init__(account_number, balance)
        self.__minimum_balance = minimum_balance


#declare the function to get withdraw statement using elif condition
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif (self.get_balance() - amount) < self.__minimum_balance:
            print(f"Withdrawal denied. Minimum balance of ₹{self.__minimum_balance} must be maintained.")
        else:
            # Use parent's protected deposit/withdraw methods
            super().withdraw(amount)


#by implementing encapsulation we get the output
# Savings Account
s1 = SavingsAccount("SA001", 5000)
s1.apply_interest()
s1.withdraw(1000)

# Current Account
c1 = CurrentAccount("CA001", 3000)
c1.withdraw(2500)  # Denied
c1.withdraw(1500)  # Allowed
