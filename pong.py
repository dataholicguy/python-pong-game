import turtle

# init screen
wn = turtle.Screen()

# set title for window
wn.title('Pong Game by Dataholicguy')

# set background color
wn.bgcolor('black')

# set size for window
wn.setup(width=800, height=600)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0) # center of window
ball.dx = 3     # distance each time the ball move horizontally
ball.dy = 3    # distance each time the ball move vertically

# move the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding for moving paddles
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Pen for Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('sans-serif', 24, 'normal'))

# Score
score_a = 0
score_b = 0

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking

    # top & bottom
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    # left & right
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {0}  Player B: {1}'.format(score_a, score_b), align='center', font=('sans-serif', 24, 'normal'))

    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {0}  Player B: {1}'.format(score_a, score_b), align='center', font=('sans-serif', 24, 'normal'))


    # padle and ball collisions

    # ball vs paddle A
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    # ball vs paddle B
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
