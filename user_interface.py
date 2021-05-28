import random
from marketing_firm import MarketingFirm
from marketing_firm_creator import MarketingFirmCreator
from contestant import Contestant
from sweepstake import Sweepstake


# default menu for user to navigate application
def main_menu():
    print('\n\tWelcome to your Sweepstakes application.\n'
          '\t\tSelect <1> to set up your firm.\n'
          '\t\tSelect <2> to create a sweepstake.\n'
          '\t\tSelect <3> to register a contestant.\n'
          '\t\tSelect <4> to view registered contestants.\n')
    user_input = int(input('\t\t'))
    if user_input == 1:
        create_firm = MarketingFirmCreator()
        create_firm.set_up_firm()
    if user_input == 2:
        create_sweepstake = MarketingFirm(manager=None, name=None)
        create_sweepstake.create_sweepstakes()
    if user_input == 3:
        register_contestant = Sweepstake(name=None)
        register_contestant.register_contestant(contestant=None)
    if user_input == 4:
        view_contestants = Sweepstake(name=None)
        view_contestants.print_all_contestants()
    return user_input


def name_sweepstakes():
    input('Enter a name for the new sweepstake.')


# need to create key-value pairs to append to dictionary
def add_contestant():
    contestant = Contestant()
    contestant.first_name = input('First Name: ')
    contestant.last_name = input('Last Name: ')
    contestant.email = input('Email: ')
    contestant.registration_number = random.randrange(100000, 999999)
    print(f"{contestant.first_name} {contestant.last_name}'s registration number is {contestant.registration_number}")
    main_menu()
