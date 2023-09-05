from turtle import Turtle
import time

class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for i in range(3):
            turtle1 = Turtle("square")
            turtle1.setpos(x=0 + i * -20, y=0)
            turtle1.color("white")
            turtle1.pu()
            self.all_squares.append(turtle1)
    def extend(self):
        turtle1 = Turtle("square")
        turtle1.setpos(self.all_squares[-1].position())
        turtle1.color("white")
        turtle1.pu()
        self.all_squares.append(turtle1)

    def reset(self):
        for square in self.all_squares:
            square.goto(1000,1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]

    def move(self):
        for square in range(len(self.all_squares) - 1, 0, -1):
            x = self.all_squares[square - 1].xcor()
            y = self.all_squares[square - 1].ycor()
            self.all_squares[square].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
