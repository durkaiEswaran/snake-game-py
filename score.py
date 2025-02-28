from turtle import Turtle
from food import Food
class Myscoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-20,310)
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"score: {self.score}",align="center",font=("Courier",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",24,"normal"))
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update()