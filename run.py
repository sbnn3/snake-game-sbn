import curses

# The snake game window setup
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
window.border(0)
window.nodelay(1)

# The snake and food variables
snake = [(4, 10), (4, 9), (4,8)]
food = (10, 20)

# The snake game structure and logic
score = 0

while True:
    event = window.getch()

    for c in snake: 
        window.addch(c[0], c[1], '-')

    window.addch(food[0], food[1], '#')

curses.endwin()
print(f"The final score is = {score}")
