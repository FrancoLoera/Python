class Persona():
    def __init__(self, name, lastname):
        self.__nombre = name
        self.__apellido = lastname
        
    def get_Nombre(self):
        return self.__nombre
    
    def get_Apellido(self):
        return self.__apellido
    
    def set_Nombre(self, name):
        self.__nombre = name

    def set_Apellido(self, lastname):
        self.__apellido = lastname
               
franco = Persona("Franco", "Loera")
new_Name = input(f"Introduzca el nuevo nombre de {franco.get_Nombre()}: ")
franco.set_Nombre(new_Name)

new_Lastname = input(f"Introduzca el nuevo apellido de {franco.get_Apellido()}: ")
franco.set_Apellido(new_Lastname)
print(f"Nuevo nombre: {franco.get_Nombre()} {franco.get_Apellido()}")