FONT = ("Courier", 50, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.hideturtle()
        self.penup()
        self.lvlup()

    def lvlup(self):
        self.clear()
        self.goto(-270, 270)
        self.i += 1
        self.write(f"level :{self.i} ", FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", FONT)
