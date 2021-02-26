import turtle\
import winsound
#winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

wn = turtle.Screen()
wn.title("rrichglitch pong")
wn.bgcolor("black")
wn.setup(800,600)
wn.tracer(0,1)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.goto(-350,0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.goto(0,0)
default_dx = .3
ball.dx = default_dx
ball.dy = .15

# score
score_a = 0
score_b = 0
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0,260)
pen1.write("Player A: 0  Player B: 0", align = "center",font =("courier",24,"normal"))


def paddle_a_up():
    if paddle_a.ycor() < 300 :
        paddle_a.sety(paddle_a.ycor()+50)

def paddle_a_down():
    if paddle_a.ycor() > -300:
        paddle_a.sety(paddle_a.ycor()-50)

def paddle_b_up():
    if paddle_b.ycor() < 300:
        paddle_b.sety(paddle_b.ycor()+50)

def paddle_b_down():
    if paddle_b.ycor() > -300:
        paddle_b.sety(paddle_b.ycor()-50)

# key bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

#main loop
while True:
    wn.update()

    # moveball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checks
    if abs(ball.ycor()) > 290:
        ball.dy *= -1
    if ball.xcor() > 400:
        score_a += 1
        pen1.clear()
        pen1.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
        ball.dx = default_dx * -1

    elif ball.xcor() < -400:
        score_b += 1
        pen1.clear()
        pen1.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                   font=("courier", 24, "normal"))
        ball.dx = default_dx


    # paddle b collision
    if paddle_b.ycor() - 60 <= ball.ycor() <= paddle_b.ycor() + 60:
        if ball.xcor() >= paddle_b.xcor() - 10 and ball.dx > 0:
            ball.dx *= -1.05

    # paddle a collision
    if paddle_a.ycor() - 60 <= ball.ycor() <= paddle_a.ycor() + 60:
        if ball.xcor() <= paddle_a.xcor() + 10 and ball.dx < 0:
            ball.dx *= -1.05
