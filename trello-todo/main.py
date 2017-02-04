#!/usr/bin/env python

import os
import sys

def main():
    with open('test_todos.py', 'r') as f:
        # We do not care about the first line of the file because that should
        # be a shebang.
        f.readline()       
        is_comment = False
        for line in f:
            if (line.upper().startswith('# TODO:') or 
                line.upper().startswith('#TODO:') or 
                line.upper().startswith('#TODO') or
                line.upper().startswith('# TODO')):
                print line[7:].strip('#TODO: ')
                is_comment = True
            else:
                if line.startswith('#'):
                    print line[2:].strip('# ')
                else:
                    is_comment = False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
        sys.exit(0)
