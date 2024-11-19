#Manejo de CSV
# - Lectura
import csv

datos = dict()

auto1 = "BMW", 2005
auto2 = "Toyota", 2015

datos[10] = auto1
datos[20] = auto2

#Abrir un archivo en modo de escritura
archivo = open("autos.csv", "w", encoding="latin1", newline="")

#Establecer una salida de escritura
grabador = csv.writer(archivo)

#Asignar encabezado
grabador.writerow(("Clave", "Marca", "Año"))

#Iterar sobre los elementos de los datos a grabar
for clave, elementos in datos.items():
    grabador.writerow((clave, elementos[0], elementos[1]))
    
#Grabar todos los datos
grabador.writerows([(clave, elementos[0], elementos[1]) for clave, elementos in datos.items()])

archivo.close()

#Manejador de contexto With
with open("autos.csv", "w", encoding = "latin1", newline="") as archivo:
    grabador = csv.writer(archivo)
    
    grabador.writerow(("Clave", "Marca", "Año"))
    
    grabador.writerows([(clave, elementos[0], elementos[1]) for clave, elementos in datos.items()])
    
# - Lectura
datos_lectura = dict()

with open("autos.csv", "r", encoding = "latin1", newline = "") as archivo:
    lector = csv.reader(archivo)
    
    #El método next() devuelve el siguiente elemento de un iterador
    next(lector)
    
    """for clave, marca, año in lector:
        datos_lectura[int(clave)] = (marca, int(año))"""
        
    datos_a_leer = {int(clave): (marca, int(año)) for clave, marca, año in lector}