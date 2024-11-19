from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def on_select(event):
    print(messagebox.showinfo(title="Elemento Seleccionado", message=f"Seleccionado: {cbox.get()}"))

root = Tk()
root.title("XGUI 10 - ComboBox")
root.geometry("600x400")

cbox = Combobox(root, width=10, height=10, background="black", foreground="white")
cbox.pack()

elements = ["Elemento 1", "Elemento 2", "Elemento 3"]
cbox["values"] = elements

#Para actualizar los elementos del Combobox se deben actualizar los elementos de la lista y asignar nuevamente la lista al Combobox
elements.insert(0, "Elemento 0")
cbox["values"] = elements

elements.pop(0)
cbox["values"] = elements

cbox.bind("<<ComboboxSelected>>", on_select)

root.mainloop()