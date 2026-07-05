# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from .Logic.example import *
from .UserInterface.adapter import *
from ..interfaces.ILogic_Interface import *
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *


class LogicExampleInterface(ILogicInterface):

    def __init__(self):
        self.broker = None
        self.obj_logic = None

    def create(self, args, broker_utility_manager:utility_manager):
        print("Creating Example Logic Object")
        self.obj_logic: LogicExample = LogicExample(args, broker_utility_manager)

    def wait_for_completion(self):
        print("Wait For Completion", self.obj_logic.__class__.__name__)
        if self.obj_logic:
            print("Before Joining thread")
            self.obj_logic.get_thread_info().join()
            print("After Joining thread")




