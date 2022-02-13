from enum import Enum
from multiprocessing.sharedctypes import Value
import os
import random
from time import sleep


class Items(Enum):
    # health potion which gives you 25 hp
    HEALTH_POTION = 1
    # increase damage for one round
    INCREASE_DAMAGE = 2
    # allows you to take no damage for one round
    UNTOUCHABLE = 3


class Rooms(Enum):
    CENTRAL_WING = 1
    NORTH_WING = 2
    WEST_WING = 3
    SOUTH_WING = 4
    EAST_WING = 5
    SOUTH_EAST_WING = 6
    NORTH_EAST_WING = 7
    DUNGEON = 8


class GameState:
    def __init__(self) -> None:
        self.level = 1

    def level_up(self, level):
        self.level += level
        return None

    def get_level(self):
        return self.level


class Player:
    def __init__(self, name: str, position: int, health: int) -> None:
        self.name: str = name
        self.position: int = position
        self.health: int = health
        self.items: list = []
        self.damage_adder: int = 0
        self.damage_adder_bool: bool = False
        self.untouchable: bool = False
        self.level = 1

    def __repr__(self) -> str:
        return self.name

    def raise_level(self, game_state: GameState) -> None:
        self.level = game_state.level
        return

    def item_drop(self, amount=1) -> None:
        for _ in range(0, amount):
            item_number = random.randint(1, 3)
            item = Items(item_number)
            self.items.append(item)
            print(f'\nYou received item: {self.get_item_details(item)}\n')
        return

    def get_health(self) -> int:
        return self.health

    def get_name(self) -> str:
        return self.name

    def increase_health(self, amount) -> None:
        self.health += amount
        return

    def decrease_health(self, amount) -> None:
        self.health -= amount
        return

    def get_item_details(self, item) -> str:
        if item == Items.HEALTH_POTION:
            return f'Health Potion - Use this to increase your health by {100 * self.level}'
        elif item == Items.INCREASE_DAMAGE:
            return 'Increase Damage - Use this to amplify your damage'
        elif item == Items.UNTOUCHABLE:
            return 'Untouchable - Used this to receive 0 damage from your opponent'

    def display_all_items(self) -> str:
        for index, item in enumerate(self.items):
            print(f'{index} - {self.get_item_details(item)}')
        print('99 - Cancel use item')

    def get_item_number(self) -> int:
        while True:
            item = int(input('\nSelect an item\n:'))

            if item == 99:
                return 99

            if item in range(0, len(self.items)):
                return item

            print('Did you choose the right number?')

    def attack_or_items(self) -> None:
        try:
            user_input = int(
                input('Would you like to:\n1. Attack\n2. Use item\n:'))

            if user_input == 1:
                return True

            if len(self.items) == 0:
                print('\nYou dont have any items yet, kill a demon!\n')
                return False

            self.display_all_items()

            item = self.get_item_number()

            if item == 99:
                return False

            self.player_item_use(self.items[item])
            self.items.pop(item)
            return True
        except ValueError as VALUE_ERROR:
            print(
                f"Error - {VALUE_ERROR}: input must be a number between 1 and 4, try again.")

    def player_item_use(self, item: Items):
        """Item use"""
        if item == Items.HEALTH_POTION:
            potion_ammount = 100 * self.level
            self.increase_health(potion_ammount)
            print(
                f'You have been giving 25 health.\nYour health is now {self.get_health()}\n')
        elif item == Items.INCREASE_DAMAGE:
            self.damage_adder = random.randint(50, 100) * self.level
            self.damage_adder_bool = True
            print('Increase damage for one round')
        elif item == Items.UNTOUCHABLE:
            self.untouchable = True
            print('Untouchable for one round')

    def round_item_use(self, type: Items):
        """During the round we check if any of the items have to be applied"""
        if type == Items.INCREASE_DAMAGE:
            if self.damage_adder_bool:
                self.damage_adder_bool = False
                return self.damage_adder
            return 0
        elif type == Items.UNTOUCHABLE:
            if self.untouchable:
                self.untouchable = False
                return True
            return False

    def random_health_increase(self, level) -> None:
        health = random.randint(80, 120) * level
        print(f'\nHealth increase by {health + 100}')
        self.increase_health(health)
        return


class Demon:
    def __init__(self, health) -> None:
        self.name = 'Demon'
        self.health = health

    def get_name(self) -> str:
        return self.name

    def get_health(self) -> int:
        return self.health

    def increase_health(self, amount) -> None:
        self.health += amount
        return

    def decrease_health(self, amount) -> None:
        self.health -= amount
        return


class King:
    def __init__(self) -> None:
        self.name = 'King'
        self.health = 10000

    def get_name(self) -> str:
        return self.name

    def get_health(self) -> int:
        return self.health

    def increase_health(self, amount) -> None:
        self.health += amount
        return

    def decrease_health(self, amount) -> None:
        self.health -= amount
        return


def initiate_fight(villain: object, player: Player, game_state: GameState) -> None:
    while True:
        os.system('cls')
        level = game_state.get_level()
        print(
            f'\n{player.get_name()} Health: {player.get_health()}\n{villain.get_name()} Health: {villain.get_health()}\n')
        move = player.attack_or_items()

        if not move:
            sleep(2)
            continue

        print(game_state.level)

        hit = random.randint(15 * level, 30 * level)

        damage_increase = player.round_item_use(Items.INCREASE_DAMAGE)
        hit += damage_increase

        print(f'{player.get_name()} is attacking the {villain.get_name()} for {hit}')
        villain.decrease_health(hit)

        if villain.health <= 0:
            if villain.name == 'King':
                print('You won the game! Congrats!')
                exit()
            print(f'\nYou won the fight!\n')

            player.increase_health(150)
            player.random_health_increase(level)
            player.item_drop(2)
            return

        hit = random.randint(15 * level, 30 * level)

        untouchable = player.round_item_use(Items.UNTOUCHABLE)

        if untouchable:
            hit = 0

        print(f'{villain.get_name()} is attacking the {player.get_name()} for {hit}')
        player.health -= hit
        player.decrease_health(hit)

        if player.get_health() <= 0:
            print('You lose...')
            exit()

        if villain.get_name() == 'King':
            game_level_up(game_state, player, 5)

        sleep(2)
        os.system('cls')


def get_room(room: Rooms) -> str:
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
    print(f'\nYou are in {get_room(current_room)}, and can move to:\n')
    for room in args[0]:
        print(f'{room.value}: {get_room(room)}')


def room_movement(player: Player):
    new_room = None
    room_possibilities = None

    if player.position == Rooms.CENTRAL_WING:
        room_possibilities = [Rooms.CENTRAL_WING, Rooms.NORTH_WING, Rooms.WEST_WING,
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

        except ValueError as VALUE_ERROR:
            print(
                f"Error - {VALUE_ERROR}: input must be a number between 1 and 4, try again.")


def check_if_demon_is_alive(demons: dict, player_position: Rooms) -> bool:
    for demon in demons:
        demon_room = Rooms(int(demon))
        demon_object: Demon = demons[demon]
        if demon_room == player_position and demon_object.health >= 100:
            return True, demon_object

    if player_position != Rooms.DUNGEON:
        print(f'\nYou killed the demon in {get_room(player_position)}\n')

    return False, None


def demons_get_stronger(demons: dict, level: int):
    health = random.randint(50, 80) * level
    for demon in demons:
        obj = demons[demon]
        if obj.health > 0:
            obj.health += health
    print(f'Demons grow stronger! Living demons gained {health} health')


def king_caution(check) -> bool:
    if not check:
        return True

    while True:
        answer = input(
            '\nYou have not killed all the demons, are you sure you want to enter the Dungeon and face the king? (y or n)\n:')

        if answer == 'y':
            print('Okay good luck!')
            return True

        if answer == 'n':
            print('Probably a good idea...')
            return False

        print('Not a valid answer, try again...')
        continue


def game_level_up(game_state: GameState, player: Player, level=1) -> None:
    game_state.level_up(level)
    player.raise_level(game_state)


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
    game_state = GameState()

    player.item_drop(5)

    print('Game is starting!')
    sleep(3)

    check, demon = check_if_demon_is_alive(demons, player.position)
    if check:
        initiate_fight(demon, player, game_state)
        demons_get_stronger(demons, game_state.level)
        game_level_up(game_state, player)

    while True:
        player_position = room_movement(player)

        check, demon = check_if_demon_is_alive(demons, player_position)
        if check:
            initiate_fight(demon, player, game_state)
            demons_get_stronger(demons, game_state.level)
            game_level_up(game_state, player)
        elif player_position == Rooms.DUNGEON:
            if king_caution(check):
                game_level_up(game_state, player)
                player.increase_health(1500)
                player.item_drop(4)
                initiate_fight(king, player, game_state)
                print('Game Over, you win!!! Congrats!')
                exit()
            player.position = Rooms.NORTH_WING


if __name__ == '__main__':
    main()
