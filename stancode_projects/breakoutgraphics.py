"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Heather is so sleepy, but the city lights are too bright to sleep.
Please help her to turn off all the lights so that she can have a good sleep.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 35       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width+5 + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        bg = GRect(window_width, window_height)
        bg.filled = True
        self.window.add(bg)
        self.hp_lst = []  # Stored variable according to the number of lives

        # beginning
        self.beginning1 = GLabel('Too bright!')
        self.beginning2 = GLabel('Help turn off all the lights!')
        self.beginning1.font = 'Courier-15-bold'
        self.beginning1.color = 'powderblue'
        self.beginning2.font = 'Courier-15-bold'
        self.beginning2.color = 'powderblue'
        self.window.add(self.beginning1, (self.window.width-self.beginning1.width)/2, 400)
        self.window.add(self.beginning2, (self.window.width - self.beginning2.width)/2, 450)

        # Create a paddle
        self.paddle = GImage("bed.jpg")
        self.paddle_y = window_height - paddle_offset*2
        self.window.add(self.paddle, (window_width-paddle_width)/2, self.paddle_y)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'powderblue'
        self.window.add(self.ball, (window_width-self.ball.width)/2, (window_height-self.ball.height)/2)
        self.ball_lst = ['ball_ul', 'ball_ur', 'ball_dl', 'ball_dr']  # Used to detect collisions

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        self.is_slow = False
        self.is_fast = False

        # Initialize our mouse listeners
        self.is_game_start = False
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        brick_x_spacing = brick_width+brick_spacing
        brick_y_spacing = brick_height+brick_spacing
        self.brick_lst = []
        for i in range(10):
            for j in range(10):
                self.brick_lst.append(str(i)+str(j))
                self.brick_lst[i*10+j] = GRect(brick_width, brick_height)
                self.brick_lst[i*10+j].filled = True
                self.brick_lst[i*10+j].fill_color = 'white'
                self.window.add(self.brick_lst[i*10+j], (brick_x_spacing+3)*i+12, brick_offset + brick_y_spacing*j)

        # Special_bricks
        # rise
        self.brick_lst[19].fill_color = 'salmon'
        self.brick_lst[42].fill_color = 'salmon'
        self.brick_lst[65].fill_color = 'salmon'
        # decline
        self.brick_lst[4].fill_color = 'aquamarine'
        self.brick_lst[37].fill_color = 'aquamarine'
        self.brick_lst[84].fill_color = 'aquamarine'
        # discolor
        self.brick_lst[23].fill_color = 'orange'
        self.brick_lst[47].fill_color = 'pink'
        self.brick_lst[55].fill_color = 'peru'
        self.brick_lst[72].fill_color = 'orchid'
        self.brick_lst[79].fill_color = 'violet'
        self.brick_lst[97].fill_color = 'rosybrown'
        # slow
        self.brick_lst[15].fill_color = 'grey'
        self.brick_lst[81].fill_color = 'grey'
        # fast
        self.brick_lst[11].fill_color = 'tan'
        self.brick_lst[34].fill_color = 'tan'

        # Score
        self.score = 0
        self.scoreboard = GLabel(f'Light: {100-self.score}')
        self.scoreboard.font = 'Courier-15-bold'
        self.scoreboard.color = 'white'
        self.window.add(self.scoreboard, 10, self.scoreboard.height + 10)

    def paddle_move(self, m):
        if self.paddle.width/2 <= m.x <= self.window.width-self.paddle.width/2:
            self.window.add(self.paddle, m.x-self.paddle.width/2, self.paddle.y)

    def start(self, m):
        self.window.remove(self.beginning1)
        self.window.remove(self.beginning2)
        self.is_game_start = True
        return self.is_game_start

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def initialize_ball_position(self):
        self.window.add(self.ball, (self.window.width-self.ball.width)/2,
                        (self.window.height-self.ball.height)/2)

    def reset_dx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def collision(self):
        """
        Hit the wall and paddle will return True to reverse the dy in the 'breakout' to make a rebound effect.
        Hit a brick will add point and eliminate the brick.
        Hit the colored bricks with special effects: paddle rises or falls, the ball changes color,
        the speed of the ball becomes faster or slower.
        """
        self.ball_lst[0] = self.window.get_object_at(self.ball.x, self.ball.y)
        self.ball_lst[1] = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.ball_lst[2] = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.ball_lst[3] = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        for corner in self.ball_lst:
            for i in range(len(self.brick_lst)):
                brick = self.brick_lst[i]
                if corner is self.paddle or corner is brick:
                    if corner is brick:
                        self.window.remove(corner)
                        self.score += 1
                        self.scoreboard.text = f'Light: {100-self.score}'
                        if corner is self.brick_lst[19] or corner is self.brick_lst[42] or corner is self.brick_lst[65]:
                            self.rise()
                        if corner is self.brick_lst[4] or corner is self.brick_lst[37] or corner is self.brick_lst[84]:
                            self.decline()
                        if corner is self.brick_lst[23]:
                            self.discolor(self.brick_lst[23].fill_color)
                        if corner is self.brick_lst[47]:
                            self.discolor(self.brick_lst[47].fill_color)
                        if corner is self.brick_lst[55]:
                            self.discolor(self.brick_lst[55].fill_color)
                        if corner is self.brick_lst[72]:
                            self.discolor(self.brick_lst[72].fill_color)
                        if corner is self.brick_lst[79]:
                            self.discolor(self.brick_lst[79].fill_color)
                        if corner is self.brick_lst[97]:
                            self.discolor(self.brick_lst[97].fill_color)
                        if corner is self.brick_lst[15] or corner is self.brick_lst[81]:
                            self.is_slow = True
                            return self.is_slow
                        if corner is self.brick_lst[11] or corner is self.brick_lst[34]:
                            self.is_fast = True
                            return self.is_fast
                    return True

    # Special bricks effect
    def rise(self):
        self.paddle.y -= 30

    def decline(self):
        if self.paddle.y < self.window.height - self.paddle.height:
            self.paddle.y += 30

    def discolor(self, color):
        self.ball.fill_color = color

    # hp
    def draw_hp(self, n):
        for i in range(n):
            self.hp_lst.append(str(i))
            self.hp_lst[i] = GImage('pillow.jpg')
            self.window.add(self.hp_lst[i], self.window.width - self.hp_lst[i].width * (i + 1) - (i + 5), 5)

    def reduce_hp(self, n):
        for i in range(len(self.hp_lst)):
            self.window.remove(self.hp_lst[i])
        for i in range(n):
            self.hp_lst.append(str(i))
            self.hp_lst[i] = GImage('pillow.jpg')
            self.window.add(self.hp_lst[i], self.window.width - self.hp_lst[i].width * (i + 1) - (i + 5), 5)

    # Final page
    def draw_bg(self):
        bg = GRect(self.window.width, self.window.height)
        bg.filled = True
        bg.fill_color = 'white'
        bg.color = 'white'
        return bg

    def win(self):
        bg = self.draw_bg()
        bg.fill_color = 'black'
        bg.color = 'black'
        self.window.add(bg)
        word = GLabel('Have a good dream! zzz...')
        word.font = 'Courier-20-bold'
        word.color = 'skyblue'
        self.window.add(word, (bg.width - word.width)/2, (bg.height + word.height)/2)

    def lose(self):
        bg = self.draw_bg()
        self.window.add(bg)
        word = GLabel('Please let me sleep......')
        word.font = 'Courier-20-bold'
        word.color = 'firebrick'
        self.window.add(word, (bg.width - word.width)/2, (bg.height + word.height)/2)

    # After the score exceeds 80, the color of the ball becomes darker.
    def harder(self):
        self.ball.fill_color = 'darkgrey'


if __name__ == 'breakoutgraphics':
    print('"breakoutgraphics.py" provides all the image components!')