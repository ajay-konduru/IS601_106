# Task 2 (50 Points)
# This task is divided into sub parts.

# Part 1: Bank Account Class
# 1. Create BankAccount class with following attributes and methods:
    # Attributes:
        # account_number: An integer.
        # balance: A float. 
        # account_holder: A string.
    # Methods:
        # deposit(self, amount): Adds the amount to current balance.
        # withdraw(self, amount): Subtracts the amount from current balance.
        # get_balance(self): Returns the current balance.
# call the BankAccount class by creating an instance of it and pass in the values.
# pass the balance as 1000, give a account number and account holder name  
# call deposit() method, withdraw() method by passing deposit amount as 200, withdraw amount as 700
# then print the total balance of the account (call the get_balance() method)
# Part 1: BankAccount Class
class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance: 
            self.balance -= amount
        else:
            print("Insufficient balance to withdraw.")

    def get_balance(self):
        return self.balance
bank_account = BankAccount(12345, 1000, 'Tester')
bank_account.deposit(200)
bank_account.withdraw(700)
print(f'Total balance after transactions: {bank_account.get_balance()}')

# Part 2: Checking Account Class
# 1. Create CheckingAccount class that inherits from BankAccount
# 2. Add the following attributes and methods to the CheckingAccount class:
    # Attributes:
        # transaction_fees: A float, transaction fees charged for each transaction.
    # Methods:
        # apply_transaction_fees(self): Subtracts the transaction fees from current balance.
# call CheckingAccount class by creating an instance of it
# pass the transaction fees as 34.50 and call the apply_transaction_fees() method
# then print the total balance of the account (call the get_balance() method)
# Part 2: CheckingAccount Class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, transaction_fees):
        super().__init__(account_number, balance, account_holder)
        self.transaction_fees = transaction_fees
    
    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees
checking_account = CheckingAccount(12345, 1000, 'Tester', 34.50)
checking_account.apply_transaction_fees()
print(f'Total balance after transaction fees: {checking_account.get_balance()}')



# Part 3: Savings Account Class
# 1. Create SavingsAccount class that inherits from BankAccount.
# 2. Add the following attributes and methods to the SavingsAccount class:
    # Attributes:
        # interest_rate: A float
    # Methods:
        # calculate_interest(self): Calculates and adds the interest to the current balance.
# call SavingsAccount class by creating an instance of it
# pass the interest rate as 0.12 and call the calculate_interest() method
# then print the total balance of the account (call the get_balance() method)
        # Part 3: SavingsAccount Class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        self.balance += self.balance * self.interest_rate

savings_account = SavingsAccount(12345, 1000, 'Tester', 0.12)
savings_account.calculate_interest()
print(f'Total balance after interest: {savings_account.get_balance()}')