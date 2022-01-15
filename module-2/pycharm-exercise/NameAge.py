from datetime import datetime


def prompt(messages: list) -> list:
    lst = []
    for message in messages:
        lst.append(input(message))
    return lst


def calculate_dob(age: str) -> int:
    age = int(age)
    date = datetime.now().year - age
    return date


def output_message(name: str, age: str) -> str:
    dob = calculate_dob(age)
    return f'Hello {name}! You were born in {dob}.'


def main() -> None:
    messages = ['What is your name?', 'How old are you?']
    user_input = prompt(messages)
    output = output_message(user_input[0], user_input[1])
    print(output)
    return None


if __name__ == '__main__':
    main()
