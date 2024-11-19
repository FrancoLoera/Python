#Posicionamiento de label
#"Responsividad" de Label
#Asignar texto a un Label (elemento ["text"])
import tkinter
from tkinter import messagebox

"""def saludo(persona):
    print(messagebox.showinfo(message=f"Hola {persona}"))
    
def texto():
    cadena = txt1.get()
    lbl1["text"] = cadena
    print(messagebox.showinfo(message=f"Tu texto es: {cadena}"))"""

root = tkinter.Tk()

root.geometry("500x300")

#Label
lbl1 = tkinter.Label(root, text="Buenas")
#Posicionamiento del texto (inservible si el Label es responsivo)
lbl1.pack(side=tkinter.BOTTOM)
#Si usamos fill, debemos usar expand
lbl1.pack(fill=tkinter.BOTH, expand=True)

#Button
"""btn1 = tkinter.Button(root, text="Aceptar", padx=20, pady=20, command=lambda: print(messagebox.showinfo(message="Saludos")))
#Botón con función con argumentos
btn1 = tkinter.Button(root, text="Aceptar", padx=20, pady=20, command=lambda: saludo("Franco"))
btn1.pack()"""

#Conjunto 1
"""txt1 = tkinter.Entry(root, font="Arial 14")
txt1.pack()
#Label que se actualiza mediante función
lbl1 = tkinter.Label(root)
lbl1.pack()
btn1 = tkinter.Button(root, text="Aceptar", command=lambda: texto())
btn1.pack()"""

"""btn1 = tkinter.Button(text="Botón 1")
btn2 = tkinter.Button(text="Botón 2")
btn3 = tkinter.Button(text="Botón 3")

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)"""

root.mainloop()