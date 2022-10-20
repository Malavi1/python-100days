import turtle
from turtle import Turtle, Screen
import random
new_turtle = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle win the race')
y_position = [-70, -40, -10, 20, 50, 80]
colour = ['red','orange', 'yellow','green','blue','purple']
all_turtle = []
for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colour[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'you win! {winning_color} is the winner')
            else:
                print(f'you lose! {winning_color} is the winner')

        rad_distance = random.randint(0,10)
        turtle.forward(rad_distance)


screen.exitonclick()
