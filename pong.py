import turtle
import winsound

t = turtle

wn = t.Screen()
wn.title("Pong by Ben")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

class c_paddle_a:
    paddle_a = t.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

class c_paddle_b:
    paddle_b = t.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

class c_ball:
    ball = t.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

    dx = 0.3
    dy = 0.3

# pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = c_paddle_a.paddle_a.ycor()
    y += 20
    c_paddle_a.paddle_a.sety(y)

def paddle_a_down():
    y = c_paddle_a.paddle_a.ycor()
    y += -20
    c_paddle_a.paddle_a.sety(y)

def paddle_b_up():
    y = c_paddle_b.paddle_b.ycor()
    y += 20
    c_paddle_b.paddle_b.sety(y)

def paddle_b_down():
    y = c_paddle_b.paddle_b.ycor()
    y += -20
    c_paddle_b.paddle_b.sety(y)

class keyboard_binding:
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "i")
    wn.onkeypress(paddle_b_down, "k")

class Main_game_loop:
    while True:
        wn.update()

        c_ball.ball.setx(c_ball.ball.xcor() + c_ball.dx)
        c_ball.ball.sety(c_ball.ball.ycor() + c_ball.dy)

        #border
        if c_ball.ball.ycor() > 290:
            c_ball.ball.sety(290)
            c_ball.dy *= -1
            winsound.PlaySound("pingpond-MadeWithClipchamp.wav", winsound.SND_ASYNC)

        if c_ball.ball.ycor() < -290:
            c_ball.ball.sety(-290)
            c_ball.dy *= -1

        if c_ball.ball.xcor() > 390:
            c_ball.ball.goto(0, 0)
            c_ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if c_ball.ball.xcor() < -390:
            c_ball.ball.goto(0, 0)
            c_ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # paddle and ball collisions
        if (c_ball.ball.xcor() > 340 and c_ball.ball.xcor() < 350 and (c_ball.ball.ycor() < c_paddle_b.paddle_b.ycor() + 40 and c_ball.ball.ycor() > c_paddle_b.paddle_b.ycor() -40)):
            c_ball.ball.setx(340)
            c_ball.dx *= -1

        if (c_ball.ball.xcor() < -340 and c_ball.ball.xcor() > -350 and (c_ball.ball.ycor() < c_paddle_a.paddle_a.ycor() + 40 and c_ball.ball.ycor() > c_paddle_a.paddle_a.ycor() -40)):
            c_ball.ball.setx(-340)
            c_ball.dx *= -1