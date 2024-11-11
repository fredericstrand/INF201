import turtle

def draw_heart(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()

    for _ in range(2):
        turt.circle(100, 180)

    turt.left(120)
    turt.circle(-50, 180)

    turt.penup()
    turt.home()
    turt.pendown()

window = turtle.Screen()
heart = turtle.Turtle()
draw_heart(heart, 0, -200)

window.mainloop()
