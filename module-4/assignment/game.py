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


def main():
    while True:
        print('Welcome to the higher/lower game, Bella!')
        low_num = int(input('Enter the lower bound: '))
        hight_num = int(input('Enter the upper bound: '))

        if hight_num > low_num:
            break

        print('The lower bound must be less than the upper bound.')

    random_number = random.randint(low_num, hight_num)

    guessed_number = int(input(
        f'\nGreat, now guess a number between {low_num} and {hight_num}: '))

    while True:
        outcome, low_high = number_guess(guessed_number, random_number)

        if outcome:
            print('You got it!')
            break

        print(f'Nope, too {low_high}')

        guessed_number = int(input('\nGuess another number: '))


if __name__ == '__main__':
    main()
