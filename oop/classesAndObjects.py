class BankAccount:
    # Class attribute shared by all instances of the class.
    interest_rate = 0.02

    # Constructor to initialize the account with an account holder and balance.
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    # Method to withdraw money from the account.
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount."

    # Method to calculate interest and add it to the account.
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added interest. New balance: ${self.balance}"

    # Method to get the account information.
    def get_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%"


# Create two bank accounts.
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Deposit and withdraw money from the accounts.
print(account1.deposit(500))      # Deposited $500. New balance: $1500
print(account2.withdraw(200))     # Withdrew $200. New balance: $300

# Add interest to the accounts.
print(account1.add_interest())    # Added interest. New balance: $1530.0
print(account2.add_interest())    # Added interest. New balance: $306.0

# Get account information.
print(account1.get_info())       # Account holder: Alice, Balance: $1530.0, Interest Rate: 2.0%
print(account2.get_info())       # Account holder: Bob, Balance: $306.0, Interest Rate: 2.0%
