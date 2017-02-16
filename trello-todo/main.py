#!/usr/bin/env python

import os
import re
import sys
from trello import TrelloClient

class TodoNotFoundException(Exception):
    pass

class TrelloTodo(object):
    def __init__(self, API_KEY, AUTH_TOKEN, board):
        self.prefixes = ['TODO:', 'TODO: ', 'todo:', 'todo: ', 'TODO ', 'todo ']
        self.client = TrelloClient(API_KEY, token=AUTH_TOKEN)
        board = self.client.get_board(board)
        lists = board.get_lists('all')
        self.todo_cards = self.__get_todo(lists)
        if not self.todo_cards:
            raise TodoNotFoundException

    def strip_prefixes(self, string):
        for prefix in self.prefixes:
            if string.startswith(prefix):
                return string[len(prefix):].lstrip()
        return string

    def __archive_all_cards(self):
        pass

    def __get_todo(self, lists):
        for l in lists:
            if 'TODO' in l.name.upper():
                return l
        return None
    
    def get_cards(self):
        cards = []
        for card in self.todo_cards.list_cards():
            cards.append(card.name)
        return cards
    
    def add_card(self, card):
        self.todo_cards.add_card(card)

def read_todo_from_file(filename):
    """Finds any occurrences of TODO and returns the entire line."""
    lines = None
    # I know I could use a better regular expressiosn to get the perfect match
    # and remove the TODO's, but I'd rather do that via python instead of some
    # insane RegEx that I won't be able to understand a week from now.
    pattern = r'((TODO|todo).*)'
    with open(filename, 'r') as f:
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
    trello = None
    try:
        trello = TrelloTodo(API_KEY, AUTH_TOKEN, board_id)
    except TodoNotFoundException:
        print 'Unable to find a TODO list on your Trello board.'
        sys.exit(1)

    todos = read_todo_from_file(filename)
    cards = trello.get_cards()

    for item in todos:
        item = trello.strip_prefixes(item)
        if item not in cards:
            trello.add_card(item)
    
if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        else:
            main('test_todos.py')
    except KeyboardInterrupt:
        print
        sys.exit(0)
