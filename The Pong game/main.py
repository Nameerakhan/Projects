from turtle import  Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import score

scr = Screen()
scr.setup(width=800, height = 600)
scr.bgcolor("black")
scr.title("The Pong game")
scr.tracer(0)
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))

ball = Ball()
score_record = score()
scr.listen()
scr.onkey(paddle1.go_up,"Up")
scr.onkey(paddle1.go_down,"Down")
scr.onkey(paddle2.go_up,"w")
scr.onkey(paddle2.go_down,"s")


is_on =True
while is_on:
    time.sleep(ball.moving_speed)
    scr.update()
    ball.move()


    if ball.ycor()>280 or ball.ycor()<-280:
#         ball bounces
         ball.bounce_y()
    if ball.distance(paddle1)<50 and ball.xcor() >320  or ball.distance(paddle2) <50 and ball.xcor() <-320 :
        ball.bounce_x()


    if ball.xcor()>380:
       ball.reset_position()
       score_record.left_point()

    if ball.xcor()<-380:
       ball.reset_position()
       score_record.right_point()

scr.exitonclick()
