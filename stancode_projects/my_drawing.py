"""
File: my_drawing.py
Name: Heather Ou
----------------------
Let' s join the most popular "popcat.click"!
Clicking your mouse will open and close the cat’s mouth, and will count at the same time.
Clicking 100 times will change the ranking.
Let Taiwan win another gold medal!!!

Little Secret:
Click the left eye of the cat, you can accumulate the number of times faster.
However, if you click the cat’s eye too many times, the cat will get mad.
Do it at your own risk.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousereleased
from campy.gui.events.timer import pause

WIN_NUM = 100
ANGRY_NUM = 10

# background
window = GWindow(500, 500, title="POPCAT.CLICK")

# score
n = 0
eye_n = 0  # click eye num
score = GLabel(f"{n}")

# open mouth
pop = GOval(120, 120)


def main():
    """
    Set scenes, draw cat and leaderboard.
    Click event: Cat's mouth will open.
    Release event: Cat's mouth will close.
    Click more than 100 times, Taiwan’s ranking will rise from 2nd to 1st.
    """
    setting()
    draw_cat()
    second_place()  # Original ranking
    onmouseclicked(click)
    onmousereleased(release)


def setting():
    # background
    bg = GRect(window.width, window.height)
    bg.filled = True
    bg.fill_color = "tan"
    bg.color = "tan"
    window.add(bg)

    # title
    title = GLabel('POPCAT')
    title.font = 'Courier-70-bold'
    window.add(title, (window.width - title.width) / 2, 100)

    # score
    score.font = "Courier-30-bold"
    window.add(score, (window.width - score.width) / 2, 140)


def draw_cat():
    # body
    body = GPolygon()
    body.add_vertex((100, 500))
    body.add_vertex((160, 350))
    body.add_vertex((100, 180))
    body.add_vertex((180, 210))
    body.add_vertex((270, 190))
    body.add_vertex((300, 150))
    body.add_vertex((360, 300))
    body.add_vertex((340, 360))
    body.add_vertex((350, 500))
    body.filled = True
    body.fill_color = 'linen'
    body.color = 'black'
    window.add(body)

    # pattern
    pattern = GPolygon()
    pattern.add_vertex((160, 350))
    pattern.add_vertex((132, 270))
    pattern.add_vertex((210, 280))
    pattern.filled = True
    pattern.fill_color = 'darkgrey'
    pattern.color = 'darkgrey'
    window.add(pattern)

    # eyes
    eye_left = GOval(25, 25)
    eye_left.filled = True
    eye_left.fill_color = "black"
    window.add(eye_left, 210, 220)

    eye_right = GOval(25, 25)
    eye_right.filled = True
    eye_right.fill_color = "black"
    window.add(eye_right, 290, 210)

    # ears
    ear_left = GPolygon()
    ear_left.add_vertex((120, 200))
    ear_left.add_vertex((130, 230))
    ear_left.add_vertex((150, 210))
    ear_left.filled = True
    ear_left.fill_color = 'pink'
    ear_left.color = 'pink'
    window.add(ear_left)

    ear_right = GPolygon()
    ear_right.add_vertex((300, 165))
    ear_right.add_vertex((285, 185))
    ear_right.add_vertex((305, 180))
    ear_right.filled = True
    ear_right.fill_color = 'pink'
    ear_right.color = 'pink'
    window.add(ear_right)

    # nose
    nose = GPolygon()
    nose.add_vertex((260, 240))
    nose.add_vertex((290, 240))
    nose.add_vertex((275, 260))
    nose.filled = True
    nose.fill_color = 'salmon'
    nose.color = 'salmon'
    window.add(nose)

    # closed mouth
    mouth1 = GLine(275, 260, 270, 270)
    window.add(mouth1)
    mouth2 = GLine(270, 270, 255, 260)
    window.add(mouth2)
    mouth3 = GLine(275, 260, 280, 270)
    window.add(mouth3)
    mouth4 = GLine(280, 270, 290, 260)
    window.add(mouth4)

    # open mouth
    pop.filled = True
    pop.fill_color = 'lightpink'
    pop.color = 'lightpink'


def click(m):
    # Control the mouth
    window.add(pop, 220, 235)

    # Count the score
    global n
    global eye_n
    if 210 <= m.x <= 235 and 220 <= m.y <= 245:
        # Click on the left eye area
        eye_n += 1
        n += 10
    else:
        n += 1
    score.text = f"{n}"

    # if you click a certain number of times, the ranking will change.
    if WIN_NUM <= n < WIN_NUM + 10:  # avoid the leaderboard keeping flicking after the score exceeds the WIN_NUM
        first_place()

    # if you click the cat’s eye too many times, it will get mad.
    if eye_n >= ANGRY_NUM:
        angry_cat()


def release(m):
    pause(60)
    window.remove(pop)


def second_place():
    draw_leaderboard()
    # ranking
    label = GLabel(" #1     106B   #2     105B   #3 Others")
    label.font = "Courier-12"
    window.add(label, 60, 485)

    # flag
    window.add(j_flag1(), 95, 460)
    window.add(j_flag2(), 107, 465)
    window.add(t_flag1(), 235, 460)
    window.add(t_flag2(), 235, 460)
    window.add(t_flag3(), 240, 462)


def first_place():
    draw_leaderboard()
    # ranking
    label = GLabel(" #1     107B   #2     106B   #3 Others")
    label.font = "Courier-12"
    label.color = "darkorange"
    window.add(label, 60, 485)

    # flag
    window.add(j_flag1(), 235, 460)
    window.add(j_flag2(), 248, 465)
    window.add(t_flag1(), 95, 460)
    window.add(t_flag2(), 95, 460)
    window.add(t_flag3(), 100, 462)


# Cat's eyes & mouth change
def angry_cat():
    # bloody eyes
    eye_left_n = GOval(25, 25)
    eye_left_n.filled = True
    eye_left_n.fill_color = 'red'
    window.add(eye_left_n, 210, 220)

    eye_right_n = GOval(25, 25)
    eye_right_n.filled = True
    eye_right_n.fill_color = 'red'
    window.add(eye_right_n, 290, 210)

    dot1 = GOval(5, 5)
    dot1.filled = True
    dot1.fill_color = "black"
    window.add(dot1, 215, 225)

    dot2 = GOval(5, 5)
    dot2.filled = True
    dot2.fill_color = "black"
    window.add(dot2, 217, 235)

    dot3 = GOval(5, 5)
    dot3.filled = True
    dot3.fill_color = "black"
    window.add(dot3, 225, 230)

    dot4 = GOval(5, 5)
    dot4.filled = True
    dot4.fill_color = "black"
    window.add(dot4, 300, 215)

    dot5 = GOval(5, 5)
    dot5.filled = True
    dot5.fill_color = "black"
    window.add(dot5, 295, 225)

    dot6 = GOval(5, 5)
    dot6.filled = True
    dot6.fill_color = "black"
    window.add(dot6, 306, 223)

    # bloody mouse
    pop.fill_color = "darkred"
    pop.color = "darkred"


def draw_leaderboard():
    leaderboard = GRect(400, 50)
    leaderboard.filled = True
    leaderboard.fill_color = "white"
    window.add(leaderboard, (window.width - leaderboard.width) / 2, 450)


# Create Japan flag & Taiwan flag
def j_flag1():
    flag1 = GRect(40, 25)
    flag1.filled = True
    flag1.fill_color = "white"
    return flag1


def j_flag2():
    flag2 = GOval(15, 15)
    flag2.filled = True
    flag2.fill_color = "red"
    flag2.color = "red"
    return flag2


def t_flag1():
    flag1 = GRect(40, 25)
    flag1.filled = True
    flag1.fill_color = "red"
    return flag1


def t_flag2():
    flag2 = GRect(20, 15)
    flag2.filled = True
    flag2.fill_color = "blue"
    flag2.color = "blue"
    return flag2


def t_flag3():
    flag3 = GOval(10, 10)
    flag3.filled = True
    flag3.fill_color = "white"
    flag3.color = "white"
    return flag3


if __name__ == '__main__':
    main()
