'''
Car's information:
   Model year: 2011
   Purchase price: 18000
   Current value: 5770

'''


# class Car:
#     def __init__(self):
#         self.model_year = 0
#         self.purchase_price = 0
#         self.current_value = 0

#     def print_info(self):
#         print(
#             f"Car's information:\n   Model year: {self.model_year}\n   Purchase price: {self.purchase_price}\n   Current value: {self.current_value}")

#     def calc_current_value(self, current_year):
#         depreciation_rate = 0.15
#         # Car depreciation formula
#         car_age = current_year - self.model_year
#         self.current_value = round(
#             self.purchase_price * (1 - depreciation_rate) ** car_age)


# if __name__ == "__main__":
#     year = int(input())
#     price = int(input())
#     current_year = int(input())

#     my_car = Car()
#     my_car.model_year = year
#     my_car.purchase_price = price
#     my_car.calc_current_value(current_year)
#     my_car.print_info()


'''
8.10 LAB: Winning team (classes)
Complete the Team class implementation. For the instance method get_win_percentage(), the formula is:
team_wins / (team_wins + team_losses)

Note: Use floating-point division.

Ex: If the input is:

Ravens
13
3 
where Ravens is the team's name, 13 is the number of team wins, and 3 is the number of team losses, the output is:

Congratulations, Team Ravens has a winning average!
If the input is Angels 80 82, the output is:

Team Angels has a losing average.

'''


class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
