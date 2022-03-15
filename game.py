# A simple Pong game using PyGame

# Import the necessary modules
import pygame
import random

# initialize the pygame module
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("PyPong")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define ball location, default to center of screen
BALL_COORDINATES = [400, 300]
# define ball X, Y speed
BALL_SPEED = [random.choice([-5, 5]), random.choice([-5, 5])]
# define the left paddle Y position
LEFT_PADDLE_Y = 300
# define the right paddle Y position
RIGHT_PADDLE_Y = 300
# left paddle size
LEFT_PADDLE_SIZE = [20, 100]
# right paddle size
RIGHT_PADDLE_SIZE = [20, 100]
# ball is paused by default
BALL_PAUSED = True
# left player score
LEFT_SCORE = 0
# right player score
RIGHT_SCORE = 0
NEW_GAME = True

# function to draw the ball
def draw_ball():
    pygame.draw.circle(screen, GREEN, BALL_COORDINATES, 20)

# move left paddle accorded to mouse Y position
def move_left_paddle():
    global LEFT_PADDLE_Y
    LEFT_PADDLE_Y = pygame.mouse.get_pos()[1]

    # make sure the paddle doesn't go off the screen
    if LEFT_PADDLE_Y < 0:
        LEFT_PADDLE_Y = 0
    elif LEFT_PADDLE_Y > 599:
        LEFT_PADDLE_Y = 599

# move the right paddle in response to the ball Y position
def move_right_paddle():
    global RIGHT_PADDLE_Y
    # if the ball is moving up, move the right paddle up
    if BALL_SPEED[1] < 0:
        RIGHT_PADDLE_Y -= 5
    # if the ball is moving down, move the right paddle down
    elif BALL_SPEED[1] > 0:
        RIGHT_PADDLE_Y += 5
    # make sure the paddle doesn't go off the screen
    if RIGHT_PADDLE_Y < 0:
        RIGHT_PADDLE_Y = 0
    elif RIGHT_PADDLE_Y > 599:
        RIGHT_PADDLE_Y = 599
    

def draw_left_paddle():
    pygame.draw.rect(screen, RED, [0, LEFT_PADDLE_Y, LEFT_PADDLE_SIZE[0], LEFT_PADDLE_SIZE[1]])

def draw_right_paddle():
    pygame.draw.rect(screen, BLUE, [780, RIGHT_PADDLE_Y, RIGHT_PADDLE_SIZE[0], RIGHT_PADDLE_SIZE[1]])

def check_ball_paddle_collision():
    # check for collisions with the left paddle
    if BALL_COORDINATES[0] <= LEFT_PADDLE_SIZE[0] and BALL_COORDINATES[1] >= LEFT_PADDLE_Y and BALL_COORDINATES[1] <= LEFT_PADDLE_Y + LEFT_PADDLE_SIZE[1]:
        BALL_SPEED[0] = -BALL_SPEED[0]
        BALL_SPEED[1] = random.choice([-5, 5])
    # check for collisions with the right paddle
    elif BALL_COORDINATES[0] >= 760 and BALL_COORDINATES[1] >= RIGHT_PADDLE_Y and BALL_COORDINATES[1] <= RIGHT_PADDLE_Y + RIGHT_PADDLE_SIZE[1]:
        BALL_SPEED[0] = -BALL_SPEED[0]
        BALL_SPEED[1] = random.choice([-5, 5])

def check_ball_wall_collision():
    global RIGHT_SCORE
    global LEFT_SCORE
    # if the ball collides with the top wall, bounce it appropriately
    if BALL_COORDINATES[1] <= 0:
        BALL_SPEED[1] = -BALL_SPEED[1]
    # if the ball collides with the bottom wall, bounce it appropriately
    elif BALL_COORDINATES[1] >= 599:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # if the ball collides with the left wall, reset the ball to the center and randomize the direction
    if BALL_COORDINATES[0] <= 0:
        BALL_COORDINATES[0] = 400
        BALL_COORDINATES[1] = 300
        BALL_SPEED[0] = -5
        BALL_SPEED[1] = random.choice([-5, 5])
        # increment the right player's score
        RIGHT_SCORE += 1

    # if the ball collides with the right wall, reset the ball to the center and randomize the direction
    elif BALL_COORDINATES[0] >= 800:
        BALL_COORDINATES[0] = 400
        BALL_COORDINATES[1] = 300
        BALL_SPEED[0] = 5
        BALL_SPEED[1] = random.choice([-5, 5])
        # increment the left player's score
        LEFT_SCORE += 1

def move_ball(paused = False):
    BALL_COORDINATES[0] += BALL_SPEED[0]
    BALL_COORDINATES[1] += BALL_SPEED[1]
    check_ball_paddle_collision()
    check_ball_wall_collision()

def draw_left_score():
    # display the left player's score
    font = pygame.font.Font(None, 36)
    text = font.render(str(LEFT_SCORE), True, BLACK)
    screen.blit(text, [10, 10])

def draw_right_score():
    # display the right player's score
    font = pygame.font.Font(None, 36)
    text = font.render(str(RIGHT_SCORE), True, BLACK)
    screen.blit(text, [780, 10])

def init_game():
    # initialize the game
    global BALL_PAUSED
    BALL_PAUSED = False
    global LEFT_SCORE
    LEFT_SCORE = 0
    global RIGHT_SCORE
    RIGHT_SCORE = 0
    # initialize the ball to the center of the screen
    BALL_COORDINATES[0] = 400
    BALL_COORDINATES[1] = 300
    # make the ball move to the left by default
    BALL_SPEED[0] = -5
    BALL_SPEED[1] = random.choice([-5, 5])


# run the game loop
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill entire screen with white
    screen.fill(WHITE)

    # draw the left paddle
    draw_left_paddle()
    # draw the right paddle
    draw_right_paddle()

    # draw the scores
    draw_left_score()
    draw_right_score()

    # move the left paddle
    move_left_paddle()
    # move the right paddle
    move_right_paddle()

    # draw the ball
    draw_ball()
    move_ball(False)

    # update the screen
    pygame.display.flip()

    # limit to 60 frames per second
    pygame.time.delay(10)

pygame.quit()
