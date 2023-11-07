from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")



turtle_1 = Turtle(shape="turtle")
turtle_1.penup()
turtle_1.goto(x=-240, y=0)



print(user_bet)

screen.exitonclick()