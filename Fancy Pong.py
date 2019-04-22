# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 8
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0, 0]
ball_pos = [WIDTH/2, HEIGHT/2]

paddle_pos1 = 45
paddle_pos2 = 45
pad_vel1 = 0
pad_vel2 = 0
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(1, 3)
        ball_vel[1] = - (random.randrange(1, 3))
      
    elif direction == LEFT:
        ball_vel[0] = - (random.randrange(1, 3))
        ball_vel[1] = - (random.randrange(1, 3))
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2
    # these are ints
    score1, score2 = 0, 0
    dirc = random.choice([LEFT, RIGHT])
    spawn_ball(dirc)

def draw(canvas):
    global score1, score2, paddle_pos1, paddle_pos2, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    global ball_pos
    ball_pos[0] +=  ball_vel[0]
    ball_pos[1] +=  ball_vel[1]
  
            
    # for collsion to upper and lower wall     
    if ball_pos[1] <= (BALL_RADIUS + 8):
        ball_vel[1] = -ball_vel[1]
        
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS - 8):
        ball_vel[1] = -ball_vel[1] 
        
    
    # for checking the collision with gutters  
    if ball_pos[0] <= (BALL_RADIUS ):
        spawn_ball(RIGHT)
        score2 += 1
        
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS ):
        spawn_ball(LEFT)
        score1 += 1
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 24, "Yellow", "Yellow")
    
    
    # update paddle's vertical position, keep paddle on the screen
    paddle_pos1 += pad_vel1
    paddle_pos2 += pad_vel2
    
    if paddle_pos1 <= 45:
        paddle_pos1 = 45
    elif paddle_pos1 >= HEIGHT - 45:
        paddle_pos1 = HEIGHT - 45
        
    if paddle_pos2 <= 45:
        paddle_pos2 = 45
    elif paddle_pos2 >= HEIGHT - 45:
        paddle_pos2 = HEIGHT - 45
    
    
    # draw paddles
    canvas.draw_line((0, paddle_pos1-45), (0, paddle_pos1 + 45), 16, "Red")
    canvas.draw_line((600, paddle_pos2-45), [600, paddle_pos2+45], 16, "Blue")
                    
  
    # determine whether paddle and ball collide
    if ball_pos[0] <= (16 + BALL_RADIUS) and (ball_pos[1] >= paddle_pos1-50) and ball_pos[1] <= paddle_pos1 +50:
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = 1.4 * ball_vel[0]
        ball_vel[1] = 1.4 * ball_vel[1]    
    
        
    if ball_pos[0] >= WIDTH - (16 + BALL_RADIUS) and ball_pos[1] <= paddle_pos2+50 and ball_pos[1] >= paddle_pos2 - 50: 
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = 1.4 * ball_vel[0]
        ball_vel[1] = 1.4 * ball_vel[1]
        
    # for decision who wins    
    if score1 >= 7 and score2 < 7:
        canvas.draw_text("Red Wins", [160, 200], 55,"Red")
        canvas.draw_text("Press 'Restart'", [220,400],24, "Yellow")
    elif score2 >= 7 and score1 < 7:
        canvas.draw_text("Blue Wins", [160, 200], 55,"Red")
        canvas.draw_text("Press 'Restart'", [220,400],24, "Yellow")
        
        
        
    # draw scores      
    canvas.draw_text(str(score1), [200, 80], 48, "Red")
    canvas.draw_text(str(score2), [400, 80], 48, "Blue") 
    
def keydown(key):
    global pad_vel1, pad_vel2
    acc = 10
    if key == simplegui.KEY_MAP["w"]:
        pad_vel1 -= acc    
    elif key == simplegui.KEY_MAP["s"]:
        pad_vel1 += acc
           
    if key == simplegui.KEY_MAP["up"]:
        pad_vel2 -= acc    
    elif key == simplegui.KEY_MAP["down"]:
        pad_vel2 += acc
     
def keyup(key):
    global pad_vel1, pad_vel2
    pad_vel1, pad_vel2 = 0, 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
frame.add_label('')
frame.add_label("CONTROLS FOR RED:")
frame.add_label('')
frame.add_label("'W' and 'S' keys for up and down respectively.")
frame.add_label('')
frame.add_label("CONTROLS FOR BLUE:")
frame.add_label('')
frame.add_label("'up arrow' and 'down arrow' keys for up and down respectively.")
frame.add_label('')
frame.add_label("To win you have to score 7 before the other player")
# start frame
new_game()
frame.start()
