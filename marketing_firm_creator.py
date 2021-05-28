import user_interface
from marketing_firm import MarketingFirm
from sweepstakes_stack_manager import SweepStakesManager
from sweepstakes_queue_manager import SweepstakesQueueManager


class MarketingFirmCreator:
    def __init__(self):
        # Marketing firm required parameters passed through--unsure how to treat w/ out =None
        self.new_firm = MarketingFirm(manager=None, name=None)

    def set_up_firm(self):
        self.new_firm.name = input('Please enter the name of your firm: ')
        self.choose_manager_type()
        user_interface.main_menu()

    def choose_manager_type(self):
        self.new_firm.manager = int(input('Enter <1> for Stack Manager.\n'
                                          'Enter <2> for Queue Manager.\n'))
        if self.new_firm.manager == 1:
            self.new_firm.manager = SweepStakesManager()
            print('Your firm will run a Stack Manager.')
        if self.new_firm.manager == 2:
            self.new_firm.manager = SweepstakesQueueManager()
            print('Your firm will run a Queue Manager.')
        return self.new_firm
