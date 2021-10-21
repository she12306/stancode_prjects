"""
File: draw_line
Name: Heather Ou
-------------------------
Click the mouse to create lines.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
circle = GOval(SIZE, SIZE)

# control: circle or line
switch = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(m):
    global switch
    switch *= -1
    if switch < 0:
        window.add(circle, m.x - SIZE/2, m.y - SIZE/2)
    else:
        window.remove(circle)
        line = GLine(circle.x, circle.y, m.x, m.y)
        window.add(line)


if __name__ == "__main__":
    main()
