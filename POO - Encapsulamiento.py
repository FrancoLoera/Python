class MiClase():
    def __init__(self):
        #El primer guión bajo indica Private
        self._Atributo_Privado = "Valor"
        #Los primeros dos guiones bajos indican Muy privado
        self.__Atributo_Muy_Privado = "Valor oculto"
        
    def __hablar(self):
        print("Hola")
        
objeto = MiClase()
print(objeto._Atributo_Privado)
#Dará error si queremos llamarlo
"""print(objeto.__Atributo_Muy_Privado)"""

#Get Set
class Persona():
    def __init__(self, name, age):
        self.__nombre = name
        self.__edad = age
     
    #Getter
    #Creamos una función interna que sirve como un Get que obtiene el nombre    
    def get_Nombre(self):
        return self.__nombre
    
    #Setter
    def set_Nombre(self, new_Name):
        self.__nombre = new_Name

#Debido a que el Get trabaja de forma interna (dentro de la clase persona) no hay problema en la obtención del nombre
franco = Persona("Franco", 18)
nombre = franco.get_Nombre()
print(nombre)
#Si quisieramos acceder al nombre desde afuera, tendríamos un error
"""print(franco.__nombre)"""

franco.set_Nombre("Cloud")
print(franco.get_Nombre())
