from src.address_book.address_book import AddressBook
from src.address_book.record import Record
from src.bot.commands import parse_input
from src.bot.handlers import handle_invalid_command, command_handlers


def main():
    contacts = AddressBook()

    record1 = Record("Valera")
    record2 = Record("Olya")
    record3 = Record("Vitaliy")
    record1.add_phone("0501111111")
    record2.add_phone("0967350676")
    record3.add_phone("0509081174")
    contacts.add_record(record1)
    contacts.add_record(record2)
    contacts.add_record(record3)

    print("Welcome to the assistant bot!")
    print("Input 'help' for a list of commands.")
    should_exit = False
    while not should_exit:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler = command_handlers.get(command, handle_invalid_command)
        should_exit = handler(args, contacts)


if __name__ == "__main__":
    main()
