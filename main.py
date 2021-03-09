from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which color will win today?")
colors = ["red", "orange", "blue", "black", "pink", "yellow", "green", "purple", "brown"]
names = ["James", "Caine", "Nader", "Bryan", "Kevin", "Matheo", "Anna", "Trinh", "Moh"]
y_positions = [-130, -100, -70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0,9):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"The {winning_color} turtle is the winner!")



        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()