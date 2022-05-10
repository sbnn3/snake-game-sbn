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

window.addch(food[0], food[1], '#')

# The snake game structure and logic
score = 0


ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    window.addnstr(0, 2, 'Score ', + str(score) + ' ')
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
    if s == 19: break
    if x == 0: break
    if x == 59: break

    if snake[0] in snake[1:]: break


    for c in snake: 
        window.addch(c[0], c[1], '-')

    window.addch(food[0], food[1], '#')

curses.endwin()
print(f"The final score is = {score}")
