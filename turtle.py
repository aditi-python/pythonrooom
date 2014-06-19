# author: aditi-python

import turtle
t = turtle.Turtle()
u = turtle.Turtle()
v = turtle.Turtle()
w = turtle.Turtle()

numbers = range(10, 50)
colors = ["red" , "blue" , "green" , "orange" , "yellow" ]

v.color("white")
w.color("white")
v.left(180)
w.left(180)
v.forward(20)
w.forward(20)


for number in numbers:
	for color in colors:
		t.color(color)
		t.forward(5)
		t.left(number / 5)
	
	
for number in numbers:
	for color in colors:
		u.color(color)
		u.forward(5)
		u.right(number / 5)
		
		
		
for number in numbers:
	for color in colors:
		w.color(color)
		w.forward(5)
		w.left(number / 5)
	
	
for number in numbers:
	for color in colors:
		v.color(color)
		v.forward(5)
		v.right(number / 5)
		
		
