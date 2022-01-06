"""
Eric went to Chipotle to buy 12 different types of cars


Eric
Chipotle
12
cars
"""


# first_name = input()
# generic_location = input()
# whole_number = input()
# plural_noun = input()    

# print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)


"""

this should be the output:

Enter integer:
4
You entered: 4
4 squared is 16 
And 4 cubed is 64 !!
Enter another integer:
5
4 + 5 is 9
4 * 5 is 20

"""

user_num = int(input('Enter integer:\n'))

print(f'You entered: {user_num}\n{user_num} squared is {user_num**2}\nAnd {user_num} cubed is {user_num**3} !!' )

user_num_two = int(input('Enter another integer:\n'))

print(f'{user_num} + {user_num_two} is {user_num_two + user_num}')
print(f'{user_num} * {user_num_two} is {user_num_two * user_num}')