#!/usr/bin/env python

class Color:
    WARNING = '\033[96m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    REDB = '\033[41m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m' 
    GREEN = '\033[32m' 

    @staticmethod
    def colorize(text, color, use_color=True):
        if use_color is False:
            return text
        return color + text + Color.ENDC
