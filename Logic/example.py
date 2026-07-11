# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect - Historical Data

"""
from enum import Enum
import traceback
import threading

from BusinessLogic.interfaces.ILogic import *
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *
from BusinessLogic.example_logic.UserInterface.adapter.login.login import *
from BusinessLogic.example_logic.UserInterface.adapter.config.config import *
from Utility.nse_utility import *

#logic class
class LogicExample(ILogic):
    def __init__(self, args, broker_utility_manager:utility_manager, quotes_utility:QuoteUtility):
        # initialization from arguments
        self.logic_name = "LogicExample"
        self.obj_utility_manager = broker_utility_manager
        self.obj_ui_adapter_login:UserInterfaceAdapterLogin = UserInterfaceAdapterLogin(args)
        self.obj_ui_adapter_config:UserInterfaceAdapterConfig = UserInterfaceAdapterConfig(args)
        self.order_utility = self.obj_utility_manager.get_utility_object(self.obj_ui_adapter_login.get_data())
        self.trade_utility = self.obj_utility_manager.get_utility_object(self.obj_ui_adapter_login.get_data())
        self.option_chain_utility = self.obj_utility_manager.get_utility_object(self.obj_ui_adapter_login.get_data())
        self.nse_utility = nse_utitlity()
        self.quotes_utility: QuoteUtility = quotes_utility
        self.nifty_future: str = ""
        self.config_data = self.obj_ui_adapter_config.get_data()

        #pre requisite complete eent
        self.pre_requisite_complete_event = threading.Event()

        self.day_preset = 0


        #update the trade date
        trade_day = date.today() - timedelta(self.day_preset)
        date_str = trade_day.strftime("%d-%m-%Y")

        #pre requisite start time
        self.pre_requisite_start_time = (datetime.now() + timedelta(seconds=10)).strftime('%H:%M:%S')

        #start time
        self.execution_start_time = "09:15:00"

        #stop time
        self.execution_stop_time = "15:00:00"


        #start the thread
        self.pre_requisite_thread = threading.Thread(target=self.pre_requisite_thread_handler)
        self.execute_thread = threading.Thread(target=self.execute)
        self.exit_thread = threading.Thread(target=self.exit_execution_thread)
        self.isFirstTime = True

        # start the prerequisite thread
        self.pre_requisite_thread.start()
        # start the thread
        self.execute_thread.start()
        # start the close order thread
        #start exit thread
        self.exit_thread.start()

    def get_broker_utility(self):
        return self.trade_utility

    def pre_requisite_thread_handler(self):
        print("Inside pre-requisite thread")
        #print(self.__class__.__name__, ":", "Prerequsite Thread", self.pre_requisite_start_time, type(self.pre_requisite_start_time))
        self.pre_requisite_complete_event.set()
        print("Exiting pre-requisite thread")

    def execute(self):
        self.pre_requisite_complete_event.wait()
        print(self.__class__.__name__, ":", "Execution Started", self.config_data.start_time)

    def exit_execution_thread(self):
        print(self.__class__.__name__, ":", "Start of Exiting Thread")
        #end_time = datetime.strptime(self.config_data.end_time, '%H:%M:%S')
        #i_sleep_time = (end_time - datetime.now()).seconds
        i_sleep_time = 10
        print(self.__class__.__name__, ":", "Exit sleep time: ", i_sleep_time)
        time.sleep(i_sleep_time)
        self.quotes_utility.stop()
        self.quotes_utility.get_thread_info().join()
        print(self.__class__.__name__, ":", "End of Exiting Thread")

    def get_thread_info(self):
        return self.exit_thread


