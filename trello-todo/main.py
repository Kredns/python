#!/usr/bin/env python

import os
import re
import sys
from trello import TrelloClient

def strip_prefixes(string, prefixes):
    for prefix in prefixes:
        if string.startswith(prefix):
            return string[len(prefix):].lstrip()
    return string

def find_todos(program):
    """Finds any occurrences of TODO and returns the entire line."""
    lines = None
    # I know I could use a better regular expressiosn to get the perfect match
    # and remove the TODO's, but I'd rather do that via python instead of some
    # insane RegEx that I won't be able to understand a week from now.
    pattern = r'((TODO|todo).*)'
    with open(program, 'r') as f:
        lines = f.readlines()

    for line in lines:
        match = re.search(pattern, line)
        if match:
            yield match.group()

def main(filename):
    todos = find_todos(filename)
    prefixes = ['TODO:', 'TODO: ', 'todo:', 'todo: ', 'TODO ', 'todo ']
    for todo in todos:
        print strip_prefixes(todo, prefixes)

    #TRELLO_APP_KEY = None
    #AUTH_TOKEN = None
    #with open('TRELLO_APP_KEY', 'r') as k:
    #    TRELLO_APP_KEY = k.readline().strip()
    #with open('AUTH_TOKEN', 'r') as t:
    #    AUTH_TOKEN = t.readline().strip()

    #client = TrelloClient(TRELLO_APP_KEY, token=AUTH_TOKEN)
    #board = client.get_board('6yIqXMb5')
    #lists = board.get_lists('all')
    #todo_list = lists[0]

    #for todo in todos:
    #    todo_list.add_card(todo) 

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            main('test_todos.py')
    except KeyboardInterrupt:
        print
        sys.exit(0)
