import pandas as pd
import csv
df = pd.read_csv("otro_archivo.csv")
#CSV - Lectura
"""with open("otro_archivo.csv") as archivo:
    #Este es un objeto iterable, por ende, para mostrar su contenido es necesario utilizar un ciclo for
    reader = csv.reader(archivo)
    
    for row in reader:
        print(row)"""
        
#CSV - Lectura óptima
#pd es el uso universal de pandas
"""import pandas as pd
#Data frame
#Para cambiar el nombre de las columas, se utiliza el parámetro name y se asignan los valores de los nombres en una lista
df = pd.read_csv("otro_archivo.csv", names=["Name", "Lastname", "Age"])
print("\nNombres del Data frame:")
print(df["Name"])
print("\nData frame completo:")
print(df)"""

#CSV - Ordenar valores
"""print(df.sort_values("edad"))
#Imprime las edades de forma descendente (mayor a menor)
print("")
print(df.sort_values("edad", ascending=False))"""

#CSV - Concatenación
"""df2 = pd.read_csv("otro_archivo.csv")
df_concatenado = pd.concat([df, df2])
print(df_concatenado)"""

#CSV - Filas iniciales y finales
"""#La fila 0 hace referencia a la cabecera
print(df.head(0))
print(df.head(3))
#Últimas filas
#La última fila es un Df vacío
print(df.tail(0))
print(df.tail(3))"""

#CSV - Cantidad de filas y columnas
#.shape es un atributo que guarda la cantidad de filas y columnas en una tupla
"""filas_totales, columnas_totales = df.shape
print(f"Contamos con {filas_totales} filas y {columnas_totales} columnas")"""

#CSV - Estadísticas del Df
"""print(df.describe())"""

#CSV - Acceso a elementos especificos del Df
#Mediante loc indicamos el índice de la fila y el nombre de la columna para obtener el elemento contenido en estas
print(df.loc[1, "nombre"])

#Acceder a todos los elementos de una fila mediante slicing (loc)
print(df.loc[:, "nombre"])

#Mediante iloc accedemos únicamente mediante indices (de fila y columna)
print(df.iloc[1, 0])

#Acceder a todos los elementos de una fila mediante slicing (iloc)
print(df.iloc[:, 0])

#Mostrar todos los datos de una fila (loc e iloc)
print(df.loc[0,:])

#Accediendo a filas con condición
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)