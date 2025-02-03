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
def is_wining(bet, color):
    write_turtle = Turtle()
    write_turtle.hideturtle()
    write_turtle.color("black")

    if user_bet == color:
        screen.bgcolor("forest green")
        write_turtle.write(arg="YOU WIN", align="center", font=("arial", 28, "bold"))
    else:
        screen.bgcolor("deep pink")
        write_turtle.write(arg="YOU LOSE", align="center", font=("arial", 28, "bold"))


initial_turtle()
start_line()
end_line()

user_bet= screen.textinput(title="Guess the winner", prompt="Enter the color for the winner: ")
winning_color=""
race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(random.random()*5)
        if turtle.xcor() >= 450:
            winning_color = turtle.pencolor()
            race_on = False
        else:
            pass
        screen.update()
        time.sleep(0.001)

is_wining(user_bet, winning_color)



screen.exitonclick()