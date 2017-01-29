#!/usr/bin/env python
import os, sys
import curses

class fileman(object):
    def __init__(self, screen):
        self.screen = screen
        self.MAX_ROWS, self.MAX_COLS = screen.getmaxyx()
        self.screen.clear()
        self.screen.border(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def show_files(self, path):
        row = 1
        col = 1
        for filename in os.listdir(path):
            if row is 1 and col is 1:
                self.screen.addstr(row, col, filename, curses.color_pair(1))
            else:
                self.screen.addstr(row, col, filename)
            row = row + 1
            if row == self.MAX_ROWS - 1:
                row = 1
                col = col + 30
        self.screen.refresh()
        opt = screen.getch()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        path = os.getcwd()
    else:
        path = sys.argv[1]

    try:
        screen = curses.initscr()
        curses.start_color()
        window = fileman(screen)
        window.show_files(path)
    except Exception as e:
        print e
        curses.endwin()
    finally:
        curses.endwin()

