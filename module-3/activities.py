# bonus_val = 5

# if bonus_val < 12:
#    num_items = 100
# else:
#    num_items = 200

# print(num_items)


'''
If user_age is greater than 62, assign item_discount with 15. Else, assign item_discount with 0.
'''

# if user_age > 62:
#     item_discount = 15
# else:
#     item_discount = 0


'''
If num_people is greater than 10, execute group_size = 2 * group_size. Otherwise, execute group_size = 3 * group_size and num_people = num_people - 1.
'''
# num_people = 11
# group_size = 5

# if num_people > 10:
#     group_size *= 2
# else:
#     group_size *= 3
#     num_people -= 1


# if num_people > 10:
#    group_size = 2 * group_size
# else:
#    group_size = 3 * group_size
#    num_people = num_people - 1

# print(group_size, num_people)


'''If num_players is greater than 11, execute team_size = 11. Otherwise, execute team_size = num_players. Then, no matter the value of num_players, execute team_size = 2 * team_size.'''

# if num_players > 11:
#     team_size = 11
# else:
#     team_size = num_players

# team_size = 2 * team_size


# user_tickets = int(input())
# num_tickets = 0

# if user_tickets < 5:
#     num_tickets = 1
# else:
#     user_tickets = num_tickets

# print('Value of num_tickets:', num_tickets)


'''
Write an if-else statement with multiple branches.
If year is 2101 or later, print "Distant future" (without quotes). Otherwise, if year is 2001 or greater, print "21st century". 
Otherwise, if year is 1901 or greater, print "20th century". Else (1900 or earlier), print "Long ago".

Sample output with input: 1776
Long ago
'''

# year = int(input())

# if year >= 2101:
#     print("Distant future")
# elif year >= 2001:
#     print("21st century")
# elif year >= 1901:
#     print("20th century")
# else:
#     print("Long ago")


'''
Write multiple if statements. 
If car_year is 1969 or earlier, print "Few safety features." 
If 1970 or later, print "Probably has seat belts." 
If 1990 or later, print "Probably has antilock brakes." 
If 2000 or later, print "Probably has airbags." End each phrase with a period and a newline.

Sample output for input: 1995
Probably has seat belts.
Probably has antilock brakes.
'''

# car_year = int(input())

# ''' Your solution goes here '''

# if car_year <= 1969:
#     print("Few safety features")

# if car_year >= 1970:
#     print("Probably has seat belts.")

# if car_year >= 1990:
#     print("Probably has antilock brakes." )

# if car_year >= 2000:
#     print("Probably has airbags.")

# num_users = int(input())
# update_direction = int(input())

# num_users = num_users + 1 if update_direction == 3 else num_users - 1

# print('New value is:', num_users)

print('hello')
print('woop')
print('hello', end=' ')
print('woop')
print('woop')
print('woop')
print('woop')
print('woop')
