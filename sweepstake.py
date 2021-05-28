import random
import user_interface
from contestant import Contestant


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestant_list = {}
        self.random_winner = Contestant()

# is not appending to contestant_list correctly
    def register_contestant(self, contestant):
        print("Enter the new contestant's info")
        new_contestant = user_interface.add_contestant()
        self.contestant_list[new_contestant] = contestant

# need to pick winner by registration_number key once register_contestant method is working
    def pick_winner(self):
        contestant_list = list(self.contestant_list)
        self.random_winner = random.choice(contestant_list)
        return self.random_winner

# need to insert random_winner into method to print info--make method 'not static'
    def print_contestant_info(self, contestant):
        print(f'\nFirst Name: {contestant.first_name}'
              f'\nLast Name: {contestant.last_name}'
              f'\nEmail: {contestant.email}'
              f'\nRegistration Number: {contestant.registration_number}')

# need to
    def print_all_contestants(self):
        contestant_list = self.contestant_list.items()
        for contestant in contestant_list:
            try:
                print(contestant)
            except:
                print('There are no contestants in this sweepstakes.')
