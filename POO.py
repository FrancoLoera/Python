#Clases y Objetos
class Celular():
    #Método constructor (función para atributos fijos)
    def __init__(self, mar, mod, cam):
        self.marca = mar
        self.modelo = mod
        self.camara = cam
        
    def mensaje(self):
        print(f"Este mensaje se está mostrando desde un {self.marca} {self.modelo}")
        
#Atributos de instancia
celular1 = Celular("Samsung", "JA34X", "30MP")
celular2 = Celular("Apple", "Iphone X", "50MP")

#Llamada del método
celular1.mensaje()

#Ejercicios I- Crear una clase estudiante con los atributos Nombre, Edad y Grado. Contaremos con un método estudiar() que mostrará "el estudiante (nombre) está estudiando". Crear un objeto Estudiante y usar el método estudiar(). El usuario brinda los atributos
class Estudiante():
    def __init__(self, name, age, grade):
        self.nombre = name
        self.edad = age
        self.grado = grade
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")
        
    def no_Estudiar(self):
        print(f"El estudiante {self.nombre} ya no está estudiando")
        
nombre = input("¿Cuál es su nombre?: ")
edad = input("¿Cuál es su edad?: ")
grado = input("¿Cuál es su grado?: ")

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE\n
      Nombre: {estudiante1.nombre}
      Edad: {estudiante1.edad}
      Grado: {estudiante1.grado}
      """)

salida = False
while (salida == False):
    estudiar = input()
    
    if estudiar.lower() == "estudiar":
        estudiante1.estudiar()
    elif estudiar.lower() == "no estudiar":
        salida = True
        
estudiante1.no_Estudiar()