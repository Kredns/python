#!/usr/bin/env python
# My solution to the following challenge: https://redd.it/39ws1x

import os
from datetime import date
from collections import defaultdict

home = os.path.expanduser('~')

class Todo:
    def __init__(self):
        self.items = defaultdict(list)

    def __load_items(self):
        try:
            with open(home + '/.config/todo/list', 'r') as todo:
                for item in todo.readline():
                    # TODO: Need to figure out a way to store tags and items.
                    pass
        except IOError:
            print 'You do not have any items to load.'

    def __save_items(self):
        try:
            with open(home + '/.config/todo/list', 'w') as todo:
                # TODO: Implement saving items.
                pass

    def add_item(self, item, tag):
        self.items[tag].append(item)

    def remove_item(self, item, tag):
        if tag in self.items:
            if item in self.items[tag]:
                self.items[tag].remove(item)
            else:
                print "Item %s could not be found." % item
        else:
            print 'There is not tag named %s' % tag

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
