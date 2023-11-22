"""Customer entity class"""
import re
import uuid
from src.domain.entities.exception import InvalidPhoneNumberException


class Customer:
    def __init__(self, name, email, phone_number):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone_number = self.validate_phone(phone_number)

    @staticmethod
    def phone_validation(v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        return v
