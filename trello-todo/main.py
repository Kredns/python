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

def main():
    todos = find_todos('test_todos.py')
    for todo in todos:
        print todo

    trello = TrelloApi(TRELLO_APP_KEY)
    trello.get_token_url('trello_todo', expires='30days', write_access=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        sys.exit(0)
