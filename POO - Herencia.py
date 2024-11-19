class Persona():
    def __init__(self, name, age, nacion):
        self.nombre = name
        self.edad = age
        self.nacionalidad = nacion
        
    def hablar(self):
        print("Hola, este es un pequeño saludo")

#Heredando de Persona() mediante Herencia simple
class Empleado(Persona):
    def __init__(self, name, age, nacion, work, salary):
        #Hereda lo que está después del método super()
        super().__init__(name, age, nacion)
        self.trabajo = work
        self.salario = salary
        
    def saludo(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad}, trabajo como {self.trabajo} y mi sueldo es de ${self.salario}")


roberto = Empleado("Roberto", 43, "Argentino", "Administrador", 10000)
roberto.saludo()
roberto.hablar()

#Para saber si cierta clase (x) es subclase de otra clase (y), utilizamos issubclass(x, y)
print(f"Roberto es una instancia de Empleado?: {isinstance(roberto, Empleado)}")