from tkinter import *

root = Tk()

texto = Text(root)

scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")

#yview sirve para que el texto se desplace cuando la barra lo hace
scroll.config(command=texto.yview)
#el método set sirve para que el scroll no vuelva al punto de inicio cuando lo soltemos
texto.config(yscrollcommand=scroll.set)
texto.pack(side="left", fill="both", expand=True)

root.mainloop()