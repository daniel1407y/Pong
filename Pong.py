
import turtle
import time
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a=0
score_b=0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("square") #size is 20x20 (pixels)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3  #everytime the ball moves, it moves by 0.1 pixels
ball.dy = 3

# Names
Player_a_name=turtle.textinput("a", "Enter player a:")
Player_b_name=turtle.textinput("b", "Enter player b:")

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: {}  {}: {}".format(Player_a_name, score_a, Player_b_name, score_b), align="center", font=("courier", 24, "normal"))

# Movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Stop Game
def stop_Game():
    paddle_a.reset()
    paddle_b.reset()
    ball.reset()
    pen.clear()
    pen.color("red")
    pen.goto(0, 0)
    if score_a>=2:
        pen.write("{} won\n".format(Player_a_name) , align="center", font=("courier", 24, "normal"))
        pen.write("Final score {}:{}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    else:
        pen.write("{} won\n".format(Player_b_name) , align="center", font=("courier", 24, "normal"))
        pen.write("Final score {}:{}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    turtle.done()

# Main game loop 
while True:
    wn.update()

    if score_a>=2 or score_b>=2:
        stop_Game()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    time.sleep(.01)

    # Border checking
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of y coordinate

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of y coordinate

    if paddle_b.ycor() >225:
        paddle_b.sety(225)
    if paddle_b.ycor() <-225:
        paddle_b.sety(-225)
    if paddle_a.ycor() >225:
        paddle_a.sety(225)
    if paddle_a.ycor() <-225:
        paddle_a.sety(-225)

    if ball.xcor()<-390: # past paddle a
        ball.goto(0, 0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(Player_a_name, score_a, Player_b_name, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor()>390: # past paddle b
        ball.goto(0, 0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(Player_a_name, score_a, Player_b_name, score_b), align="center", font=("courier", 24, "normal"))


    # Paddle and ball collisions
    if ball.xcor() <-340 and  ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+65 and ball.ycor()>paddle_a.ycor()-65):
        ball.setx(-340)
        ball.dx *= -1

    if ball.xcor() > 340 and  ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+65 and ball.ycor()>paddle_b.ycor()-65):
        ball.setx(340)
        ball.dx *= -1

