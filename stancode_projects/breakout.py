"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The animation part works here.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
TOTAL_SCORE = 100


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.draw_hp(lives)
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    while True:
        pause(FRAME_RATE)
        if lives > 0:
            if graphics.score < TOTAL_SCORE:
                if graphics.is_game_start:
                    graphics.ball.move(dx, dy)

                    # Collision detection
                    if graphics.collision():
                        # Prevent the ball from rebounding twice in the area of the paddle
                        if graphics.ball.y + graphics.ball.height > graphics.paddle.y and dy < 0:
                            pass
                        else:
                            dy *= -1
                            # Hit a special brick, the speed will change.
                            if graphics.is_slow:
                                dy *= 0.8
                                graphics.is_slow = False
                            if graphics.is_fast:
                                dy *= 1.2
                                graphics.is_fast = False

                    # Border detection
                    if graphics.ball.x <= 0 or \
                            graphics.ball.x >= graphics.window.width - graphics.ball.width:
                        dx *= -1
                    if graphics.ball.y <= 0:
                        dy *= -1
                    if graphics.ball.y >= graphics.window.height:
                        lives -= 1
                        graphics.reduce_hp(lives)
                        graphics.is_game_start = False
                        graphics.initialize_ball_position()
                        dx = graphics.reset_dx()
                        dy = graphics.get_dy()

                    # Difficulty adjustment
                    if graphics.score >= 80:
                        graphics.harder()
            else:
                graphics.win()
                break
        else:
            graphics.lose()
            break


if __name__ == '__main__':
    main()
