'''
2.12 LAB: Name format
Many documents use a specific format for a person's name. Write a program whose input is:

firstName middleName lastName

and whose output is:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the form:

firstName lastName

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.

'''

# name = input().split()

# if len(name) > 2:
#     print(f"{name[2]}, {name[0][0:1]}.{name[1][0:1]}.")
# else:
#     print(f"{name[1]}, {name[0][0:1]}.")


'''
2.13 LAB: Count characters
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.

Ex: If the input is:

n Monday
the output is:

1
Ex: If the input is:

z Today is Monday
the output is:

0
Ex: If the input is:

n It's a sunny day
the output is:

2
Case matters.

Ex: If the input is:

n Nobody
the output is:

0
n is different than N.

'''

# def char_count(character: str, input: str) -> int:
#     return input.count(character)

# str = input()

# print(char_count(str[0:1], str[1:]))


'''
2.14 LAB: Warm up: Creating passwords
(1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6
Note: User input is not part of the program output.


(2) Output two passwords using a combination of the user input. Format the passwords as shown below. (Submit for 2 points, so 3 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

(3) Output the length of each password (the number of characters in the strings). (Submit for 2 points, so 5 points total).

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6

First password: yellow_Daisy
Second password: 6yellow6

Number of characters in yellow_Daisy: 12
Number of characters in 6yellow6: 8

'''

input_data = {
    'word1': '',
    'word2': '',
    'number': '',
}

for data in input_data:
    input_data[data] = input()

print(f"You entered: {input_data['word1']} {input_data['word2']} {input_data['number']}")

password1 = f"{input_data['word1']}_{input_data['word2']}"
password2 = f"{input_data['number']}{input_data['word1']}{input_data['number']}"

print(f"First password: {password1}")
print(f"Second password: {password2}")
print(f"Number of characters in {password1}: {len(password1)}")
print(f"Number of characters in {password2}: {len(password2)}")

# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')


# FIXME (2): Output two password options
password1 = favorite_color
print('\nFirst password:')


# FIXME (3): Output the length of the two password options
