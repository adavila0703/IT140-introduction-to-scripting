from enum import Enum
import os
import random
from time import sleep


class Player:
    def __init__(self, name, position, health) -> None:
        self.name = name
        self.position = position
        self.health = health


class Demon:
    def __init__(self, health) -> None:
        self.name = 'Demon'
        self.health = health
        self.item = random.randint(50, 100)


class King:
    def __init__(self) -> None:
        self.name = 'King'
        self.health = 1000


class Rooms(Enum):
    CENTRAL_WING = 1
    NORTH_WING = 2
    WEST_WING = 3
    SOUTH_WING = 4
    EAST_WING = 5
    SOUTH_EAST_WING = 6
    NORTH_EAST_WING = 7
    DUNGEON = 8


def initiate_fight(villain: object, player: Player, level: int) -> None:
    os.system('cls')
    while True:
        hit = random.randint(5 * level, 20 * level)
        print(f'{player.name} is attacking the {villain.name} for {hit}')
        villain.health -= hit

        print(
            f'\n{player.name} Health: {player.health}\n{villain.name} Health: {villain.health}\n')

        if villain.health <= 0:
            if villain.name == 'King':
                print('You won the game! Congrats!')
                exit()
            print(
                f'You won the fight! You gained {100 + villain.item} health!')
            player.health += villain.item + 100
            return

        hit = random.randint(5 * level, 10 * level)
        print(f'{villain.name} is attacking the {player.name} for {hit}')
        player.health -= hit

        print(
            f'\n{player.name} Health: {player.health}\n{villain.name} Health: {villain.health}\n')

        if player.health <= 0:
            print('You lose...')
            exit()

        sleep(1)
        os.system('cls')


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
    return new_room


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


def check_if_demon_is_alive(demons: dict, player_position: Rooms) -> bool:
    for demon in demons:
        demon_room = Rooms(int(demon))
        demon_object: Demon = demons[demon]
        if demon_room == player_position and demon_object.health >= 100:
            return True, demon_object
    return False, None


def demons_get_stronger(demons: dict):
    print('Demons grow stronger')
    for demon in demons:
        obj = demons[demon]
        if obj.health > 0:
            obj.health += random.randint(50, 80)


def main():
    player = Player('Angel', Rooms.CENTRAL_WING, 100)
    demons = {
        '1': Demon(100),
        '2': Demon(100),
        '3': Demon(100),
        '4': Demon(100),
        '5': Demon(100),
        '6': Demon(100),
        '7': Demon(100),
    }
    king = King()
    level = 1

    check, demon = check_if_demon_is_alive(demons, player.position)
    if check:
        initiate_fight(demon, player, level)

    demons_get_stronger(demons)

    while True:
        player_position = room_movement(player)

        check, demon = check_if_demon_is_alive(demons, player_position)
        if check:
            initiate_fight(demon, player, level)

        if not check and player_position == Rooms.DUNGEON:
            initiate_fight(king, player, level)

        level += 0.5


if __name__ == '__main__':
    main()
