from turtle import Turtle
ALIGNMENT = "center"
MOVEMENT = False
FONT_TYPE = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score} ", align=ALIGNMENT, move=MOVEMENT,
                   font=FONT_TYPE)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_TYPE)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
