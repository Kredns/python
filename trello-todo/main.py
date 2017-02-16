#!/usr/bin/env python

import os
import re
import sys
from trello import TrelloClient

class TrelloTodo(object):
    def __init__(self, API_KEY, AUTH_TOKEN, board):
        self.prefixes = ['TODO:', 'TODO: ', 'todo:', 'todo: ', 'TODO ', 'todo ']
        self.client = TrelloClient(API_KEY, token=AUTH_TOKEN)
        self.board = self.client.get_board(board)
        lists = self.board.get_lists('all')
        # In order for this to work TODO has to be the first list on the board.
        lists.reverse()
        self.todo = lists.pop()

    def __strip_prefixes(self, string, prefixes):
        for prefix in prefixes:
            if string.startswith(prefix):
                return string[len(prefix):].lstrip()
        return string

    def __archive_all_cards(self):
        pass

    def find_todos(self, program):
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
    API_KEY = None
    AUTH_TOKEN = None
    with open('API_KEY', 'r') as k:
        API_KEY = k.readline().strip()
    with open('AUTH_TOKEN', 'r') as t:
        AUTH_TOKEN = t.readline().strip()

    board_id = '6yIqXMb5'
    todo = TrelloTodo(API_KEY, AUTH_TOKEN, board_id)
    for item in todo.find_todos(filename):
        print item

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            main('test_todos.py')
    except KeyboardInterrupt:
        print
        sys.exit(0)
