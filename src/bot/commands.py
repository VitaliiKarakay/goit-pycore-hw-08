import utils.constants
from src.address_book.address_book import AddressBook
from src.address_book.record import Record
from src.bot.decorator import input_error
from src.utils.exceptions import InvalidPhoneNumberLengthError


@input_error
def change_phone_by_name(args, contacts):
    name = str.capitalize(args[0])
    old_phone = args[1]
    new_phone = args[2]
    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")
    if len(new_phone) != 10:
        raise InvalidPhoneNumberLengthError
    record = contacts[name]
    if record.find_phone(old_phone):
        record.edit_phone(old_phone, new_phone)
        return f"{name}'s phone number changed from {old_phone} to {new_phone}."
    else:
        return f"{name} does not have the phone number {old_phone}."


@input_error
def get_phone_by_name(args, contacts):
    name = str.capitalize(args[0])
    return f"{name}: {contacts[name]}"


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    name = name.strip().capitalize()
    if len(phone) != 10:
        raise InvalidPhoneNumberLengthError
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message


@input_error
def print_commands():
    print(utils.constants.COMMANDS)


@input_error
def add_birthday(args, contacts):
    name, birthday = args
    name = name.strip().capitalize()
    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")
    record = contacts[name]
    record.add_birth(birthday)
    return f"Birthday added to {name}."


@input_error
def show_birthday(args, contacts):
    name = args[0].strip().capitalize()
    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")
    record = contacts[name]
    if record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return f"{name} does not have a birthday set."


@input_error
def birthdays(args, contacts):
    return contacts.get_upcoming_birthdays()
