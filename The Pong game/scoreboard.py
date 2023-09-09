from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Courier", 24, "normal")


class score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score= 0
        self.penup()
        self.color("green")
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"P1:{self.l_score}", align=ALIGHNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"P2:{self.r_score}", align=ALIGHNMENT, font=FONT)

    def left_point(self):
        self.l_score+=1
        self.update()

    def right_point(self):
        self.r_score+=1
        self.update()
