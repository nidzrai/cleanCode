"""Implement a Use Case class for making a transaction. It should have a method named
make_transaction() that takes account_id, amount, and transaction_type (either
&#39;deposit&#39; or &#39;withdraw&#39;) as input and updates the account balance accordingly."""

class MakeTransaction:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        self.account_repository.save_account(account)
