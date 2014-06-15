# author: aditi-python

import turtle
t = turtle.Turtle()

numbers = range(10, 200 )
colors = ["red" , "blue" , "green" , "orange" , "yellow" ]

for number in numbers:
	for color in colors:
		t.color(color)
		t.forward(5)
		t.left(number / 5)