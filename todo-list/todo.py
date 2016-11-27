#!/usr/bin/env python
# My solution to the following challenge: https://redd.it/39ws1x

import os
from datetime import date
from collections import defaultdict
from color import Color

home = os.path.expanduser('~')

class Todo:
    def __init__(self):
        self.items = defaultdict(list)
        self.__load_items()

    def __load_items(self):
        try:
            with open(home + '/.config/todo/list', 'r') as todo:
                for t in todo.readline():
                    # TODO: Need to figure out a way to store tags and items.
                    pass
        except IOError:
            print Color.ERROR + 'You do not have any items to load.' + Color.ENDC

    def __save_items(self):
        try:
            with open(home + '/.config/todo/list', 'w+') as todo:
                for (tag, items) in self.items.items():
                    todo.write(str(tag) + ':\n')
                    for item in items:
                        todo.write(' ' + item + '\n')
        except IOError:
            print Color.ERROR + 'Sorry there was a problem saving your file.' + Color.ENDC

    def add_item(self, item, tag):
        self.items[tag].append(item)
        self.__save_items()

    def remove_item(self, item, tag):
        if tag in self.items:
            if item in self.items[tag]:
                self.items[tag].remove(item)
            else:
                print Color.ERROR + "Item %s could not be found." % item + Color.ENDC
        else:
            print Color.ERROR + 'There is not tag named %s' % tag + Color.ENDC

    def print_all_items(self):
        for (tag, items) in self.items.items():
            print str(tag) + ':'
            for item in items:
                print ' ' + item
            print ''
        
if __name__ == '__main__':
    todo = Todo()
    # I actually need to do this, for real.
    todo.add_item('Get an oil change.', 'Car')
    todo.add_item('Plastidip my wheels.', 'Car')
    todo.add_item('Clean my room.', 'Housework')
    todo.print_all_items()
    todo.remove_item('Get an oil change.', 'Car')
    todo.remove_item('x', 'x')
    todo.remove_item('x', 'Housework')
    todo.print_all_items()
