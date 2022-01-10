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

# user_num = int(input('Enter integer:\n'))

# print(f'You entered: {user_num}\n{user_num} squared is {user_num**2}\nAnd {user_num} cubed is {user_num**3} !!' )

# user_num_two = int(input('Enter another integer:\n'))

# print(f'{user_num} + {user_num_two} is {user_num_two + user_num}')
# print(f'{user_num} * {user_num_two} is {user_num_two * user_num}')


"""
1.21 LAB: Divide by x
Write a program using integers user_num and x as input, and output user_num divided by x three times.

Ex: If the input is:

2000
2
Then the output is:

1000 500 250
Note: In Python 3, integer division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).
"""

# user_num = int(input())
# x = int(input())
# output = ""

# for num in range(0, 3):
#     user_num /= x
    
#     if num == 2:
#         print("wooop")
#         output += str(int(user_num))
#         continue
        
#     output += str(int(user_num)) + ' '

# print(output)

'''
1.22 LAB: Expression for calories burned during workout

'''

user_info = { 'age': 0, 'weight': 0, 'hr': 0, 'time': 0 }

for info in user_info:
    user_info[info] = input()

calories = (((user_info['age'] * 0.2757) + (user_info['weight'] * 0.03295) + ((user_info['hr'] * 1.0781) - 75.4991)) * user_info['time']) / 8.368

print('Calories: {:.2f} calories'.format(calories))