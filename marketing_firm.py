# import user_interface
from sweepstake import Sweepstake


class MarketingFirm:

    def __init__(self, manager, name):
        self.manager = manager
        self.name = name

    # not entirely sure how to create
    def create_sweepstakes(self):
        sweepstakes_name = input("Enter the name of your sweepstakes: ")
        sweepstakes = Sweepstake(sweepstakes_name)
        sweepstakes.contestant_list = {}
