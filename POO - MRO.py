class A():
    pass
    """def hablar(self):
        print("Hola desde A")"""
        
class F():
    def hablar(self):
        print("Hola desde F")
        
class B(A):
    pass
    """def hablar(self):
        print("Hola desde B")"""
        
class C(F):
    pass
    """def hablar(self):
        print("Hola desde C")"""
        
class D(B,C):
    pass
    """def hablar(self):
        print("Hola desde D")"""
        
d = D()
#Para saber qué método se imprimirá debemos tomar en cuenta el Método de Resolución de Orden
#Primero se busca en la Clase D (derivada de B y C), como no encuentra el método se dirige a la primera de sus clases padre, la clase B
#Ahora, dentro de B se búsca el método, al no encontrarlo se dirige a su clase padre, la Clase A
#En caso de no encontrarlo en A, volveríamos a la Clase D, para luego entrar a la Clase C, la otra clase padre de D
#Finalmente, si no lo encuentra en C, lo buscaría en F
d.hablar()

class SA():
    pass
    def saludo(self):
        print("Hola desde SA")
        
class SX():
    def saludo(self):
        print("Hola desde SX")
        
class SB(SA):
    def saludo(self):
        print("Hola desde SB")
        
class SC(SA):
    pass
    """def saludo(self):
        print("Hola desde SC")"""
        
class SF(SC,SB):
    pass
    """def saludo(self):
        print("Hola desde SF")"""
    

S = SF()
S.saludo()

#El método .mro() únicamente funciona en clases, no en instancias como S
print(f"Orden para la impresión de clases: {SF.mro()}")

#Para especificar de dónde queremos sacar el método escribirmos:
SA.saludo(S)
#SA es de donde queremos sacar el método y S es el objeto que sirve como self

#Ejercicios II - 1 - Crear dos clases: Persona y Estudiante
#La clase persona tendrá los atributos nombre y edad y un método que imprima el nombre y la edad
#La clase estudiante heredara la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado
#Usar super en el método init para reutilizar Persona. Luego crear una instancia de Estudiante e imprimir sus atributos y sus métodos
class Persona():
    def __init__(self, name, age):
        self.nombre = name
        self.edad = age
        
    def datos(self):
        print(f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grado = grade
        
    def estudia(self):
        print(f"estoy en {self.grado} grado")
        
estudiante = Estudiante("Franco", 18, 2)
estudiante.datos()
estudiante.estudia()

#Ejercicios II - 2 -
#Crear 3 clases: Animal, Mamífero y Ave
#La clase Animal debe tener un método llamado 'comer'
#La clase Mamífero debe tener un método llamado 'amamantar'
#La clase Ave un método llamado 'volar'
#Crear una clase Murcielago que herede Mamífero y Ave
#Jugar con el orden MRO y al usar .super()

class Animal():
    def comer(self):
        print("Estoy comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Estoy amamantando")
        
class Ave(Animal):
    def volar(self):
        print("Estoy volando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.volar()
murcielago.comer()
murcielago.amamantar()