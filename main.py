import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
is_race_on=False
user_bet=screen.textinput("Make your bet","Which turtle will win the race? Chooce color")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles=[]
height=150
for color in colors:
    index=0
    turtle=Turtle("turtle")
    turtle.color(color)
    turtle.penup()
    height-=50
    turtle.goto(-238,height)
    all_turtles.append(turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                print(f"You have won! The {user_bet} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_turtle} turtle is the winner!")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()