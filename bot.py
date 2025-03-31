from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
     def __init__(self, name: str):
        if not name:
            print(ValueError("Name cannot be empty."))
        super().__init__(name)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) <= 9:
            raise ValueError("Phone number must be at least 10 characters long or contains letters")
        super().__init__(value)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
            return True
        return False


    def change_phone(self, old_phone: str, new_phone: str):
        phones_list = [p.value for p in self.phones]
        if old_phone in phones_list:
            index = phones_list.index(old_phone)
            self.phones[index] = Phone(new_phone)
            return True
        print('Please provide a valid phone number.')
        return False   
    

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj is not None:
            self.phones.remove(phone_obj)
            return True
        return False
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
        

        def new_record(self, name: str):
            if name not in self.data:
                self.data[name] = Record(name)
            return self.data[name]
        
        
        def add_record(self, name: str, phone = ''):
            record = self.new_record(name)
            if len(phone) > 9:
                if record.add_phone(phone):
                    return record
                print('Phone number already exists')
                return None
            print(ValueError("Phone number must be at least 10 characters long"))
            return None


        def get_records(self):
            for name, record in book.data.items():
                yield record


        def change_record(self, name: str, old_phone: str, new_phone: str):
            if name in self.data:
                record = self.data[name]
                if record.change_phone(old_phone, new_phone):
                    return record
                return None
            else:
                return None


        def __str__(self):
            return "\n".join(str(record) for record in self.data.values())
        

        def get_contact(self, name: str):
            if name in self.data:
                return self.data[name]
            else:
                return f"Contact {name} not found."
            
        
        def delete(self, name: str):
            if name in self.data:
                del self.data[name]
                return True
            return False


        def remove_phone_from_contact(self, name: str, phone: str):
            if name in self.data:
                return self.data[name].remove_phone(phone)
            return False


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
def add_contact(args):
    name, phone = args
    if phone not in book.data:
        if book.add_record(name, phone) is not None:
            return "Contact added."
        return None


@input_error
def change_contact(args):
    name, old_phone, new_phone = args
    change = book.change_record(name, old_phone, new_phone)
    if change is not None:
        print(change, "\nContact changed.")
    else:
        print('Contact not found')


@input_error
def show_phone(args):
    name = args[0]
    get = book.get_contact(name)
    if get:
        print(get)


@input_error
def show_all():
    if book.data:
        for item in book.get_records():
            print(item)
    else:
        print("No contacts found.")


@input_error
def delete_contact(args):
    name = args[0]
    if book.delete(name):
        print("Deletion was successful.")
    else:
        print("Contact not found.")


@input_error
def remove_phone(args):
    name, phone = args
    if book.remove_phone_from_contact(name, phone):
        print("Phone removed successfully.")
    else:
        print("Phone not found or contact does not exist.")


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            func_output = add_contact(args)
            if func_output is not None:
                print(func_output)
        elif command == "change":
            change_contact(args)
        elif command == "phone":
            show_phone(args)
        elif command == "all":
            show_all()
        elif command == 'delete':
            delete_contact(args)
        elif command == 'remove':
            remove_phone(args)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
