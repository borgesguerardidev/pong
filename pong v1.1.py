#PONG by borgesguerardi!

# modules
import turtle
import winsound
from playsound import playsound

# canvas
window = turtle.Screen()
window.title('Pong by borgesguerardi - ver 1.1')
window.bgcolor('grey')
window.setup(width=800, height=600)
window.tracer(0)

# paddle orange
# 50px tall, 7px wide
paddle_orange = turtle.Turtle()
paddle_orange.speed(0)
paddle_orange.shape('square')
paddle_orange.color('orange')
paddle_orange.shapesize(stretch_wid=5, stretch_len=0.7)
paddle_orange.penup()
paddle_orange.goto(-350, 0)

# paddle blue
paddle_blue = turtle.Turtle()
paddle_blue.speed(0)
paddle_blue.shape('square')
paddle_blue.color('blue')
paddle_blue.shapesize(stretch_wid=5, stretch_len=0.7)
paddle_blue.penup()
paddle_blue.goto(350, 0)

# ball
# 5px wide and tall
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.speedx, ball.speedy = 0.3, -0.3

# main funcs

    # paddle movements
def paddle_orange_up():
    y = paddle_orange.ycor()
    y += 20
    paddle_orange.sety(y)

def paddle_orange_down():
    y = paddle_orange.ycor()
    y -= 20
    paddle_orange.sety(y)

def paddle_blue_up():
    y = paddle_blue.ycor()
    y += 20
    paddle_blue.sety(y)

def paddle_blue_down():
    y = paddle_blue.ycor()
    y -= 20
    paddle_blue.sety(y)

def printed_score():
    txt_score.clear()
    return txt_score.write(f'orange: {score_orange}  blue: {score_blue}', align='center', font=('Courier', 15, 'normal'))

def sound_effects(paddle = True, borders = False):
    if paddle == False and borders == True:
        return winsound.PlaySound('wall_bounce.wav', winsound.SND_ASYNC)
    else:
        return winsound.PlaySound('paddle_bounce.wav', winsound.SND_ASYNC)

# user input
window.listen()
window.onkeypress(paddle_orange_up, 'w')
window.onkeypress(paddle_orange_down, 's')
window.onkeypress(paddle_blue_up, 'Up')
window.onkeypress(paddle_blue_down, 'Down')

#score
score_orange = 0
score_blue = 0

# score text
txt_score = turtle.Turtle()
txt_score.speed(0)
txt_score.color('white')
txt_score.penup()
txt_score.hideturtle()
txt_score.goto(0, 260)
printed_score()

# game loop
while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + ball.speedx)
    ball.sety(ball.ycor() + ball.speedy)

    # borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.speedy *= -1
        sound_effects(paddle = False, borders = True)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.speedy *= -1
        sound_effects(paddle = False, borders = True)
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.speedx *= -1
        score_blue += 1
        printed_score()
        sound_effects(paddle = False, borders = True)
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.speedx *= -1
        score_orange += 1
        printed_score()
        sound_effects(paddle = False, borders = True)

    # paddle collisions
        
        # paddle blue
    if (ball.xcor() < -335 and ball.xcor() > -350) and (ball.ycor() < paddle_orange.ycor() + 40 and ball.ycor() > paddle_orange.ycor() - 40):
        ball.setx(-335)
        ball.speedx *= -1
        sound_effects(paddle = True, borders = False)
        
        # paddle orange
    elif (ball.xcor() > 335 and ball.xcor() < 350) and (ball.ycor() < paddle_blue.ycor() + 40 and ball.ycor() > paddle_blue.ycor() - 40):
        ball.setx(335)
        ball.speedx *= -1
        sound_effects(paddle = True, borders = False)