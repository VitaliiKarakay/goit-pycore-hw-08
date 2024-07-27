from src.address_book.birthday import Birthday
from src.address_book.name import Name
from src.address_book.phone import Phone


class Record:
    def __init__(self, name, birthday):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        return any(p.value == phone for p in self.phones)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
