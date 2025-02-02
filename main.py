import random
from turtle import Turtle, Screen
import time

turtles = []
colors = ["red", "orange", "green", "blue", "white"]
y_position= [-100, -50, 0, 50, 100]

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Turtle Race v1.00")
screen.tracer(0)
# Create turtles
def initial_turtle():
    for i in range(5):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(-480, y_position[i])
        turtles.append(new_turtle)
# Draw start line
def start_line():
    s_line = Turtle()
    s_line.hideturtle()
    s_line.color("white")
    s_line.penup()
    s_line.goto(-460, -120)
    s_line.left(90)
    s_line.pendown()
    s_line.forward(240)
# Draw end line
def end_line():
    e_line = Turtle()
    e_line.hideturtle()
    e_line.color("white")
    e_line.penup()
    e_line.goto(460, -120)
    e_line.left(90)
    e_line.pendown()
    e_line.forward(240)

initial_turtle()
start_line()
end_line()
race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(random.random()*5)
    screen.update()
    time.sleep(0.05)


screen.exitonclick()