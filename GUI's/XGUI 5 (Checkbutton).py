#Checkbutton (varias selecciones)
#Estado de un Button
from tkinter import *
from tkinter import messagebox

def on_checkbutton_change():
    print(messagebox.showinfo(message="El checkbutton cambió"))
    
def available_button():
    #Método get necesario para determinar valor booleano de var_control
    if var_control3.get():
        btn1.configure(state="normal")
    else:
        btn1.configure(state="disabled")

root = Tk()
root.title("XGUI 5")
root.geometry("300x200")

#Se crean varias variables de control ya que en un Checkbutton se pueden seleccionar varias opciones
var_control1 = BooleanVar()
var_control2 = BooleanVar()
var_control3 = BooleanVar()

chk1 = Checkbutton(root, text="Opción 1", font=("Arial", 12, "bold"), variable=var_control1, command=on_checkbutton_change)
chk2 = Checkbutton(root, text="Opción 2", font=("Arial", 12, "bold"), variable=var_control2, command=on_checkbutton_change)
chk3 = Checkbutton(root, text="Habilitar botón", font=("Arial", 12, "bold"), variable=var_control3, command=available_button)
chk1.pack()
chk2.pack()
chk3.pack()

#Parámetro state para habilitar/deshabilitar botón
btn1 = Button(root, text="Click", state="disabled")
btn1.pack()

root.mainloop()