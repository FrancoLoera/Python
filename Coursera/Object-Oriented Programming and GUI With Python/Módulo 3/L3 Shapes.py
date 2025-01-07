import tkinter as tk
from turtle import RawTurtle, TurtleScreen

def draw_bulls_eye(turtle):
    colors = ["red", "white"]
    radius = 100
    for i in range(5): 
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.fillcolor(colors[i % 2])
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        radius -= 20

def create_gui():
    root = tk.Tk()
    root.title("Bull's-Eye")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    screen = TurtleScreen(canvas)
    turtle = RawTurtle(screen)
    turtle.speed(0)

    draw_button = tk.Button(root, text="Draw Bull's-Eye", command=lambda: draw_bulls_eye(turtle))
    draw_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
