from enum import Enum


class Player:
    def __init__(self, name, position, health) -> None:
        self.name = name
        self.position = position
        self.health = health


class Demon:
    def __init__(self) -> None:
        self.name
        self.position
        self.health
        self.item


class King:
    def __init__(self) -> None:
        self.name
        self.position
        self.health


class Rooms(Enum):
    CENTRAL_WING = 1
    NORTH_WING = 2
    WEST_WING = 3
    SOUTH_WING = 4
    EAST_WING = 5
    SOUTH_EAST_WING = 6
    NORTH_EAST_WING = 7
    DUNGEON = 8


class Movement(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def drop_item():
    pass


def initiate_fight():
    pass


def get_room(room) -> str:
    if room == Rooms.CENTRAL_WING:
        return 'Central Wing'
    elif room == Rooms.NORTH_WING:
        return 'North Wing'
    elif room == Rooms.WEST_WING:
        return 'West Wing'
    elif room == Rooms.SOUTH_WING:
        return 'South Wing'
    elif room == Rooms.EAST_WING:
        return 'East Wing'
    elif room == Rooms.SOUTH_EAST_WING:
        return 'South East Wing'
    elif room == Rooms.NORTH_EAST_WING:
        return 'North East Wing'
    elif room == Rooms.DUNGEON:
        return 'Dungeon'


def display_room_possibilities(current_room: Rooms, *args):
    print(f'You are in {get_room(current_room)}, and can move to:')
    print("rooms", args)
    for room in args[0]:
        print(f'{room.value}: {get_room(room)}')


def room_movement(player: Player):
    new_room = None
    room_possibilities = None

    if player.position == Rooms.CENTRAL_WING:
        room_possibilities = [Rooms.NORTH_WING, Rooms.WEST_WING,
                              Rooms.SOUTH_WING, Rooms.EAST_WING]
    elif player.position == Rooms.NORTH_WING:
        room_possibilities = [Rooms.DUNGEON, Rooms.CENTRAL_WING]
    elif player.position == Rooms.WEST_WING:
        room_possibilities = [Rooms.CENTRAL_WING]
    elif player.position == Rooms.SOUTH_WING:
        room_possibilities = [Rooms.CENTRAL_WING, Rooms.SOUTH_EAST_WING]
    elif player.position == Rooms.EAST_WING:
        room_possibilities = [Rooms.CENTRAL_WING, Rooms.NORTH_EAST_WING]
    elif player.position == Rooms.NORTH_EAST_WING:
        room_possibilities = [Rooms.EAST_WING]
    elif player.position == Rooms.SOUTH_EAST_WING:
        room_possibilities = [Rooms.SOUTH_WING]
    elif player.position == Rooms.DUNGEON:
        room_possibilities = [Rooms.NORTH_WING]

    display_room_possibilities(player.position, room_possibilities)
    new_room = movement_option(room_possibilities)

    player.position = new_room


def movement_option(*args) -> Rooms:
    while True:
        try:
            room = Rooms(int(input("\nChoose a room: ")))
            if room not in args[0]:
                print('\nRoom not availible try again...\n')
                continue
            return room

        except ValueError as ve:
            print(
                f"Error - {ve}: input must be a number between 1 and 4, try again.")


def main():
    player = Player('Angel', Rooms.CENTRAL_WING, 100)

    while True:
        room_movement(player)


if __name__ == '__main__':
    main()
