import curses

# The snake game window setup
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
window.border(0)
window.nodelay(1)