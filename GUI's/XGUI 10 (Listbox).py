from tkinter import *

def on_select(event):
    index = lbox.curselection()
    lbl1.config(text=f"CLICK \nSeleccionado: {lbox.get(index)}")
    
def on_double_click(event):
    index = lbox.curselection()
    lbl1.config(text=f"DOBLE CLICK \nSeleccionado: {lbox.get(index)}")

root = Tk()
root.title("XGUI 10 - ListBox")
root.geometry("600x400")

lbox = Listbox(root, width=20, height=5, fg="white", bg="black")
lbox.insert(END, "Elemento 1")
lbox.insert(END, "Elemento 2")
lbox.insert(END, "Elemento 3")
lbox.insert(0, "Elemento 0")
lbox.pack()

lbl1 = Label(root, text="Hola")
lbl1.pack()

#Un < para eventos específicos
#Doble < para eventos generales
lbox.bind("<<ListboxSelect>>", on_select)
lbox.bind("<Double-Button-1>", on_double_click)

root.mainloop()