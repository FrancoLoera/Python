import numpy as np

lista_bidimensional = [[0, 1], [0, 2], [0, 3], [0, 4]]
arreglo_bidimensional = np.array([[0, 1], [0, 2], [0, 3], [0, 4]])
arreglo = np.array([['ola', 'cómo', 'tamos'], ['gente', 'bonita', 'xd']])
print(arreglo)

print(f"Arreglo: {lista_bidimensional}\n")
print(f"Arreglo Numpy:\n{arreglo_bidimensional}")

#Acceso a elementos
#arreglo[fila][columna] o arreglo[fila, columna] es igual
print(f"Elemento de fila 3, columna 2: {arreglo_bidimensional[2, 1]}")

#Acceder al valor de columna de múltiples filas
print(f"Elementos de columna 2: {arreglo_bidimensional[:, 1]}")

#Creación de un elemento con valores cero
arreglo_cero = np.zeros(shape=(2, 4), dtype = int)
print(arreglo_cero)
print(f"Tamaño del arreglo: {arreglo_cero.shape}")

#Creación de un arreglo unidimensional con 10 valores aleatorios
arreglo_aleatorio = np.random.randint(1,11, size=10)
print(arreglo_aleatorio)

#Creación de una matriz bidimensional con 2 filas y 4 valores aleatorios
matriz_aleatoria = np.random.randint(1,11, size=(2,4))
print(matriz_aleatoria)

#Creación de un arreglo unidimensional que contenga una secuencia de valores
dos_en_dos = np.arange(10,25,2)
print(dos_en_dos)
print(f"\nLas dimensiones de la estructura resultante son: {dos_en_dos.shape}")

lista_uni = [i for i in range(2, 12, 2)]
arreglo_uni = np.arange(2, 12, 2)

#Los arreglos de numpy permiten operaciones matriciales, mientras que las listas únicamente duplican el contenido
print(lista_uni * 2)
print(arreglo_uni * 2)

#Filtrado booleano
arreglo_filtro = np.arange(1, 10)
filtro = arreglo_filtro < 5

#El resultado generado será un arreglo unidimensional
resultado = arreglo_filtro[filtro]
print(type(resultado))