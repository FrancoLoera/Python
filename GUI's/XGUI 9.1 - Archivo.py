from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
#askopenfilename sirve para abrir un archivo
#asksaveasfilename sirve para guardar un archivo

def abrir_archivo():
    #Método para abrir archivo
    archivo = askopenfilename()
    #Si encuentra el archivo, se borrará el contenido del scroll_text para mostrar el del archivo
    if archivo:
        scroll_text1.delete(1.0, "end")
        with open(archivo, "r") as file:
            #Inserta en el scroll_text el contenido leído en el archivo
            scroll_text1.insert(1.0, file.read())
            
def guardar_archivo():
    archivo = askopenfilename()
    if archivo:
        with open(archivo, "w") as file:
            file.write(scroll_text1.get(1.0, "end"))
            
root = Tk()
root.geometry("600x400")

scroll_text1 = ScrolledText(root, wrap="word")
#Expand=True    Si la ventana crece, el widget adapta su posición.
#Fill="both"    Si la ventana crece, el widget también.
scroll_text1.pack(expand=True, fill="both")

btn1 = Button(root, text="Abrir", command=abrir_archivo)
btn1.pack(side="left")

btn2 = Button(root, text="Guardar", command=guardar_archivo)
btn2.pack(side="left")

root.mainloop()