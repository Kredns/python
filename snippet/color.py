#!/usr/bin/env python

class Color:
    WARNING = '\033[96m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m' 
    REDB = '\033[41m'
    GREEN = '\033[32m' 

    def __init__(self, use_color=True):
        self.use_color = use_color

    def colorize(self, text, color):
        if self.use_color is False:
            return text
        return color + text + Color.ENDC
