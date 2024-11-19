"""
GUI (derivado 1) con:
- *Posición Pack
- Grid (Posición)
- Parámetros Grid
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
root.title("Segunda GUI")

root.configure(background="#FAEBD7")

myFont = Font(size=8, family="TW Cen MT")

lbl1 = Label(root, text="PRIMER NÚMERO", font=myFont, bg="#8B4513", fg="white")
#lbl1.pack(pady=5)
lbl1.grid(row=0, column=0, padx=8, pady=5, sticky="nsew")
lbl1.rowconfigure(0, weight=1)
lbl1.columnconfigure(0, weight=1)

txt1 = Entry(root, fg="black", font=myFont)
#txt1.pack(pady=5)
txt1.grid(row=0, column=1, sticky="w")

lbl2 = Label(root, text="SEGUNDO NÚMERO", font=myFont, bg="#8B4513", fg="white")
#lbl2.pack(pady=5)
lbl2.grid(row=1, column=0, padx=8, pady=5, sticky="nsew")

txt2 = Entry(root, fg="black", font=myFont)
#txt2.pack(pady=5)
txt2.grid(row=1, column=1, sticky="w")

lbl3 = Label(root, text="RESULTADO", font=myFont, bg="#8B4513", fg="white")
#lbl3.pack(pady=5)
lbl3.grid(row=3, column=0, padx=8, pady=5, sticky="nsew")

txt3 = Entry(root, fg="black", font=myFont)
#txt3.pack(pady=5)
txt3.grid(row=3, column=1, sticky="w")

btnResultado = Button(root, text="Sumar", bg="black", fg="white", command=fnSuma)
#btnResultado.pack(pady=5)
btnResultado.grid(row=2, columnspan=2)

root.mainloop()