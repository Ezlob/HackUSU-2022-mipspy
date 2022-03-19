import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,20,"hello world")
    stdscr.refresh()
    stdscr.getch()
wrapper(main)