from cmath import rect
import curses
from curses import wrapper
from curses.textpad import rectangle

def main(stdscr):
    stdscr.clear()
    rectangle(stdscr, 0, 0, 38, 130)
    rectangle(stdscr, 0, 0, 35, 75)
    rectangle(stdscr, 0, 10, 17, 10)
    stdscr.refresh()
    stdscr.getch()



wrapper(main)