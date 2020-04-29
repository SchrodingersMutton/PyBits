from random import *
from turtle import *
from tkinter import *
from time import *
from datetime import *

bgcolor("#330099")


screen = Screen()
screen.setup(800,580)

    
color('white')

questions = 20
question_no = 1
score = 0

while questions > 0:


    screen.bgpic('soph_maths.gif')
    
    timer = 3
    penup()
    goto(-350,00)
    pendown()
    color('yellow')
    write("Maths: Addition", font=("Freemono", 40, "bold"))
    penup()
    
    num_one = randint(1,30)

    num_two = randint(1,30)
    
    actual_answer = num_one + num_two
    
    goto(-350, -50)
    pendown()
    color('#81F5FF')
    write("Question " + str(question_no), font=("Freemono", 26, "bold"))
    
    penup()
    goto(-350, -100)

    
    write(str(num_one) + str(' + ') + str(num_two), font=("Freemono", 24, "bold"))

    if score > 0:
        goto(100,-200)
        color('#00FFFF')
        write("Score: " + str(score), font=("Freemono", 30, "bold")) 
    
    goto(350,100)
    my_answer = numinput("Answer", str(num_one) + str(' + ') + str(num_two), default=None, minval=None, maxval=None)

    
    try:
        entered_answer = my_answer
    except ValueError as ve:
        entered_answer = 0
        print("This isn't a number")

    if entered_answer == int(actual_answer):
        bgcolor("#FFFFFF")
        screen.bgpic('correct.gif')
        score = score + 1
        clear()
        goto(-290,250)
        color('#05ea02')
        write("Correct! The answer is " + str(actual_answer) + str("!"), font=("Freemono", 30, "bold"))

        goto(-200,200)
        color('blue')
        write("Your score is " + str(score), font=("Freemono", 30, "bold"))

        while timer > 0:
            timer -= 1
            sleep(1)
            
        else:
            clear()

    else:
        clear()
        bgcolor("#F9F9F9")
        screen.bgpic('incorrect.gif')
        goto(-290,250)
        color('red')
        write("Wrong! The answer is " + str(actual_answer) + str("!"), font=("Freemono", 30, "bold"))

        goto(-200,200)
        color('blue')
        write("Your score is " + str(score), font=("Freemono", 30, "bold"))

        while timer > 0:
            timer -= 1
            sleep(1)
            
        else:
            clear()

    questions = questions - 1
    question_no = question_no + 1
