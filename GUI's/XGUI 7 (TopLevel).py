#Toplevel
from tkinter import *

root = Tk()
root.title("XGUI 7 - TOPLEVEL")
root.geometry("600x400+50+50")

#Se abrirá la ventana por default
top1 = Toplevel(root)
top1.title("Ventana Top 1")
top1.geometry("300x200+100+100")

#Puede abrir varias a la vez
def abrir_top():
    top2 = Toplevel(root, relief=FLAT)
    top2.title("Ventana Top 2")
    top2.geometry("300x200+100+100")
    lbl1 = Label(top2, text="Ventana TopLabel")
    lbl1.pack()

def cerrar_top():
    top1.destroy()

btn1 = Button(root, text="Abrir ventana", command=abrir_top)
btn1.pack()

btn2 = Button(root, text="Cerrar ventana", command=cerrar_top)
btn2.pack()

root.mainloop()