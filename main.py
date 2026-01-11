from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:").lower()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Initial turtle position
position = {"x": -230,"y": -175,"step": 50}

# Generate turtles, one of each color in the color list, and appends it into all_turtles list
for color in color_list:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    all_turtles.append(new_turtle)

    position["y"] += position["step"]
    new_turtle.goto(position["x"], position["y"])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        paces = random.randint(0, 10)
        turtle.forward(paces)

        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle won the race!")
            else:
                print(f"You lose! The {winning_color} turtle won the race!")
            break

screen.exitonclick()