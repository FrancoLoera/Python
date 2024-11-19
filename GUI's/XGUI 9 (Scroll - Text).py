#Text
#Scrolledtext
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def copiar():
    txt1.event_generate("<<Copy>>")
    
def cortar():
    txt1.event_generate("<<Cut>>")
    
def pegar():
    txt1.event_generate("<<Paste>>")

root = Tk()
root.title("XGUI 9 - Text y ScrolledText")
root.geometry("600x400")

#Wrap word evita colocar palabras "cortadas". Coloca la palabra en el renglón inferior
txt1 = Text(root, wrap="word", width=20, height=20)
txt1.pack()

#Texto por default
#"resaltado" es la etiqueta que le brindará estilos
txt1.insert("1.0", "Este es el texto inicial")
txt1.insert("end", "\n\nEste es el texto final", "resaltado")

txt1.delete("1.0", "2.0")

#Configuración del texto mediante etiquetas
txt1.tag_configure("resaltado", foreground="blue")

btn1 = Button(root, text="Copiar", command=copiar)
btn1.pack()

btn2 = Button(root, text="Cortar", command=cortar)
btn2.pack()

btn3 = Button(root, text="Pegar", command=pegar)
btn3.pack()

#Scrolled text
"""scroll_text1 = ScrolledText(root, wrap="word", width=20, height=20)
scroll_text1.pack()"""

root.mainloop()