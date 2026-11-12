from colorama import Fore

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "provide name and phone please"
        except KeyError:
            return "key error"
        except IndexError:
            return "index error"
    return inner

def show_all(contacts):
    contacts_string = ""
    for name, phone in contacts.items():
        contacts_string += f"{Fore.BLUE}{name}{Fore.BLACK}: {Fore.WHITE}{phone}\n"
    return contacts_string

@input_error
def add_contact(args,contacts):
    name,phone=args
    contacts[name]=phone
    return "contact added"

@input_error
def change_contact(args,contacts):
    name,phone=args
    contacts[name]=phone
    return "contact updted"

@input_error
def show_phone(args,contacts):
    name=args[0]
    return contacts[name]



def main():
    contacts = {
    "alex": "123456789",
    "nikita": "987654321",
    "vlad": "555123456",
    "maria": "111222333"
}
    print("Welcome to the assistant bot!")
    while True:

        user_input=input("Enter a command: \n").split()

        if not user_input:
            continue

        command, *args = user_input
        command = command.strip().lower()

        if command in ["close","exit"]:
            print("Good bye!")
            break

        match command:

            case "hello":
                print("How can I help you?")
            case "all":
                print(show_all(contacts))
            case "add":
                print(add_contact(args,contacts))
            case "change":
                print(change_contact(args,contacts))
            case "phone":
                print(show_phone(args,contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()