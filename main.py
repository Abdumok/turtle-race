import random
from turtle import Turtle, Screen
import time

TURTLE_SPEED= 5

turtles = []
colors = ["red", "orange", "green", "blue", "white"]
y_position= [-100, -50, 0, 50, 100]
goal_letters= ["G", "O", "A", "L"]
goal_position= [80, 30, -30, -80]

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
    e_line.goto(468, -120)
    e_line.left(90)
    e_line.pendown()
    e_line.forward(240)
# TO determine the winner
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
# Write Goal word:
def goal(letters, pos):
    for i in range(4):
        goal = Turtle()
        goal.hideturtle()
        goal.color("white")
        goal.penup()
        goal.goto(x= 480, y= pos[i])
        goal.pendown()
        goal.write(arg=letters[i], align="center", font=("arial", 12, "bold"))
# Draw Flag:
def flag():
    flag_element= []
    xcor= 473
    for j in range(2):
        ycor= -110
        for i in range(17):
            white= Turtle()
            white.shape("square")
            white.color("white")
            white.penup()
            white.shapesize(.25)
            white.goto(xcor, ycor)
            flag_element.append(white)
            ycor += 14
        xcor += 14

    xcor= 480
    ycor= -117
    for i in range(17):
        white= Turtle()
        white.color("white")
        white.shape("square")
        white.penup()
        white.shapesize(0.25)
        white.goto(xcor, ycor)
        flag_element.append(white)
        ycor += 14
# Show counting down numbers:
def count_down():
    count= Turtle()
    count.hideturtle()
    count.color("white")
    count.goto(x=0, y=0)
    for i in range(4):
        count.write(arg=(3-i), align="center", font=("courier", 48, "bold"))
        time.sleep(1)
        screen.update()
        count.clear()

user_bet= screen.textinput(title="Guess the winner", prompt="Enter the color for the winner: ")
winning_color=""
race_on = True

screen.tracer(0)
# goal(goal_letters, goal_position)
flag()
initial_turtle()
start_line()
end_line()
count_down()

while race_on:
    for turtle in turtles:
        turtle.forward(random.random()*TURTLE_SPEED)
        if turtle.xcor() >= 455:
            winning_color = turtle.pencolor()
            race_on = False
        else:
            pass
        screen.update()

is_wining(user_bet, winning_color)

screen.exitonclick()