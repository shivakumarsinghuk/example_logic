# -*- coding: utf-8 -*-
"""
Zerodha Kite Connect - Historical Data

"""
from enum import Enum
import traceback
import threading


#logic class
class LogicExample:
    def __init__(self, order_utility, \
                 trade_utility, option_chain_utility, quotes_utility, nse_utility):
        # initialization from arguments
        self.logic_name = "LogicORBNiftyIndex"
        self.order_utility = order_utility
        self.trade_utility = trade_utility
        self.option_chain_utility = option_chain_utility
        self.nse_utility = nse_utility
        self.quotes_utility: QuoteUtility = quotes_utility
        self.nifty_future: str = ""

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

    def pre_requisite_thread_handler(self):
        print(self.__class__.__name__, ":", "Prerequsite Thread", self.pre_requisite_start_time, type(self.pre_requisite_start_time))
        self.pre_requisite_complete_event.set()

    def execute(self):
        self.pre_requisite_complete_event.wait()
        self.__prerequisite()
        print(self.__class__.__name__, ":", "Execution Started", self.config_data.start_time)

    def exit_execution_thread(self):
        print(self.__class__.__name__, ":", "Start of Exiting Thread")
        end_time = datetime.strptime(self.config_data.end_time, '%H:%M:%S')
        i_sleep_time = (end_time - datetime.now()).seconds
        time.sleep(i_sleep_time)
        print(self.__class__.__name__, ":", "End of Exiting Thread")

    def get_thread_info(self):
        return self.exit_thread


