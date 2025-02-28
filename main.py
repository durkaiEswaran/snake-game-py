from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Myscoreboard
import time
is_game = True
screen = Screen()
screen.setup(700,700)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Myscoreboard()
food.refresh()
screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Left,"Left")
while is_game:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scores.increase_score()
    if snake.head.xcor() > 345 or snake.head.ycor() > 345 or snake.head.xcor() < -345 or snake.head.ycor() < -345:
        scores.game_over()
        is_game = False
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<10:
            is_game = False
            scores.game_over()




screen.exitonclick()
