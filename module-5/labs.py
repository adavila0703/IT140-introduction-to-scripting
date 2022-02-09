"""
5.18 LAB: Swapping variables
Write a program whose input is two integers and whose output is the two integers swapped.

Ex: If the input is:

3
8
the output is:

8 3
Your program must define and call the following function. swap_values() returns the two values in swapped order.
def swap_values(user_val1, user_val2)


"""


# def swap_values(user_val1, user_val2):
#     return user_val2, user_val1


# def main():
#     num1, num2 = swap_values(input(), input())
#     print(num1, num2)


# if __name__ == '__main__':
#     main()


"""
5.19 LAB: Exact change - functions
Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Ex: If the input is:

0 
or less, the output is:

no change
Ex: If the input is:

45

the output is:
1 quarter
2 dimes 

Your program must define and call the following function. 
The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
def exact_change(user_total)

"""
CHANGE_CONST = {
    'dollar': 100,
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}


def calculate_change(money: int, change_collection: dict = {}) -> dict:
    if money == 0:
        return change_collection
    diff = 0
    for change in CHANGE_CONST:
        if (money - CHANGE_CONST[change]) >= 0:
            diff = CHANGE_CONST[change]
            if change_collection.get(change) != None:
                change_collection[change] += 1
                break
            else:
                change_collection[change] = 1
                break
    return calculate_change(money - diff, change_collection)


def get_output(value: int, name: str):
    if value > 1:
        if name == 'penny':
            return f"{value} {name[0] + name[1:4] + 'ies'}"
        return f"{value} {name[0] + name[1:] + 's'}"
    return f"{value} {name[0] + name[1:]}"


def exact_change(user_total):
    if user_total == 0:
        print('no change')
        return None, None, None, None, None

    change_collection = calculate_change(user_total)

    for change_type in CHANGE_CONST:
        if change_collection.get(change_type) == None:
            change_collection[change_type] = 0

    return change_collection['dollar'], change_collection['quarter'], change_collection['dime'], change_collection['nickel'], change_collection['penny']


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val)

    if num_dollars > 0 and num_dollars != None:
        print(get_output(num_dollars, 'dollar'))

    if num_quarters > 0 and num_quarters != None:
        print(get_output(num_quarters, 'quarter'))

    if num_dimes > 0 and num_dimes != None:
        print(get_output(num_dimes, 'dime'))

    if num_nickels > 0 and num_nickels != None:
        print(get_output(num_nickels, 'nickel'))

    if num_pennies > 0 and num_pennies != None:
        print(get_output(num_pennies, 'penny'))
