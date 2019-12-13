import turtle

wn = turtle.Screen()

wn.bgcolor('black')
wn.title("PingPong")
wn.setup(height=600, width=800)

#Score!!!
score_a = 0
score_b = 0




# paddle1 (firt player) setup

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)


# paddle1 movement

def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")

# paddle2 (second player)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)


# paddle2 movement

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


wn.listen()
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

# making a ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3 # ball moves every second for 2 pixels in x
ball.dy = 3  # ball moves every second for 2 pixels in y

#PEN (draws the score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))   #font це шрифт і розмір (нормал значить тип нормальний), align це по центру, зліва чи справа

# MAIN GAME LOOP
while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # xcor and ycor is a function which displays your object coordinate in x or in y
    ball.sety(ball.ycor() + ball.dy)
    # Borders
    if ball.ycor() > 290:  # for Y positive
        ball.sety(290)  # idk why not 300 if height is 300 + 300 = 600
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:  # for Y negative
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:  # for X positive
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # for X negative
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx = ball.dx * -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx = ball.dx * -1
    #Paddles cant go out the border
            #paddle1
    if paddle1.ycor() > 260:
        paddle1.sety(260)
    if paddle1.ycor() < -260:
        paddle1.sety(-260)
            #paddle2
    if paddle2.ycor() > 260:
        paddle2.sety(260)
    if paddle2.ycor() < -260:
        paddle2.sety(-260)
#   if score_a == 5:
        #pen.clear()
        #pen.goto(0,0)
        #ball.dx = 0
        #ball.dy = 0
        #pen.write("Player A Won!", align="center",font=("Courier", 26,"normal"))
#    if score_a == 5:
        #pen.clear()
        #pen.goto(0,20) #Воно якогось хріна блимає, бо це цикл, мені виправляти влом
        #all.dx = 0
        #ball.dy = 0
        #pen.write("Player B Won!", align="center",font=("Courier", 26,"normal"))














wn.mainloop()
