import turtle

def draw_circle():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_triangle():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_rectangle():
    turtle.penup()
    turtle.goto(-150, 50)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def main():
    turtle.speed(3)
    draw_circle()
    draw_triangle()
    draw_rectangle()
    turtle.done()

if __name__ == "__main__":
    main()
