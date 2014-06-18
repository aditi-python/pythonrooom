# author: aditi-python

import turtle
t = turtle.Turtle()
angle = 71

numbers = (10, 200)
colors = ("red" , "blue" , "pink" , "purple" , "yellow", "green" , "orange")

for number in numbers:
	for color in colors:
		t.color(color)
		t.forward(100)
		t.left(angle)