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

# user_info = { 'age': 0, 'weight': 0, 'hr': 0, 'time': 0 }

# for info in user_info:
#     user_info[info] = float(input())

# calories = (((user_info['age'] * 0.2757) + (user_info['weight'] * 0.03295) + ((user_info['hr'] * 1.0781) - 75.4991)) * user_info['time']) / 8.368

# print('Calories: {:.2f} calories'.format(calories))\


"""
1.23 LAB: Warm up: Variables, input, and type conversion
(1) Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables. 
Then, output those four values on a single line separated by a space. (Submit for 2 points).

Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

Enter integer (32 - 126):
99
Enter float:
3.77
Enter character:
z
Enter string:
Howdy
99 3.77 z Howdy

(2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

Enter integer (32 - 126):
99
Enter float:
3.77
Enter character:
z
Enter string:
Howdy
99 3.77 z Howdy
Howdy z 3.77 99

(3) Extend to convert the integer to a character by using the 'chr()' function, and output that character. (Submit for 2 points, so 5 points total).

Enter integer (32 - 126):
99
Enter float:
3.77
Enter character:
z
Enter string:
Howdy
99 3.77 z Howdy
Howdy z 3.77 99
99 converted to a character is c
"""
def check_num(num: int) -> bool:
    return num > 31 and num < 127

def check_if_char(char: chr) -> bool:
    if len(char) > 1:
        print(len(char))
        return False
    return True

def type_error(value) -> None:
    print(f'Error on {value}')
    exit()

def check_value(value: any, type: any) -> any:
    if type == 'int':
        num = int(value)
        if check_num(num):
            return int(value)
        return type_error(type)
    elif type == 'float':
        return float(value)
    elif type == 'char':
        if check_if_char(value):
            return value
        return type_error(value)
    elif type == 'string':
        return value

def formatter(lst: list) -> str:
    return str(lst).replace("'", '').replace("[", '').replace("]", '').replace(",", '')

user_inputs = {
    'int': {
        'output': 'Enter integer (32 - 126):\n',
        'value': 0
    },
    'float': {
        'output': 'Enter float:\n',
        'value': 0.0
    },
    'char': {
        'output': 'Enter character:\n',
        'value': chr(0)
    },
    'string': {
        'output': 'Enter string:\n',
        'value': ''
    },
}

for inputs in user_inputs:
    temp_input = input(user_inputs[inputs]['output'])
    user_inputs[inputs]['value'] = check_value(temp_input, inputs)

lst = [user_inputs[x]['value'] for x in user_inputs]

print(formatter(lst))
lst.reverse()
print(formatter(lst))
convert = user_inputs['int']['value']
print(f'{convert} converted to a character is {chr(convert)}')

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
   
# FIXME (2): Output the four values in reverse
   
# FIXME (3): Convert the integer to a character, and output that character