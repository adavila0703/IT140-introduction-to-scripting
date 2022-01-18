# car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}

# # Add the key Tesla with value USA to car_makers
# # Modify the car maker of Fiat to Italy

# ''' Your solution goes here '''

# print('Acura made in', car_makers['Acura'])
# print('Fiat made in', car_makers['Fiat'])
# print('Tesla made in', car_makers['Tesla'])


x = ['images', 'google', 'com']

my_str = '.'.join(x)

print(my_str)

from collections import namedtuple

Player = namedtuple('Player', ['name', 'number', 'position', 'team'])

cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')

print(cam.name + '(#' + cam.number + ')' + ' is a ' + cam.position + ' for the ' + cam.team + '.')
print(lebron.name + '(#' + lebron.number + ')' + ' is a ' + lebron.position + ' for the ' + lebron.team + '.')

rando = 3
woop = 1

if (rando > 3) or (woop < 4):
    pass
