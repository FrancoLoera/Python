#Variables de control (StringVar, IntVar, DoubleVar, BooleanVar)
#Método trace (detecta algún tipo de cambio y ejecuta una función)
#Scale (Control deslizante)
from tkinter import *

root = Tk()
root.title("XGUI 6")
root.geometry("300x200")

#StringVar
"""#Setear el valor sirve para cuando no queremos declarar la variable con un valor
str_control = StringVar(value="Hola")
str_control.set("Hola mundo (value)")
print(str_control.get())

txt1 = Entry(root, textvariable=str_control).pack()

#Función callback
lbl1 = Label(root)
lbl1.pack()

def actualizar_lbl(*args):
    lbl1.config(text=str_control.get())
    
#El método trace nos sirve para los posibles cambios
#Cada vez que se detecte cualquier cambio (w), se ejecutará el 2do parámetro de trace
str_control.trace("w", actualizar_lbl)"""

#IntVar
"""int_control = IntVar()

rdo1 = Radiobutton(root, text="Opción 1", variable=int_control, value=1)
rdo2 = Radiobutton(root, text="Opción 2", variable=int_control, value=2)
rdo1.pack()
rdo2.pack()

chk1 = Checkbutton(root, text="Aceptar", variable=int_control, onvalue=1, offvalue=0)
chk1.pack()

def actualizar(*args):
    print(int_control.get())
    
int_control.trace("w", actualizar)"""

#DoubleVar
dbl_control = DoubleVar()

#Control deslizante
#Resolution indica la magnitud en la que se deslizará el control
scl1 = Scale(root, variable=dbl_control, from_=0, to=10, resolution=0.1, orient=HORIZONTAL)
scl1.pack()

#BooleanVar
bln_control = BooleanVar(value=True)

chk1 = Checkbutton(root, text="Aceptar", variable=bln_control)
chk1.pack()

def actualizar(*args):
    print(bln_control.get())
    
bln_control.trace("w", actualizar)

root.mainloop()