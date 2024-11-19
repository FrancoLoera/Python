#Entry no editable
#Estilos del Entry
#Grid con contenido responsivo
from tkinter import *

def incremento():
    valor = int(txt1.get()) + 1
    txt1.configure(state="normal")
    txt1.delete(0, "end")
    txt1.insert(0, valor)
    txt1.configure(state="readonly")

root = Tk()
root.title("Contador")
root.geometry("300x200")
root.configure(bg="gray90")

lbl1 = Label(root,
             text="Contador:",
             bg="gray90")
lbl1.grid(row=0, column=0, sticky="E")

#hthickness sirve para determinar el grosor, hbackground para el color por defecto y hcolor para el color al seleccionar el Entry
txt1 = Entry(root,
             highlightthickness=2,
             highlightbackground="orange",
             highlightcolor="orange",
             bd=0,
             justify="center"
             )
txt1.grid(row=0, column=1)
txt1.insert(0, "0")
txt1.configure(state="readonly")

btn1 = Button(root,
              text="+",
              command=incremento,
              width=5,
              bd=1,
              bg="orange"
              )
btn1.grid(row=0, column=2, sticky="W")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()