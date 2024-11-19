import pandas as pd

#Declaración de una serie pandas
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(notas)

#Declaración de una serie mediante rangos
serie = pd.Series(100, range(6))
print(serie)

#Colocamos los datos en una tupla
ventas_mensuales_tupla = (100000, 85000, 180000, 128000, 143000, 96000, 107000,
                          110000, 91000, 103000, 114000, 180000)

#Valores para las etiquetas del índice de la serie
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

ventas_mensuales_serie = pd.Series(ventas_mensuales_tupla)

#Le asignamos el conjunto de valores al índice de la serie.
ventas_mensuales_serie.index = meses

#Para obtener una serie de pandas que contenga los datos de la tupla
#la creamos de la siguiente forma
print(ventas_mensuales_serie)

#Llamada de datos mediante índice
print(f"Las ventas del mes de diciembre son: {ventas_mensuales_serie["Diciembre"]}")

#FILTRADO BOOLEANO
filtro1 = ventas_mensuales_serie >= 100000
filtro2 = ventas_mensuales_serie <= 150000

ventas_mensuales_filtradas = ventas_mensuales_serie[filtro1 & filtro2]
print(ventas_mensuales_filtradas)