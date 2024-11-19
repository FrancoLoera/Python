class Auto():
    def __init__(self, state):
        self.estado = state
        
    def encender(self):
        self.estado = "encendido"
        print("El auto está encendido")
        
    def conducir(self):
        if (self.estado == "apagado"):
            self.encender()
        print("Conduciendo el auto")
        
auto = Auto("apagado")
auto.conducir()

#Clases abstractas
#abc es una librería que nos permite utilizar los métodos y clases abstractas
#Las métodos de las clases abstractas no pueden ser usados por sus clases, mas sí por aquellas clases que utilicen esa clase como "plantilla"
from abc import ABC, abstractclassmethod


class Persona(ABC):
    #Si no "heredamos" de la clase ABC, @abstractclassmethod no serviría de nada
    @abstractclassmethod
    def __init__(self, name, age, gender, job, activity):
        self.nombre = name
        self.edad = age
        self.genero = gender
        self.actividad = activity
        
    @abstractclassmethod
    def hacer_Actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

#Si intentaramos crear una instancia de la clase Persona, nos mostraría un error debido a que es una clase abstracta (no es posible crear instancias de estas)
"""franco = Persona("Franco", 18, "Masculino", "Programador")"""

class Estudiante(Persona):
    def __init__(self, name, age, gender, activity):
        super().__init__(self, name, age, gender, activity)
        
    def hacer_Actividad(self):
        print(f"Estoy estudiando {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, name, age, gender, activity):
        super().__init__(self, name, age, gender, activity)
        
    def hacer_Actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")
            
franco = Estudiante("Franco", 18, "H", "Programación")
franco.presentarse()
franco.hacer_Actividad()

denis = Trabajador("Denis", 18, "Masculino", "Programación")
denis.presentarse()
denis.hacer_Actividad()