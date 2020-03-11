from turtle import *
# Draw Graph
# Set up gloves variables
gloves = [5,8,10,5,6,9,15,22,5,10,18,7]



total = 0
for index in range(len(gloves)):
    total = total + gloves[index]

# Produce x axis
goto(350,0)

penup()
goto(60, -50)
pendown()
write("Months", font=("Freemono", 20, "bold"))
penup()

# Produce y axis

goto(0,0)
pendown()
goto(0,250)
penup()
goto(-100, 50)
pendown()
write("Million\nGloves\nSold", align="center", font=("Freemono", 20, "bold"))
penup()

total = 0
position = 0
spacing = 30


goto(0,0)
pendown()
for index in range(len(gloves)):

    goto(position,gloves[index] * 10)
    position = position + spacing
    write(gloves[index], font=("Freemono", 10, "bold"))


penup()
position = 0
months = ["Jan ","Feb ","Mar ","Apr ","May ","Jun ","Jul ","Aug ","Sep ","Oct ","Nov ","Dec "]

for index in range(len(months)):

    goto(position,-15)
    write(months[index], font=("Freemono", 10, "bold"))
    position = position + spacing
