#Métodos Especiales o Dunder
class Persona:
    def __init__(self, name, age):
        self.nombre = name
        self.edad = age
    
    #Utilizamos __str__ para que nos devuelva el texto indicado, en caso de no aplicarlo, nos retornaría la ubicación de la clase Persona
    def __str__(self):
        return f"PERSONA \nNombre = {self.nombre} \nEdad = {self.edad}"
    
    #Aquí es necesario colocarlo como código debido a que __repr__ busca representarlo como tal (convertimos el contenido en una string para crear un objeto)
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    #Sobrecarga de operadores (definir como actuarán las operaciones de nuestras clases —por ejemplo Persona + Persona—)
    def __add__(self, otro):
        nuevo_Valor = self.edad + otro.edad
        return Persona(self.nombre + f" {otro.nombre}", nuevo_Valor)
    
franco = Persona("Franco", 18)
print(franco)

#Guardamos la representación de __repr__
repre = repr(franco)
#Creamos la representación de __repr__
result = eval(repre)
#eval() evalúa el contenido de un str para realizar posibles operaciones (en este caso lo toma como la declaración de un objeto)

print(result.edad)

denis = Persona("Denis", 18)
nueva_Persona = franco + denis
print(f"Nueva persona: {nueva_Persona.nombre} de {nueva_Persona.edad} de edad")

