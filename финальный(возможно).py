import turtle
import math
screen = turtle.Screen()
screen.title("Интерактивная геометрическая программа")
pen = turtle.Turtle()
def draw_square(side_length):
    """Рисует квадрат со стороной side_length."""
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)
def draw_equilateral_triangle(side_length):
    """Рисует равносторонний треугольник со стороной side_length."""
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)
def draw_polygon(sides, side_length):
    """Рисует многоугольник с sides сторонами."""
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(side_length)
        pen.left(angle)
def draw_circle_polygon(radius, sides):
    """Рисует многоугольник, вписанный в окружность радиуса radius."""
    side_length = 2 * radius * math.sin(math.pi / sides)
    draw_polygon(sides, side_length)
def main_menu():
    print("Выберите фигуру:")
    print("1. Квадрат")
    print("2. Треугольник")
    print("3. М regular polygon (многоугольник)")
    choice = input("Введите номер: ")
    if choice == '1':
        length = int(input("Введите длину стороны: "))
        draw_square(length)
    elif choice == '2':
        length = int(input("Введите длину стороны: "))
        draw_equilateral_triangle(length)
    elif choice == '3':
        sides = int(input("Введите количество сторон: "))
        radius = float(input("Введите радиус вписанной окружности: "))
        draw_circle_polygon(radius, sides)
    else:
        print("Некорректный выбор.")

main_menu()

turtle.done()
