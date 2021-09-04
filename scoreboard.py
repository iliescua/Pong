from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 50, "normal")
X_POS = 100
Y_POS = 230

class Scoreboard:


    def __init__(self):
        self.sb = Turtle()
        self.sb.pu()
        self.sb.color("White")
        self.sb.hideturtle()

    
    def write_score(self, r_score, l_score):
        self.sb.clear()

        self.sb.goto(X_POS, Y_POS)
        self.sb.write(r_score, align=ALIGN, font=FONT)

        self.sb.goto(-X_POS, Y_POS)
        self.sb.write(l_score, align=ALIGN, font=FONT)
