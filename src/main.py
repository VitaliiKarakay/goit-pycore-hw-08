from src.address_book.address_book import AddressBook
from src.bot.commands import parse_input
from src.bot.handlers import handle_invalid_command, command_handlers
from src.utils.save_load import load_data, save_data


def main():
    contacts = load_data()

    print("Welcome to the assistant bot!")
    print("Input 'help' for a list of commands.")
    should_exit = False
    while not should_exit:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler = command_handlers.get(command, handle_invalid_command)
        save_data(book=contacts)
        should_exit = handler(args, contacts)


if __name__ == "__main__":
    main()
