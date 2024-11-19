#Menubutton
#Clase Menu
#Menú (barra)
#Menú contextual (click derecho)
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("XGUI 7 - TOPLEVEL")
root.geometry("300x200")

#Menubutton
"""def archivo():
    print(messagebox.showinfo(message="Archivo abierto"))

#Botón que mostrará el menú
mbtn1 = Menubutton(root, text="Archivo")
mbtn1.pack()

#Instancia a la que se le asignan los elementos del menú
mnu1 = Menu(mbtn1)
mbtn1.config(menu=mnu1)

#Elementos del menú
mnu1.add_command(label="Abrir")
mnu1.add_command(label="Cerrar")
mnu1.add_command(label="Archivo", command=archivo)"""

#Barra de menú
"""#Barra total
barra_menu = Menu(root)
root.config(menu=barra_menu)

#Elementos de la barra
archivo_menu = Menu(barra_menu)
info_menu = Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Información", menu=info_menu)

#Elementos contenidos en los elementos de la barra
archivo_menu.add_command(label="Nuevo Menu")
archivo_menu.add_command(label="Abrir Menu")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar Menu")

info_menu.add_command(label="Nueva Info")
info_menu.add_command(label="Abrir Info")
info_menu.add_separator()
info_menu.add_command(label="Cerrar Info")"""

#Menú contextual (Click derecho)
def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root, event.y_root)

#Tearoff sirve para colocar el elemento con "-- -- --"
menu_contextual = Menu(root, tearoff=0)

#Botónes del menu contextual
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")

txt1 = Entry(root)
txt1.pack()

txt1.bind("<Button-3>", mostrar_menu_contextual)

root.mainloop()