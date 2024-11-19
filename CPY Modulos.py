#Importa todo el modulo
"""import modulo as m_Saludar
print(m_Saludar.Saludar("Franco"))"""

#Ver propiedades y elementos del namespace
"""print(dir(m_Saludar))"""

#Ver nombre del archivo "main"
"""print(m_Saludar.__name__)"""

#Importamos únicamente la función que necesitamos
"""from modulo import Saludar as saldr, despedirse as despds
print(saldr("Franco"))
print(despds("Denis"))"""

#Enrutamiento de módulos
#Módulo contenido en una carpeta "adelante"
"""from Mods.modulo_extra import buscar as b_Adelante
print(b_Adelante("Loera"))"""

#Módulo contenido en una carpeta "atras"
#1. Verificamos la ruta
"""import sys
print(sys.path)"""

#2. Agregamos el módulo a los módulos del sistema y lo importamos
"""sys.path.append("C:\\Users\\MrCloud\\OneDrive")
import modulo_detras as detras

print(detras.Detras("Alvarez"))"""

#Un paquete es un conjunto de módulos
#Para que Python sepa que una carpeta es un paquete, se necesita tener un archivo _init_.py
import paquete.mod1

print(paquete.mod1.saludo("Cloud"))