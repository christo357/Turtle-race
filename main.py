from turtle import Turtle,Screen
import random as rm


screen = Screen()
screen.setup(width= 500,height=400)

colors = ["violet","indigo","blue","green","yellow","orange","red"]
y_pos = [-70,-40,-10,20,50,80,110]
turtles = []


user_bet = screen.textinput(title="Your choice",prompt="Enter your turtle's color:")
print(user_bet)

def turtle_race(turtles, user_bet):
    rm.choice(turtles).forward(5)
    flag = True
    for i in range(0, 7):
        if turtles[i].xcor() >= 240:
            flag = False
            winner = turtles[i].pencolor()
            print(winner)
            print(type(winner))
            if winner == user_bet.lower():
                print("You win")
            else:
                print(f"You lose.Winner is {winner} turtle.")
            return winner
            # print(turtles[i].color())


    if flag:
        turtle_race(turtles, user_bet)

for turtle_index in range(0,7):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240,y=y_pos[turtle_index])
    turtles.append(tim)

turtle_race(turtles, user_bet)



screen.exitonclick()