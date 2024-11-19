#SRP
#Single Responsibility Principle
#Principio de responsabilidad única
#Una clase debe una única responsabilidad o tarea, si necesita realizar más, deberemos realizar otras clases que realicen las funciones necesarias

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    def agregar_Combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_Combustible(self):
        return self.combustible
    
    def usar_Combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_Combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_Combustible(distancia / 2)
            print("Has movido el vehículo")
        else:
            print("No hay suficiente combustible")
            
    def obtener_Posicion(self):
        return self.posicion
        
tanque = TanqueDeCombustible()
vehiculo = Auto(tanque)

print(vehiculo.obtener_Posicion())
print(vehiculo.mover(10))
print(vehiculo.obtener_Posicion())
print(vehiculo.mover(50))
print(vehiculo.obtener_Posicion())

#OCP
#Open/Closed Principle - Open for extension, closed for modify
#Principio de abierto/cerrado
#Las clases, módulos, funciones, etc. deben estar abiertas para las extensiones, pero cerradas para la modificación (podemos agregar más funciones, sin necesidad de cambiar el código)

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        #Raise sirve para brindar una excepción, NotImplementedError es un error derivado de no crear una subclase de esta clase "abstracta"
        raise NotImplementedError
    
#Evitamos la necesidad de modificar nuestra clase Notificador al implementar las funciones en otras clases
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
#LSP
#Liskov's Substitution Principle
#Principio de sustitución de Liskov
#Las clases hijas deben poder ser utilizadas en cualquier lugar que las clases padres lo puedan ser

# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    
# def hacer_Volar(ave = Ave):
#     return ave.volar()

# print(hacer_Volar(Pinguino()))

#En la clase Ave se deben colocar todas aquellas cosas que pueden hacer TODAS las aves
class Ave:
    pass

#Las cosas que pueden hacer TODAS las aves voladoras
class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVoladora(Ave):
    pass

#ISP
#Interface Segregation Principle
#Principio de segregación de la interfaz
#Ningún cliente debe ser forzado a las dependencias o "interfaces"

from abc import ABC, abstractmethod

#Mantener métodos que no aplican a todas las subclases no es correcto, por ende se debe crear una clase para c/u
class Trabajador(ABC): 
    """def comer(self):
        pass"""
    
    @abstractmethod
    def trabajar(self):
        pass
    
    """def dormir(self):
        pass"""
        
class Comelon(ABC):
    @abstractmethod
    def comer(self):
        pass

class Dormilon(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
    
class Humano(Trabajador, Dormilon, Comelon):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano está trabajando")
    
    def dormir(self):
        print("El humano está durmiendo")
    
#No es necesario que un robot herede los métodos comer y dormir de trabajador, únicamente hace falta que herede de las otras clases
class Robot(Trabajador):
    """def comer(self):
        pass"""
    
    def trabajar(self):
        print("El robot está trabajando")
    
    """def dormir(self):
        pass"""
        
#DIP
#Dependency Inversion Principle
#Principio de inversión de dependencias
#Las clases de alto nivel dependen de "interfaces maás complejas" y las de bajo nivel de "tareas específicas"
"""class Diccionario:
    def verificar_Palabra(self, palabra):
        pass"""
    
#CorrectorOrtografico depende de una clase superior, depende de Diccionario, si Diccionario cambia CorrectorOrtografico también
#CorrectorOrtografico es más importante, pero malamente depende de Diccionario
"""class CorrectorOrtografico:
    def __init__(self):
        self.diccionario = Diccionario()
        
    def corregir_Texto(self, texto):
        pass"""
    
class VerificadorOrtografico(ABC):
    @abstractMethod
    def verificar_Palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_Palabra(self, palabra):
        pass
    
class ServicioOnline(VerificadorOrtografico):
    def verificar_Palabra(self, palabra):
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_Texto(self, texto):
        pass