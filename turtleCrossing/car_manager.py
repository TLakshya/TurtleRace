

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():

    def __init__(self):
        self.allcar = []

    def create(self):
        randomc=random.randint(1,6)
        if randomc==6:
            new=Turtle("square")
            new.shapesize(1,2)
            new.color(random.choice(COLORS))
            new.penup()

            new.goto(300,random.randint(-260,260))
            self.allcar.append(new)


    def carmove(self):
        for car in self.allcar:
            car.backward(STARTING_MOVE_DISTANCE)
    def fast(self):
        self.STARTING_MOVE_DISTANCE+1000