#Datum poslední úpravy: 23.03.2021

from turtle import forward, left, right, clear, exitonclick, penup, pendown

#srdce z hexagonů
penup()
left(180)
forward(40)
left(180)
pendown()
#1. hexagon
for n in range(3):
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    right(60)
    forward(20)
    right(60)

for n in range(3):
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
#posun
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)



#2. hexagon
for n in range(3):
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    right(60)
    forward(20)
    right(60)

for n in range(3):
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
#posun
penup()
right(90)
right(30)
forward(80)
right(60)
forward(20)
left(180)
pendown()

#3. hexagon
for n in range(3):
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    right(60)
    forward(20)
    right(60)

for n in range(3):
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
#posun
right(120)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)

#4.hexagon
for n in range(3):
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    left(60)
    forward(20)
    right(60)
    forward(20)
    right(60)

for n in range(3):
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    right(60)
    forward(20)
    left(60)
    forward(20)
    left(60)

#pravá část srdce obrys
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)

#pravá část srdce výplň
left(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
#
right(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)

#levá část srdce obrys
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)

#levá část srdce výplň
right(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
right(60)
forward(20)
left(180)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
left(180)
forward(20)
left(60)
forward(20)

#
penup()
left(60)
left(90)
forward(90)
right(90)
forward(60)



#posunutí ze středu na začátek 1. řádku
penup()
left(180)
forward(440)
right(90)
forward(200)


exitonclick()
