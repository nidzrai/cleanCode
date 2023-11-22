"""Implement a Use Case class for creating a new account. It should have a method named
create_account() that takes customer_id, name, email, and phone_number as input and
returns an Account object."""

import uuid
from src.domain.entities.account import Account
from src.domain.entities.customer import Customer


class CreateAccount:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number):
        account = Account(account_id=uuid.uuid4(), customer_id=customer_id, account_number=uuid.uuid4())
        customer = Customer(customer_id=customer_id, name=name, email=email, phone_number=phone_number)
        self.account_repository.save_account(account)
        return account

