#!/usr/bin/env python
# My solution to the following challenge: https://redd.it/39ws1x

# I'm probably going to have to redo this whole thing to use a dictornary.

from datetime import date

class Todo:
    def __init__(self):
        self.items = {}

    def add_item(self, item, tag):
        self.items[tag] = item

    def remove_item(self, item, tag):
        pass

    def print_all_items(self):
        for item in self.items:
            pass

    def __str__(self):
        return str(self.items)
        
if __name__ == '__main__':
    todo = Todo()
    # I actually need to do this, for real.
    todo.add_item('Get an oil change.', 'Car')
    print todo
