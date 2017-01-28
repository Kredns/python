#!/usr/bin/env python
import os, sys
import curses

def show_files(screen, path):
    row = 0
    col = 1
    for filename in os.listdir(path):
        if row is 1 and col is 1:
            screen.addstr(row, col, filename, curses.color_pair(1))
        else:
            screen.addstr(row, col, filename)
        row = row + 1
        if row == MAX_ROWS - 1:
            row = 1
            col = col + 30
    screen.refresh()

def main(screen):
    global MAX_ROWS, MAX_COLS
    MAX_ROWS, MAX_COLS = screen.getmaxyx()
    screen.clear()
    screen.border(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    path = sys.argv[1]
    show_files(screen, path)
    opt = screen.getch()
    curses.endwin()

if __name__ == '__main__':
    try:
        screen = curses.initscr()
        curses.start_color()
        main(screen)
    except Exception as e:
        print e
        curses.endwin()

