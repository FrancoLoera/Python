#Decoradores
#Tenemos nuestra función saludo que simplemente dice "Hola Franco"
"""def saludo():
    print("Hola Franco")"""
    
#Nuestra función decoradora toma la función saludo como argumento ya que la modificará
def decorador(funcion):
    #Creamos dentro una nueva función que será la función que obtendremos
    def funcion_Modificada():
        #Realizamos los cambios aquí adentro, en este caso solamente agregamos dos mensajes
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    #Retornamos nuestra función una vez modificada
    return funcion_Modificada
    
#Una función decoradora sirve para realizar procesos antes y después de la función
#Transformamos saludo_Modificado de variable a función
"""saludo_Modificado = decorador(saludo)
saludo_Modificado()"""

#Decorador óptimo
@decorador
def saludo():
    print("Hola gente")
#Realiza lo mismo que arriba, pero elimina el tener que asignarlo a una nueva variable    
saludo()

#Decorador @Property
class Persona():
    def __init__(self, name, age):
        self.__nombre = name
        self.__edad = age
    
    #Primer decorador
    #Nos permite asemejar una función a una propiedad, permitiendonos evitar el colocar () al llamar la función
    @property
    def nombre(self):
        return self.__nombre
        #Que retorne self.__nombre es equivalente a retornar funcion_Modificada
    
    #Segundo decorador
    #Creamos un setter que toma por valor otra función
    @nombre.setter
    def nombre(self, new_Name):
        self.__nombre = new_Name
        
    #Tercer decorador
    @nombre.deleter
    def nombre(self):
        del self.__nombre
        
franco = Persona("Franco", 18)
#Llamamos la función sin necesidad de colocar ()
print(franco.nombre)

franco.nombre = "Denis"
print(franco.nombre)

class Animal():
    def __init__(self, name):
        self.__nombre_Animal = name
      
    #Getter  
    @property
    def nombre_A(self):
        return self.__nombre_Animal
    
    #Setter
    @nombre_A.setter
    def nombre_A(self, new_Aname):
        self.__nombre_Animal = new_Aname
        
    @nombre_A.deleter
    def nombre_A(self):
        del self.__nombre_Animal
        
perrito = Animal("Larry")
print(perrito.nombre_A)

perrito.nombre_A = "Luka"

print(perrito.nombre_A)

#Si intentaramos eliminar el atributo sin el deleter existente, nos mencionaría que hace falta el deleter
del perrito.nombre_A
#El deleter funciona debido a que trabaja de forma interna en nuestra clase

#Si intentamos imprimirlo nos indicará que no se puede imprimir debido a que ya no existe
"""print(perrito.nombre_A)"""