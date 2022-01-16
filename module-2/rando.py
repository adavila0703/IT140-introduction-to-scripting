from collections import namedtuple


rando = [0, 1, 2]

print("hello", rando.sort())

#Example of nametuple
team_names = namedtuple('team_names', ['Rockets'])

woop = team_names("test")

woop.Rockets