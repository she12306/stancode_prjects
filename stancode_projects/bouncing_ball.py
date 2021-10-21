"""
File: bouncing.ball
Name: Heather Ou
-------------------------
Click the mouse to make the ball bounce.
Limited to three clicks.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
n = 0  # The number of clicks


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)

    # ball
    ball.filled = True
    window.add(ball, START_X, START_Y)


def bounce(m):
    dx = VX
    dy = 0
    global n

    if ball.x == START_X and ball.y == START_Y and n < 3:
        while True:
            dy += GRAVITY
            ball.move(dx, dy)
            pause(DELAY)
            if ball.y + SIZE >= window.height and dy >= 0:
                dy *= -REDUCE
            if ball.x >= window.width:
                ball.x = START_X
                ball.y = START_Y
                n += 1
                break


if __name__ == "__main__":
    main()
