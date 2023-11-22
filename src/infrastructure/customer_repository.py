from src.domain.entities.account import Account
from src.domain.entities.customer import Customer


class CustomerRepository:
    def create_customer(self, first_name, last_name, email, phone):
        customer = Customer(first_name, last_name, email, phone)
        customer.account = Account(customer.customer_id)
        return customer