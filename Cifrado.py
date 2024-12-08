import sys

print("=" * 50)
print(f"{' CIFRADO EXPRESS. ':=^50}")
print("=" * 50, end = "\n\n")


while True:
    #Sección ejecutable 1.
    try:
        print(f"{'MENÚ PRINCIPAL':-^50}")
        print("1- Menú de Usuarios.")
        print("2- Menú de Etiquetas.")
        print("3- Menú de Cifrado.")
        print("4- Menú de Descifrado.")
        print("5- Salir.")
        print("¿Qué es lo que deseas realizar? ")
    
    #Sección de manejo de excepciones 1.
    except Exception:
        excepcion = sys.exc_info()
        print(f"Se ha presentado un error de tipo: {excepcion[0]}. Mensaje del error: {excepcion[1]}")