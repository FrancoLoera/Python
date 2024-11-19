from tkinter import *

root = Tk()
root.title("XGUI 12.1 - Canvas (figuras)")
root.geometry("600x400")

canvas = Canvas(root, width=500, height=300, bg="lightpink")

#(Posición x, posición y, ancho, alto, fondo, color del borde, ancho del borde)
rectangulo = canvas.create_rectangle(50, 50, 200, 100, fill="lightyellow", outline="black", width=5)
#Se mueve conforme a su posición de origen
canvas.move(rectangulo, 50, 50)

#Cordenadas esquina superior izquierda(w, x)
#Cordenadas esquina inferior derecha (y, z). Considera su posición desde el origen absoluto
canvas.create_oval(200, 50, 300, 150, fill="black", outline="lightblue", width=3) #Ovalo de 100x100
#Se crea vértice por vértice
canvas.create_polygon(100, 100, 150, 50, 200, 100, 150, 150, fill="red", outline="black", width=2)
#Dash (tamaño de las lineas punteadas, espaciado) | Capstyle (borde)
canvas.create_line(100, 200, 300, 200, fill="purple", width=4, dash=(5, 2), capstyle="round") #El dash es inútil por el ancho y el estilo de línea

canvas.pack()

root.mainloop()