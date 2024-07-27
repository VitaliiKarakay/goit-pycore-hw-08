import re

from src.address_book.field import Field


class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)
