import turtle
import math
wn = turtle.Screen()
wn.title("Геометрическая программа")
wn.setup(width=800, height=600)
drawer = turtle.Turtle()
drawer.speed(5)
def draw_square(side_length):
    for _ in range(4):
        drawer.forward(side_length)
        drawer.right(90)
def draw_equilateral_triangle(side_length):
    for _ in range(3):
        drawer.forward(side_length)
        drawer.left(120)
