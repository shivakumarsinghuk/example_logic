# -*- coding: utf-8 -*-
"""
login_types.py
"""
import sys
from ...gsheet.config import *


class UserInterfaceAdapterConfig:

    def __init__(self, args):
        if "gsheet" == args.userinterface:
            self.ui_object = UserInterfaceConfig(args.key)

    def get_data(self):
        return self.ui_object.data


