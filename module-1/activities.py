
# def product(nums: list):
#     output = 1

#     for num in nums:
#         output *= num 

#     return output


# nums = []

# for num in range(0, 3):
#     nums.append(int(input()))

# print(product(nums))

# rando = "If Fred is from a part of France, then of course Fred's French is good."

# out = rando.count('f') + rando.count('F')

# print(out)

"""
Write two statements to read in values for my_city followed by my_state. Do not provide a prompt. 
Assign log_entry with current_time, my_city, and my_state. Values should be separated by a space. 
Sample output for given program if my_city is Houston and my_state is Texas:

2014-07-26 02:12:18: Houston Texas

"""

current_time = '2014-07-26 02:12:18:'
my_city = 'Huston'
my_state = 'Texas'
log_entry = ''

current_time += ' ' + my_city + ' ' + my_state

log_entry = current_time

print(log_entry)