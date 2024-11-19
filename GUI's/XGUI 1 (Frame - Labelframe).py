#Propiedades de ventana
#Frame
#Label frame
from tkinter import *

def cambio():
    color1 = frm1["background"]
    color2 = frm2["background"]
    frm1.configure(bg=color2)
    frm2.configure(bg=color1)

    if color1 == "beige":
        btn1.configure(bg="white", fg="black")
    else:
        btn1.configure(bg="black", fg="white")

root = Tk()

#Posibles configuraciones
"""root.title("Otro curso")
root.geometry("600x400+500+250")
root.minsize(400, 200)
root.maxsize(1000, 800)
root.configure(bg="lightblue")
root.resizable(False, True)
root.attributes("-alpha", 0.9)"""

root.title("Ventana principal")
root.geometry("600x400")
root.configure(bg="lightblue")

frm1 = Frame(root)
frm1.configure(width=300, height=200, bg="beige", bd=5)
frm1.pack()

frm2= Frame(frm1)
frm2.configure(width=100, height=100, bg="black", bd=5)
frm2.pack()

btn1 = Button(frm1, text="Cambiar", command= cambio, bg="white", fg="black")
btn1.pack(pady=5)

lblFrm = LabelFrame(root, text="Título LF", bg="beige")
lblFrm.configure(width=100, height=80)
lblFrm.pack()

root.mainloop()