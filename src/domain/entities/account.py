"""Account Entity CLass"""


class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance+amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("less balance")
        self.balance = self.balance-amount

    def get_balance(self):
        return self.balance

