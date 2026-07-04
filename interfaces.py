# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Logic.example import *
from UserInterface.adapter import *


g_obj_logic: LogicExample = None


def create(args, quotes_utility, nse_utility):
    print("Creating Example Logic Object")
    obj_ui_adapter_config = UserInterfaceAdapterConfig(args)
    obj_ui_adapter_login = UserInterfaceLogin(args)


def wait_for_completion():
    print("Wait For Completion", g_obj_logic.__class__.__name__)
    g_obj_logic.get_thread_info().join()

