import os, sys

#getsizeof(x) devuelve la cantidad de bytes que el objeto X consume de memoria RAM
lista = [numero for numero in range(1, 1001)]
print(f"La lista actual tiene un consumo de: {sys.getsizeof(lista)} bytes")

tupla = tuple(lista)
print(f"La tupla actual tiene un consumo de: {sys.getsizeof(tupla)} bytes")

proporcion = (sys.getsizeof(tupla) * 100) / sys.getsizeof(lista)
print(f"La versión en tupla de los mismos datos tiene un consumo del {proporcion:.2f}% respecto a la versión en una lista")

#getcwd() retorna la ruta del directorio de trabajo actual
print(type(os.getcwd()), os.getcwd())

#chdir(X) cambia de directorio, donde X es la ruta de destino

#listdir() obtiene una lista que contiene el contenido del directorio
"""print(os.listdir())"""

try:
    #mkdir(X) crea un directorio con nombre X en el directorio de trabajo actual
    os.mkdir("DirectorioTest")
    with open("ArchivoTest.txt", "w") as archivo:
        pass
    
except:
    #rmdir(X) elimina un directorio con nombre X en el directorio de trabajo actual
    os.rmdir("DirectorioTest")
    os.remove("ArchivoTest.txt")

#walk() recorre todos los caminos de directorios posibles a partir de nuestro directorio de trabajo actual. Retorna una tupla que almacena una lista con las Rutas (a partir del directorio de trabajo actual), los nombres de Directorios y los nombres de Archivos 
for raiz, dirs, archivos in os.walk(".", topdown=False):
    for nombre in archivos:
        print(os.path.join(raiz, nombre))
    for nombre in dirs:
        print(os.path.join(raiz, nombre))

#path.exists(X) valida que exista un elemento con nombre X en el directorio de trabajo actual. Retorna un valor booleano
print(os.path.exists("GUI's"))

#rename(X, Y) cambia el nombre del elemento X al nombre Y
try:
    os.mkdir("DirectorioCambiante")
except:
    pass

try:
    os.rename("DirectorioCambiante", "DirectorioCambiado")
except:
    os.rmdir("DirectorioCambiado")
    os.rename("DirectorioCambiante", "DirectorioCambiado")

try:
    os.mkdir("DirectorioHijo")
except:
    pass

print(f"Directorio actual (padre 1): {os.getcwd()}")
os.chdir("DirectorioHijo")
print(f"Directorio actual (hijo): {os.getcwd()}")
os.chdir("..")
print(f"Directorio actual (padre 2): {os.getcwd()}")