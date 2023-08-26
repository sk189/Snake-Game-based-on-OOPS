from turtle import Turtle

ALIGNMENT = "center"
FONT = ['Arial', 15, 'normal']


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(275)
        self.write_score()

    
    def write_score(self):
        self.write(f"Score : {self.score} High Score : {self.high_score}", align = ALIGNMENT, font = FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
        if(self.score > self.high_score):
            self.goto(0,-24)
            self.write("Congratulations, You just made the new High Score!", align = ALIGNMENT, font = FONT)
            with open("highScore.txt", mode = 'w') as file:
                file.write(str(self.score))
