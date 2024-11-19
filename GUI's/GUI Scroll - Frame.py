from tkinter import *

root = Tk()
root.title("GUI - Scroll - Frame")
root.geometry("800x600")

wrapper1 = Frame(root, bg="black")
wrapper2 = Frame(root, bg="blue")
wrapper1.pack(fill="both", expand=True, padx=10, pady=10)
wrapper2.pack(fill="both", expand=True, padx=10, pady=10)

canvawrapp = Canvas(wrapper1, bg="gray")
canvawrapp.pack(side=LEFT, fill="both", expand=True)

#El comando sirve para el desplazamiento
scroll = Scrollbar(wrapper1, orient="vertical", command=canvawrapp.yview)
scroll.pack(side=RIGHT, fill=Y)

canvawrapp.configure(yscrollcommand=scroll.set(0, 0))
canvawrapp.bind("<Configure>", lambda e: canvawrapp.configure(scrollregion = canvawrapp.bbox("all")))

frame1 = Frame(canvawrapp)
canvawrapp.create_window((0, 0), window=frame1, anchor="nw")

for i in range(30):
    Button(frame1, text=f"Botón {i}", width=20).pack()

root.mainloop()