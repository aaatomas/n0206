from multiprocessing.connection import Client


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Withdrawed: {amount}")
        else:
            print(f"You don't have enough money!")

    def show(self):
        print(f"Balance: {self.balance}")


customer1 = BankAccount("Customer1", 100)
customer2 = BankAccount("Customer2", 300)

print("---" * 15, customer1.owner, "---" * 15)
customer1.deposit(100)
customer1.withdraw(300)
customer1.show()

print("---" * 15, customer2.owner, "---" * 15)
customer2.deposit(100)
customer2.withdraw(300)
customer2.show()