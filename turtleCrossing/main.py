import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)
pl = Player()
screen.listen()
screen.onkey(pl.move, "Up")
car = CarManager()
sc=Scoreboard()
game = True
while game:
    # turtle move
    time.sleep(0.1)
    screen.update()
    car.create()
    car.carmove()


# level change
    if pl.ycor()>=280:
        pl.finish()
        car.fast()
        sc.lvlup()
# turle collide with car
    for ca in car.allcar:
        if ca.distance(pl)<20:
            sc.gameover()
            game=False




screen.exitonclick()
