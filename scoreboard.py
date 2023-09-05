from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(x=-40, y=270)
        self.hideturtle()
        self.pu()
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.set_score()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", font=('Courier', 22, 'normal'))


    def resets(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=-40, y=0)
    #     self.write(arg="GAME OVER.", font=('Courier', 22, 'normal'))

    def set_score(self):
        self.update_scoreboard()
        self.score += 1
