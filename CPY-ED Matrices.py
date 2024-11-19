#Matrices - Bidimensionales, organizadas por filas y columnas
"""matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
print(f"Primera fila de la matriz: {matrix[0]} \nSegunda fila de la matriz: {matrix[1]}\nTercera fila de la matriz: {matrix[2]}")
print(f"Primera columna de la matriz: {matrix[0][0]} {matrix[1][0]} {matrix[2][0]}")"""

#Matrices - Ciclo For
"""for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()"""

#Matrices - Suma de matrices
"""matrixA = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrixB = [[9,8,7],
           [6,5,4],
           [3,2,1]]
matrixC = []
row = 0

for row in range(len(matrixA)):
    newRow = []
    for column in range(len(matrixA[row])):
        newRow.append(matrixA[row][column] + matrixB[row][column])
    matrixC.append(newRow)
    
for row in range(len(matrixA)):
    if row != 1:
        print(f"{matrixA[row]}   {matrixB[row]}   {matrixC[row]}")
    else:
        print(f"{matrixA[row]} + {matrixB[row]} = {matrixC[row]}")"""

matrixList = []

cuantMatrix = int(input("¿Cuántas matrices desea?: "))

if (cuantMatrix < 2):
    print("La cantidad mínima de matrices debe ser superior a 1")
else:
    rows = int(input("¿Cuántas filas contendrán las matrices?: "))
    columns = int(input("¿Cuántas columnas contendrán las matrices?: "))
    
    #Se crea un ciclo for para la creación de cada matriz
    for matrix in range(cuantMatrix):
        
        tempMatrix = []
        
        #Se crea un ciclo for para la creación de cada fila
        for row in range(rows):
            
            rowTemp = []
            
            #Se crea un ciclo for para la creación de cada columna
            for column in range(columns):
                
                #Se guarda el valor de la columna dentro de nuestra fila
                rowTemp.append(int(input(f"Introduzca el valor a guardar en la Matriz {matrix + 1} Fila {row} Columna {column}: ")))
            
            #Se guardan los valores de la fila dentro de nuestra matriz
            tempMatrix.append(rowTemp)
            
        #Se guardan los valores de la matriz dentro de nuestra lista de matrices matriz
        matrixList.append(tempMatrix)      
    
    resultMatrix = []

    #Se crea un ciclo for para recorrer cada fila
    for row in range(rows):
            
        resultRow = []
        
        #Se crea un ciclo for para recorrer cada columna
        for column in range(columns):
            
            resultado = 0
            
            #Se crea un ciclo for para cambiar de matriz, en la siguiente iteración nos encontraremos en la segunda matriz, pero aún estaremos en la fila 0 y la columna 0
            for matrixPos in range(cuantMatrix):
                
                #El resultado es igual a la [matriz(a)][fila(x)][columna(y)] + la [matriz(b)][fila(x)][columna(y)]		la posición de la matriz es diferente, pero la posición de entre filas y columnas no
                resultado += matrixList[matrixPos][row][column]
            
            #El resultado se almacena dentro de la fila
            resultRow.append(resultado)
             
        #Los resultados (contenidos en la fila) se almacenan dentro de la matriz
        resultMatrix.append(resultRow)

    #La matriz que contiene los resultados se agrega a la lista de matrices
    matrixList.append(resultMatrix)
        
    for row in range(rows):
        for matrixPos in range(len(matrixList)):
            if (row != 1):
                #Si la fila actual no es la fila 1 (la primera fila es la fila 0), se colocan espacios al final de la impresión de cada fila de las matrices
                print(f"{matrixList[matrixPos][row]}", end="   ")
            else:
                if ((matrixPos) < (len(matrixList) - 2)):
                    #Si la fila actual es la fila 1 y se encuentra 2 matrices antes del resultado, se agrega el símbolo de suma al final de la impresión de la fila	| 3 |   | 2 | + | 1 |   | 0 |
                    print(f"{matrixList[matrixPos][row]}", end=" + ")
                elif ((matrixPos) < (len(matrixList) - 1)):
                    #Si la fila actual es la fila 1 y se encuentra 1 matriz antes del resultado, se agrega el símbolo de igual al final de la impresión de la fila 	| 3 |   | 2 |   | 1 | = | 0 |
                    print(f"{matrixList[matrixPos][row]}", end=" = ")
                else:
                    #Si la fila actual es la fila 1 y se encuentra 3 o más matrices antes del resultado, solamente se imprimen espacios vacíos 						| 3 |   | 2 |   | 1 |   | 0 |
                    print(f"{matrixList[matrixPos][row]}", end="   ")
        print()