from collections import UserDict
from datetime import datetime

from src.utils.date_utils import adjust_for_weekend


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()
                days_to_birthday = (birthday_this_year - today).days
                if 0 <= days_to_birthday <= 7:
                    birthday_this_year = adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime('%d.%m.%Y')
                    })
        return upcoming_birthdays
