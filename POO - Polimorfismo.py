class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guag"
    
def hacer_Sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

#Polimorfismo de función (la función no cambia pero los argumentos sí, por ende es la misma función, pero actua de diversas formas)
hacer_Sonido(gato)
print(perro.sonido())

#Polimorfismo de herencia (en este polimorfismo las clases hijo heredan los métodos)