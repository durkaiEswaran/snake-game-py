from turtle import Turtle
position = [(-20,0),(-10,0),(0,0)]
move_distance = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in position:
            tr = Turtle("square")
            tr.goto(i)
            tr.color("white")
            tr.penup()
            self.segments.append(tr)

    def add_segment(self, position):
            tr = Turtle("square")
            tr.goto(position)
            tr.color("white")
            tr.penup()
            self.segments.append(tr)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
            

        self.head.forward(move_distance)
    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

