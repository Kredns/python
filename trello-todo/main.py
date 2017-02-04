#!/usr/bin/env python

import os
import sys

# TODO: Read this line and add it to a card.
# Anything below the first line should be added as a comment.

#todo: Another test

# TODO yet another test

#TODO: Last test

# This should not be added.
def main():
    with open('main.py', 'r') as f:
        for line in f.readlines():
            if (line.upper().startswith('# TODO:') or 
                line.upper().startswith('#TODO:') or 
                line.upper().startswith('#TODO')):
                print line[7:].strip('#TODO: ')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        sys.exit(0)
