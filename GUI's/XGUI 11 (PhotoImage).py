from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("XGUI 11 - (PhotoImage)")
root.geometry("600x400")

#Sin PIL
#Permite .gif y .png
"""imagens = PhotoImage(file="Rain.png", height=100, width=200)

lbl1 = Label(root, image=imagens)
lbl1.pack()

btn1 = Button(root, image=imagens)
btn1.pack()"""

#Con PIL (pillow)
imagenPil = Image.open("Pescadores.jpg")
#Las dimensiones son un conjunto
imagen_remix = imagenPil.resize((200, 100))
imagenTk = ImageTk.PhotoImage(imagen_remix)

#Cada cambio se guarda en una variable nueva
imagen_rotada = imagenPil.rotate(90)
imagen_rotada2 = imagen_rotada.resize((200, 100))
imagenTk2 = ImageTk.PhotoImage(imagen_rotada2)

lbl1 = Label(root, image=imagenTk)
lbl1.pack()

btn1 = Button(root, image=imagenTk2)
btn1.pack()

root.mainloop()