#!/usr/bin/env python
# My solution to the following challenge: https://redd.it/39ws1x

from datetime import date
from collections import defaultdict

class Todo:
    def __init__(self):
        self.items = defaultdict(list)

    def add_item(self, item, tag):
        self.items[tag].append(item)

    def remove_item(self, item, tag):
        self.items[tag].remove(item)

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
    todo.print_all_items()
