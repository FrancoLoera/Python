"""
GUI con:
- Posición Place
- Fuente personalizada
- Labels
- Entrys
- Button commands
- Valores relativos
"""
from tkinter import *
from tkinter.font import Font
    
def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    resultado = int(n1) + int(n2)
    txt3.delete(0,"end")
    txt3.insert(0, resultado)

root = Tk()
root.geometry("600x300")
root.title("Primer interfaz")

root.configure(background="#FAEBD7")

myFont = Font(size=8, family="TW Cen MT")

lbl1 = Label(root, text="PRIMER NÚMERO", font=myFont, bg="#8B4513", fg="white")
lbl1.place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.1)

lbl2 = Label(root, text="SEGUNDO NÚMERO", font=myFont, bg="#8B4513", fg="white")
lbl2.place(relx=0.01, rely=0.21, relwidth=0.3, relheight=0.1)

lbl3 = Label(root, text="RESULTADO", font=myFont, bg="#8B4513", fg="white")
lbl3.place(relx=0.01, rely=0.61, relwidth=0.3, relheight=0.1)

txt1 = Entry(root, fg="black", font=myFont)
txt1.place(relx=0.35, rely=0.01, relwidth=0.3, relheight=0.1)

txt2 = Entry(root, fg="black", font=myFont)
txt2.place(relx=0.35, rely=0.21, relwidth=0.3, relheight=0.1)

txt3 = Entry(root, fg="black", font=myFont)
txt3.place(relx=0.35, rely=0.61, relwidth=0.3, relheight=0.1)

btnResultado = Button(root, text="Sumar", bg="black", fg="white", command=fnSuma)
btnResultado.place(relx=0.35, rely=0.41, relwidth=0.3, relheight=0.1)

root.mainloop()