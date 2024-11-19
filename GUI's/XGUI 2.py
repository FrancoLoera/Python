import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("XGUI 2")
root.geometry("300x200")

def actualizar():
    lbl1.config(text="Holasadasdas")
    
lbl1 = Label(root, text="Inicial")
lbl1.pack()

btn1 = Button(root, text="Comando", command=actualizar)
btn1.pack()

#Reloj
"""lbl1 = Label(root, text="LABEL")
lbl1.configure(text="NEW LABEL", bg="beige", font=("Arial", 20, "bold"))
lbl1.pack()
def actualizar():
    lbl1.config(text=time.strftime("%H:%M:%S"))
    #Realiza esto cada 1000 milisegundos
    root.after(1000, actualizar)
actualizar()"""

#Botón cambia label
"""btn1 = Button(root, text="Presiona", bg="beige", font=("Arial", 16, "bold"))
btn1.pack()
lbl1 = Label(root, text="Label base")
lbl1.pack()
def cambiar():
    if lbl1["text"] == "Label base":
        lbl1.configure(text="Botón presionado")
    else:
        lbl1.configure(text="Label base")
btn1.configure(command=cambiar)"""
#a
"""lbl1 = Label(root, text="TEXTO")
lbl1.pack()

txt1 = Entry(root)
txt1.pack()
#Texto por defecto
txt1.insert(0, "Default")

def guardar():
    lbl1.configure(text=txt1.get())

btn1 = Button(root, text="Cambiar", command=guardar)
btn1.pack()"""

root.mainloop()