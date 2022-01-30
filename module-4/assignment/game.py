"""
Sample Output

Below is one sample output of the program, with the user input demonstrated by bold font.

Welcome to the higher/lower game, Bella!
Enter the lower bound: 10
Enter the upper bound: 30
Great, now guess a number between 10 and 30: 20
Nope, too low.
Guess another number: 25
Nope, too high.
Guess another number: 23
You got it!

Below is another sample output of your program, with the user input demonstrated by bold font.

Welcome to the higher/lower game, Bella!
Enter the lower bound: 10
Enter the upper bound: 5
The lower bound must be less than the upper bound.
Enter the lower bound: 10
Enter the upper bound: 20
Great, now guess a number between 10 and 20: 25
Nope, too high.
Guess another number: 15
Nope, too low.
Guess another number: 17
You got it!


Pseudocode


"""
import random


def number_guess(guessed_number: int, random_number: int):
    return guessed_number == random_number, 'low' if guessed_number < random_number else 'high'


def game_start_loop():
    while True:
        print('Welcome to the higher/lower game, Bella!')
        low_num = int(input('Enter the lower bound: '))
        high_num = int(input('Enter the upper bound: '))

        if high_num > low_num:
            break

        print('The lower bound must be less than the upper bound.')
    return low_num, high_num


def game_loop(guessed_number: int, random_number: int):
    while True:
        outcome, low_high = number_guess(guessed_number, random_number)

        if outcome:
            print('You got it!')
            break

        print(f'Nope, too {low_high}')
        print('number', random_number)

        guessed_number = int(input('\nGuess another number: '))


def main():
    low_num, high_num = game_start_loop()

    random_number = random.randint(low_num, high_num)

    guessed_number = int(input(
        f'\nGreat, now guess a number between {low_num} and {high_num}: '))

    game_loop(guessed_number, random_number)


if __name__ == '__main__':
    main()
