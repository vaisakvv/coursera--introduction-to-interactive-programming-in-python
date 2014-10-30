#http://www.codeskulptor.org/#user38_YttlvdmXpR_0.py

# Implementation of classic arcade game Pong

import simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles

width = 600

height= 400

ball_radius = 20

pad_width = 8

pad_height = 80

half_pad_width = pad_width / 2

half_pad_height = pad_height / 2

LEFT = False

RIGHT = True



# initialize ball_pos and ball_vel for new bal in middle of table

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):

    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [(width - 1) / 2, (height- 1) / 2]

    if direction: # do not need "direction == true" it is redundant

        ball_vel = [random.randrange(1, 3), random.randrange(2, 5) * -1] # start the ball randomly right

    else:

        ball_vel = [random.randrange(1, 3) * -1, random.randrange(2, 5) * -1] # start the ball randomly left





# define event handlers

def new_game():

    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are numbers

    global score1, score2 # these are ints

    #reset all the game variables

    score1 = 0

    score2 = 0

    spawn_ball(random.choice([RIGHT, LEFT])) # I used random choice so the ball would not always spawn

    paddle1_pos = (height/ 2) - half_pad_height # in the same direction when a new game starts.

    paddle2_pos = (height / 2) - half_pad_height

    paddle1_vel = 0

    paddle2_vel = 0

    

def draw(canvas):

    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

# draw mid line and gutters

    canvas.draw_line([width / 2, 0], [width / 2, width], 1, "White")

    canvas.draw_line([pad_width, 0], [pad_width, height], 1, "White")

    canvas.draw_line([width - pad_width,0], [width - pad_width, height], 1, "White")

# update ball

    ball_pos[0] += ball_vel[0]

    ball_pos[1] += ball_vel[1]

# check for top and bottom collision 

    if ball_pos[1] - ball_radius <= 0:

        ball_vel[1] *= -1

    elif ball_pos[1] + ball_radius >= height - 1:

        ball_vel[1] *= -1

# The next two if statements check for paddle collision. I didn't factor in ball radius to make the

# collision detection more relaxed and the game more playable.

    if (ball_pos[0] - pad_width) - ball_radius <= 0:

        if ball_pos[1] > paddle1_pos and ball_pos[1] < paddle1_pos + pad_height:

            ball_vel[0] *= -1.1 # Increase speed of the ball I did both x and y to avoid the

            ball_vel[1] *= 1.1 # ball going in a straight line

        else: # point scored

            score2 += 1

            spawn_ball(RIGHT)

    if ball_pos[0] + (ball_radius +pad_width ) >= width: # checks for right paddle collision

        if ball_pos[1] > paddle2_pos and ball_pos[1] < paddle2_pos + pad_height:

            ball_vel[0] *= -1.1

            ball_vel[1] *= 1.1

        else:

            score1 += 1

            spawn_ball(LEFT)

# draw ball

    canvas.draw_circle(ball_pos, ball_radius, 1, 'Black', 'White')

# update paddle's vertical position, keep paddle on the screen

    if paddle1_pos <= 0:

        paddle1_pos = 0

    elif paddle1_pos + pad_height >= height:

        paddle1_pos = height - pad_height

    if paddle2_pos <= 0:

        paddle2_pos = 0

    elif paddle2_pos + pad_height >= height:

        paddle2_pos = height - pad_height

# move paddles

    paddle1_pos += paddle1_vel

    paddle2_pos += paddle2_vel

# draw paddles

    canvas.draw_polygon([(0, paddle1_pos),

    (pad_width, paddle1_pos),

    (pad_width, paddle1_pos + pad_height),

    (0, paddle1_pos + pad_height)], 1, 'Black', 'White')

    canvas.draw_polygon([(width - pad_width, paddle2_pos),

    (width, paddle2_pos),

    (width, paddle2_pos + pad_height),

    (width - pad_width, paddle2_pos + pad_height)], 1, 'Black', 'White')

# draw scores

    score = str(score1) + ' ' + str(score2)

    t_width = frame.get_canvas_textwidth(score, 60)

    canvas.draw_text(score, ((width / 2) - (t_width / 2), 47), 60, 'White')



def keydown(key):

    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['S']: # Responding to key presses notice how I do the

        paddle1_vel += 5 # opposite in the keyup handler. This approach responds

    elif key == simplegui.KEY_MAP['W']: # well to multiple keys pressed in opposite directions.

        paddle1_vel -= 5

    elif key == simplegui.KEY_MAP['down']:

        paddle2_vel += 5

    elif key == simplegui.KEY_MAP['up']:

        paddle2_vel -= 5

        

def keyup(key):

    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['S']:

            paddle1_vel -= 5

    elif key == simplegui.KEY_MAP['W']:

        paddle1_vel += 5

    elif key == simplegui.KEY_MAP['down']:

        paddle2_vel -= 5

    elif key == simplegui.KEY_MAP['up']:

        paddle2_vel += 5

        

#restart button simply calls new game

def restart():

    new_game()

    

# create frame

frame = simplegui.create_frame("Pong", width, height)

frame.set_draw_handler(draw)

frame.set_keydown_handler(keydown)

frame.set_keyup_handler(keyup)

reset_button = frame.add_button('Restart', restart)

# start frame

new_game()

frame.start()
