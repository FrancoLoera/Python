#Eventos
#Bindeos
#For en 1 línea
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

#Evento al clickear
def on_click(event):
    print(messagebox.showinfo(message="Botón presionado"))

#Evento al presionar una tecla  
def on_key_press(event):
    if event.char == "a":
        print(messagebox.showinfo(message="Tecla 'a' presionada"))
        
#Evento al redimensionar (imprime al cambiar de posición y dimensiones)
"""def on_resize(event):
    print(messagebox.showinfo(message=f"Ventana reconfigurada. Medidas: {event.width} x {event.height}"))"""

#Evento al mover mouse (dentro del frame de la ventana)
"""def on_mouse_move(event):
    print(f"Posición del mouse: X: {event.x} Y: {event.y}")"""

btn1 = Button(root, text="CLICK")
btn1.pack()
#Click Izquierdo
btn1.bind("<Button-1>", on_click)
#Scroll Click
btn1.bind("<Button-2>", on_click)
#Click Derecho
btn1.bind("<Button-3>", on_click)

root.bind("<KeyPress>", on_key_press)

"""root.bind("<Configure>", on_resize)"""

"""root.bind("<Motion>", on_mouse_move)"""

def on_click2(event):
    print(messagebox.showinfo(message=f"Botón {event.widget['text']} presionado"))

#Ciclo for para crear 3 botónes
btns = [Button(root, text=f"Botón {i}") for i in range(3)]

#Ciclo for para desempaquetar y asignar evento
for btn in btns:
    btn.pack()
    btn.bind("<Button-1>", on_click2)

root.mainloop()