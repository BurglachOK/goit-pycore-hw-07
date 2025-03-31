from datetime import datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) <= 9:
            raise ValueError("Phone number must be at least 10 characters long or contains letters")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone: str):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
        #     return True
        # return False


    def edit_phone(self, old_phone: str, new_phone: str):
        phones_list = [p.value for p in self.phones]
        if old_phone in phones_list:
            index = phones_list.index(old_phone)
            self.phones[index] = Phone(new_phone)
            # return True
        # print('Please provide a valid phone number.')
        # return False   


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None


    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]


    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):


        def add_record(self, record: Record):
            self.data[record.name.value] = record


        def find(self, name):
            return self.data.get(name)


        def delete(self, name):
            if name in self.data:
                del self.data[name]


# Створення нової адресної книги
book = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except KeyError:
            print("Contact not found.") 
        except IndexError:
            print("Enter user name.")
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook) -> dict:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    pass


@input_error
def get_contact_by_phone(args, book: AddressBook):
    pass


@input_error
def get_all(book: AddressBook):
    pass


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return f'There is no Contact with Name: {name}'
    record.add_birthday(birthday)
    return f'Successfully added birthday to {name}'


@input_error
def show_birthday(args, book: AddressBook):
    pass


@input_error
def birthdays(args, book: AddressBook):
    pass


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(get_contact_by_phone(args, book))

        elif command == "all":
            print(get_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()














# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")