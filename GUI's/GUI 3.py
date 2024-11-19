"""
- Frames
- Messagebox
- Distribución y posicionamiento de Columnas, Filas y Widgets
"""
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = Tk()
root.geometry("600x300")
root.title("Frames")

customFont = Font(family="Arial", size="10", weight="bold")

frame1 = Frame(root)
frame1.pack(expand=True, fill='both')

frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.rowconfigure(0, weight=1)

frame2 = Frame(root, bg="brown")
frame2.pack(expand=True, fill='both')

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

button1 = Button(frame1, font=customFont, text="Rojo".upper(), bg="red", fg="white", command=
                 lambda: print(messagebox.showinfo(message="Este es el botón rojo", title="Información")))
button1.grid(row=0, column=0, sticky="nsew", pady=15, padx=15)

button2 = Button(frame1, font=customFont, text="Verde".upper(), bg="green", fg="white", command=
                 lambda: print(messagebox.showinfo(message="Este es el botón verde", title="Información")))
button2.grid(row=0, column=1, sticky="nsew", pady=15, padx=15)

button3 = Button(frame1, font=customFont, text="Azul".upper(), bg="blue", fg="white", command=
                 lambda: print(messagebox.showinfo(message="Este es el botón azul", title="Información")))
button3.grid(row=0, column=2, sticky="nsew", pady=15, padx=15)

button4 = Button(frame2, font=customFont, text="Negro", bg="black", fg="white", command=
                 lambda: print(messagebox.showinfo(message="Este es el botón negro", title="Información")))
button4.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

root.mainloop()