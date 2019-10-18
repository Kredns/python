#!/usr/bin/env python3

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @staticmethod
    def apply(text, color, use_color=True):
        if use_color is False:
            return text
        return color + text + Color.END

def display_colors():
    print(Color.apply('This should be purple!', Color.PURPLE))
    print(Color.apply('This should be cyan!', Color.CYAN))
    print(Color.apply('This should be dark cyan (teal?)!', Color.DARKCYAN))
    print(Color.apply('This should be blue!', Color.BLUE))
    print(Color.apply('This should be green!', Color.GREEN))
    print(Color.apply('This should be yellow!', Color.YELLOW))
    print(Color.apply('This should be red!', Color.RED))
    print(Color.apply('This should be bold!', Color.BOLD))
    print(Color.apply('This should be underline!', Color.UNDERLINE))


if __name__ == '__main__':
    display_colors()
