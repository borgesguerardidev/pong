import turtle

window = turtle.Screen()
window.title('Pong by borgesguerardi')
window.bgcolor('grey')
window.setup(width=800, height=600)
window.tracer(0)

# paddle a
paddle_orange = turtle.Turtle()
paddle_orange.speed(0)
paddle_orange.shape('square')
paddle_orange.color('orange')
paddle_orange.shapesize(stretch_wid=5, stretch_len=0.8)
paddle_orange.penup()
paddle_orange.goto(-350, 0)

# paddle b
paddle_blue = turtle.Turtle()
paddle_blue.speed(0)
paddle_blue.shape('square')
paddle_blue.color('blue')
paddle_blue.shapesize(stretch_wid=5, stretch_len=0.7)
paddle_blue.penup()
paddle_blue.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.color('black')
ball.penup()


# main funcs
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


# user input
window.listen()
window.onkeypress(paddle_orange_up, 'w')
window.onkeypress(paddle_orange_down, 's')
window.onkeypress(paddle_blue_up, 'Up')
window.onkeypress(paddle_blue_down, 'Down')

# main loop
while True:
    window.update()
