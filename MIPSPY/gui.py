import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    code_pad = curses.newpad(100, 70)
    register_pad = curses.newpad(32, 60)
    memory_pad = curses.newpad(32, 60)
    controls_win = curses.newwin(3, 130, 35, 0)

    i = 0
    while(i < 100):
        code_pad.refresh(i, 1, 0, 0, 35, 75)
        register_pad.refresh(1, 1, 0, 75, 17, 130)
        memory_pad.refresh(1, 1, 17, 75, 35, 130)

        try:
            key = stdscr.getkey()
        except:
            key = None

        #view next row
        if key == "KEY_DOWN":
            i += 1
        elif key == "KEY_UP":
            i -= 1
        elif key == "KEY_ESC":
            break
        else:
            pass

    stdscr.refresh()
    stdscr.getch()

wrapper(main)