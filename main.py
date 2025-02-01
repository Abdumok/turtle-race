import random
from turtle import Turtle, Screen

turtles = []
colors = ["red", "orange", "green", "blue", "white"]
y_position= [-100, -50, 0, 50, 100]

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Turtle Race v1.00")

# Create turtles
def initial_turtle():
    for i in range(5):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(-480, y_position[i])
        turtles.append(new_turtle)


initial_turtle()

screen.exitonclick()