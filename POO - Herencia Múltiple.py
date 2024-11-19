class Persona():
    def __init__(self, name, age, nacion):
        self.nombre = name
        self.edad = age
        self.nacionalidad = nacion

class Artista():
    def __init__(self, hability):
        self.habilidad = hability
        
    def mostrar_Habilidad(self):
        print(f"Hola, mi habilidad es {self.habilidad}")
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, name, age, nacion, hability, salary, company):
        Persona.__init__(self, name, age, nacion)
        Artista.__init__(self, hability)
        self.salario = salary
        self.empresa = company
        
    def mostrar_Habilidad2(self):
        return f'{super().mostrar_Habilidad()}'
    
    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años, vivo en {self.nacionalidad}, me gusta {self.habilidad} y gano aproximadamente ${self.salario} mensuales en {self.empresa}")
    
empleado = EmpleadoArtista("Franco", 18, "Mexico", "Pintar", 5000, "Cloud Ink")
empleado.mostrar_Habilidad2()
empleado.presentar()
    
print(f"EmpleadoArtista es subclase de Artista?: {issubclass(EmpleadoArtista, Artista)}")
print(f"EmpleadoArtista es subclase de Persona?: {issubclass(EmpleadoArtista, Persona)}")