"""
Docstring for alx_be_python.programming_paradigm.bank_account

Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. 
Use command line arguments to interact with instances of this class.

Task Description:
You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.
"""
#class declaration
class BankAccount:
    #constructor
    def __init__(self, amount = 0):
        self.amount = amount

    # Implement deposit(amount), withdraw(amount), and display_balance() methods.
    #deposit(amount) method
    def deposit(self, amount):
        self.amount += amount
        return amount

    #withdraw(amount) method
    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        if self.amount < amount:
            print(f"The amount $ {amount} you want to withdraw is greater than current bank balance $ {self.amount}")
            pass
    #display_balance() method
    def display_balance(self):
        print(f"Current Balance: $[{self.amount}]")

#object implementation
# test1 = BankAccount()
# test1.deposit(50)
# test1.withdraw(70)

# test1.display_balance()