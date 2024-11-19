from tkinter import *

def iniciar_arrastre(event):
    global obj_seleccionado
    obj_seleccionado = canvas.find_closest(event.x, event.y)
    
def terminar_arrastre(event):
    global obj_seleccionado
    #Si el objeto es distinto de None
    if obj_seleccionado:
        x, y = event.x, event.y
        #Move parte del origen del objeto, por eso se debe restar las coordenadas del objeto antes de moverse
        canvas.move(obj_seleccionado, x - canvas.coords(obj_seleccionado)[0], y - canvas.coords(obj_seleccionado)[1])
        obj_seleccionado = None

root = Tk()
root.title("XGUI 12.1 - Canvas (Texto/Arrastrable)")
root.geometry("600x400")

canvas = Canvas(root, width=500, height=300)

"""canvas.create_text(150, 50, text="Aprendiendo Canvas", fill="black", justify="center")
canvas.pack(fill="both", expand=True)"""

obj_seleccionado = None

rectangulo = canvas.create_rectangle(100, 100, 200, 200, fill="lightblue", tags="rectangulo")

canvas.tag_bind("rectangulo", "<ButtonPress-1>", iniciar_arrastre)
canvas.tag_bind("rectangulo", "<ButtonRelease-1>", terminar_arrastre)

canvas.pack()

root.mainloop()