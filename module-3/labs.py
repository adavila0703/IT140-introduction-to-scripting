'''
3.11 LAB: Smallest number
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
'''

# lst = []

# for _ in range(0, 3):
#     lst.append(int(input()))

# print(min(lst))


'''
3.12 LAB: Seasons
Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11
the output is:

Spring
In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65
the output is:

Invalid 
The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
'''

# from datetime import datetime, date, timedelta
# def get_months() -> dict:
#     months = {}
#     month_nums = list(range(1, 13))

#     for num in month_nums:
#         months[f"{datetime.strptime(str(num), '%m').strftime('%B')}".lower(
#         )] = num

#     return months


# def list_of_dates(start: date, end: date) -> dict:
#     """Returns a list of dates in a dictionary"""
#     delta = end - start
#     dates = {}
#     for days in range(delta.days + 1):
#         dates[f'{start + timedelta(days=days)}'] = ''
#     return dates


# def generate_seasons() -> dict:
#     seasons = {
#         'Spring': list_of_dates(date(datetime.now().year, 3, 20), date(datetime.now().year, 6, 20)),
#         'Summer': list_of_dates(date(datetime.now().year, 6, 21), date(datetime.now().year, 9, 21)),
#         'Autumn': list_of_dates(date(datetime.now().year, 9, 22), date(datetime.now().year, 12, 20)),
#         'Winter': list_of_dates(date(datetime.now().year, 12, 21), date(datetime.now().year + 1, 3, 19)),
#     }
#     return seasons


# def main():
#     user_input = {
#         'month': input().strip().lower(),
#         'day': int(input()),
#     }

#     months = get_months()

#     if not user_input['month'] in months:
#         print('Invalid')
#         return

#     seasons = generate_seasons()

#     year = datetime.now().year

#     if user_input['month'] in ['january', 'february', 'march']:
#         year += 1

#     try:
#         user_date = str(
#             date(year, months[user_input['month']], user_input['day']))
#     except ValueError:
#         print('Invalid')

#     for season in seasons:
#         if not seasons[season].get(user_date) == None:
#             print(season)


# if __name__ == '__main__':
#     main()


'''
3.13 LAB: Exact change
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. 
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0 
(or less than 0), the output is:

No change 
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes

'''


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
            return f"{value} {name[0].upper() + name[1:4] + 'ies'}"
        return f"{value} {name[0].upper() + name[1:] + 's'}"
    return f"{value} {name[0].upper() + name[1:]}"


def main():
    money = int(input())

    if money == 0:
        print('No change')
        return

    change_collection = calculate_change(money)

    for change in change_collection:
        print(get_output(change_collection[change], change))


if __name__ == '__main__':
    main()
