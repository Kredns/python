#!/usr/bin/env python

import os
import re
import sys
from trello import TrelloApi

def find_todos(program):
    """Finds any occurrences of TODO and returns the entire line."""
    lines = None
    pattern = r'((TODO|todo).*)'
    with open(program, 'r') as f:
        # We do not care about the first line of the file because that should
        # be a shebang.
        f.readline()       
        lines = f.readlines()

    for line in lines:
        match = re.search(pattern, line)
        if match:
            yield match.group()

def main(filename):
    todos = find_todos(filename)
    for todo in todos:
        print todo

    TRELLO_APP_KEY = None
    with open('TRELLO_APP_KEY', 'r') as keyfile:
        TRELLO_APP_KEY = keyfile.readline()
    trello = TrelloApi(TRELLO_APP_KEY)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            main('test_todos.py')
    except KeyboardInterrupt:
        print
        sys.exit(0)
