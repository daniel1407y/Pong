
import turtle
import time

wn = turtle.Screen()
wn.title("Main Menu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
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
ball.hideturtle()
ball.goto(0, 0)
ball.dx = 4  #everytime the ball moves, it moves by 0.1 pixels
ball.dy = 4

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Welcome to PONG!\nPress '1' for one player \nPress '2' for two players", align="center", font=("courier", 24, "normal"))


# Functions- key pressed
def Player_vs_AI():
    Player_a_name=turtle.textinput("a", "Enter player a:")
    wn.clear()
    import Pong_Ai

def Player_vs_Player():
    #pen.clear()
    #pen.write("please enter Player 1 Name:", align="center", font=("courier", 24, "normal"))
    wn.clear()
    import Pong


# Keyboard binding
wn.listen()
wn.onkeypress(Player_vs_AI,"1")
wn.onkeypress(Player_vs_Player, "2")

# Main game loop 
while True:
    wn.update()
    

    

