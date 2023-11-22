"""Implement a Use Case class for generating account statements. It should have a method
named generate_account_statement() that takes account_id as input and returns a
statement string containing transaction details for the given account."""


class GenerateAccountStatement:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        statement = f"Account Number {account.account_number}:\n" \
                    f"ID: {account.account_id}\n " \
                    f"Name: {account.customer_id}\n" \
                    f"left Balance: {account.get_balance()}\n" \
                    f"Transaction History:\n{account.transactions}"
        return statement
