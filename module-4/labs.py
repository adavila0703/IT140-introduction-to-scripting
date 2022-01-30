"""
4.14 LAB: Count input length without spaces, periods, or commas

Given a line of text as input, output the number of characters excluding spaces, 
periods, or commas.

Ex: If the input is:

Listen, Mr. Jones, calm down.
the output is:

21
Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

"""


# character_number = 0
# input_string = input()

# exclusion = [' ', '.', ',']

# for character in input_string:
#     if character in exclusion:
#         continue
#     character_number += 1

# print(character_number)


"""
4.15 LAB: Password modifier

Many user-created passwords are simple and easy to guess. 
Write a program that takes a simple password and makes it stronger by replacing characters 
using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
Ex: If the input is:

mypassword
the output is:

Myp@ssw.rdq*s
Hint: Python strings are immutable, but support string concatenation.
 Store and build the stronger password in the given password variable.

"""


# word = input()
# password = ''

# replacement = {
#     'i': '!',
#     'a': '@',
#     'm': 'M',
#     'B': '8',
#     'o': '.',
# }

# for character in word:
#     special_char = replacement.get(character)
#     if special_char != None:
#         password += special_char
#     else:
#         password += character

# password += 'q*s'

# print(password)


"""
4.16 LAB: Warm up: Drawing a right triangle

This program will output a right triangle based on user specified height triangle_height 
and symbol triangle_char.

(1) The given program outputs a fixed-height triangle using a * character. Modify the given 
program to output a right triangle that instead uses the user-specified triangle_char character. 
(1 pt)

(2) Modify the program to use a loop to output a right triangle of height triangle_height. 
The first line will have one user-specified character, such as % or *. Each subsequent line 
will have one additional user-specified character until the number in the triangle's base reaches 
triangle_height. Output a space after each user-specified character, including a line's last 
user-specified character. (2 pts)

Example output for triangle_char = % and triangle_height = 5:

Enter a character:
%
Enter triangle height:
5

% 
% % 
% % % 
% % % % 
% % % % % 

"""

# triangle_char = input('Enter a character:\n')
# triangle_height = int(input('Enter triangle height:\n\n'))

# triangle_length = 1

# for height in range(triangle_height):
#     print((triangle_char + ' ') * triangle_length)
#     triangle_length += 1


"""
4.17 LAB: Mad Lib - loops
Mad Libs are activities that have a person provide various words, 
which are then used to complete a short story in unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input, and outputs a sentence 
using the input values as shown in the example below. The program repeats until the input
 string is quit and disregards the integer input that follows.

Ex: If the input is:

apples 5
shoes 2
quit 0
the output is:

Eating 5 apples a day keeps the doctor away.
Eating 2 shoes a day keeps the doctor away.
"""

user_input = ''

while True:
    user_input = input().split()
    if user_input[0] == 'quit':
        break
    print(
        f'Eating {user_input[1]} {user_input[0]} a day keeps the doctor away.')
