from tkinter import *

class FrmSuma(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def suma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        
        resultado = int(n1) + int(n2)
        
        self.txt3.delete(0, "end")
        self.txt3.insert(0, resultado)
        
    def create_widgets(self):
        self.lbl1 = Label(self, text="Primer Número:", bg="black", fg="white")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.lbl2 = Label(self, text="Segundo Número:", bg="black", fg="white")
        self.lbl2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.lbl3 = Label(self, text="Resultado:", bg="gray")
        self.lbl3.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        
        self.txt1 = Entry(self)
        self.txt1.grid(row=0, column=1)
        
        self.txt2 = Entry(self)
        self.txt2.grid(row=1, column=1)
        
        self.txt3 = Entry(self)
        self.txt3.grid(row=3, column=1)
        
        self.btn1 = Button(self, bg="green", fg="white", text="Sumar", command=self.suma)
        self.btn1.grid(row=2, columnspan=2)
        
root = Tk()
root.wm_title("GUI POO")
root.wm_geometry("600x300")
app = FrmSuma(root)
app.mainloop()