import curses
from random import randint

# The snake game window setup
curses.initscr()
window = curses.newwin(25, 75, 0, 0)
window.keypad(1)
curses.noecho()
window.border(0)
window.nodelay(1)

# The snake and food variables
snake = [(4, 10), (4, 9), (4,8)]
food = (10, 20)

window.addch(food[0], food[1], '#')

# The snake game structure and logic
score = 0


ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    window.addstr(0, 2, 'Score ' + str(score) + ' ')
    window.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

    last_key = key
    event = window.getch()
    key = event if event != -1 else last_key

    if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = last_key

    # Coordinates Calculation
    s = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_UP:
        s -= 1
    if key == curses.KEY_DOWN:
        s += 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (s, x))

    # Check if snake hits the border and if runs over
    if s == 0: break
    if s == 24: break
    if x == 0: break
    if x == 74: break

    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1, 23), randint(1, 73))
            if food in snake: 
                food = ()

        window.addch(food[0], food[1], '#')
    else: 
        last = snake.pop()
        window.addch(last[0], last[1], ' ')

    window.addch(snake[0][0], snake[0][1], '-')

curses.endwin()
print(f"The final score is = {score}")
