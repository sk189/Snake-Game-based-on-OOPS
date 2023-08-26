from turtle import Screen, xcor
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the Screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
# Limiting the screen to refresh/ update only when required for smoothing animations/ movements
screen.tracer(0)

# Creating various objects
user_score = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Making the snake able to react to keypresses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Making all the snake segments
segments = []

game_is_on = True

while(game_is_on):
    screen.update()
    time.sleep(0.15)

    snake.move()

    # Detecting collision with food
    if (snake.head.distance(food) <= 13.5):
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    # Detecting collision with wall
    if(snake.head.xcor() > 284 or snake.head.ycor() > 284 or snake.head.xcor() < -284 or snake.head.ycor() < -284):
        game_is_on = False
        scoreboard.game_over()
    
    # Detecting collision of the snake head with itself
    for seg in snake.segments[1:]:
        if(snake.head.distance(seg) < 10):
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()