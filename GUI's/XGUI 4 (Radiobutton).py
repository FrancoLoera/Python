#Radiobutton (una sola selección)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("XGUI 4")
root.geometry("300x200")

"""rbtn1 = Radiobutton(root, text="Opcion 1", font=("Arial", 15, "bold"))
rbtn1.pack()"""

#Variable de control necesaria para poseer varios Radio buttons
var_control = IntVar()
#Value es el valor asignado a la variable de control
rbtn2 = Radiobutton(root, text="Rosa", variable=var_control, value=1)
rbtn3 = Radiobutton(root, text="Celeste", variable=var_control, value=2)
rbtn4 = Radiobutton(root, text="Amarillo", variable=var_control, value=3)
rbtn2.pack()
rbtn3.pack()
rbtn4.pack()

def seleccion():
    if (var_control.get() == 1):
        root.configure(bg="lightpink")
    elif (var_control.get() == 2):
        root.configure(bg="lightblue")
    elif (var_control.get() == 3):
        root.configure(bg="lightyellow")
    elif (var_control.get() == 4):
        root.configure(bg="green")
    elif (var_control.get() == 5):
        root.configure(bg="purple")
    elif (var_control.get() == 6):
        root.configure(bg="red")
    else:
        root.configure(bg="gray")

btn1 = Button(root, text="Cambiar Color", command=seleccion)
btn1.pack()

lbl1 = Label(root, text="CAMBIO ABSOLUTO", font=("Arial", 15, "bold"))
lbl1.pack()

#No se recomienda uso de lambda ya que todas las casillas se mantendrán activas
rbtn5 = Radiobutton(root, text="Verde", variable=var_control, value=4, command=seleccion)
rbtn6 = Radiobutton(root, text="Morado", variable=var_control, value=5, command=seleccion)
rbtn7 = Radiobutton(root, text="Rojo", variable=var_control, value=6, command=seleccion)
rbtn5.pack()
rbtn6.pack()
rbtn7.pack()

root.mainloop()