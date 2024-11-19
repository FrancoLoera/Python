#Tuplas - Declaración
#Las tuplas son inmutables y deben poseer más de un elementos
"""tupla = ({"a": 1, "b": 2}, True, 1, 1.2, [1, 2, 3])
print(f"Tupla: {tupla}")
#Para declarar un único elemento en nuestra tupla podemos colocar una coma sin necesidad de brindarle un valor al elemento
tupla = 0, 
print(tupla)"""

#Tuplas - Acceso
#1. Acceso por índice
"""tupla = (True, 1, 1.2, [1, 2, 3], {"a": 1, "b": 2})
print(f"Acceso a la tupla (por índice): {tupla[4]['a']}")

#2. Operador de segmentación
#La segmentación es equivalente a utilizar range() en un ciclo for
print(f"Acceso a la tupla (por segmentación): {tupla[0:5:2]}")

#3. Desempaquetado de tuplas
#El desempaquetado se refiere a colocar los valores de una tupla dentro de variables mediante la segmentación
var1, var2 = tupla[:2]
print(f"Acceso a la tupla (por desempaquetado de tuplas): {var1}, {var2}")"""

#Tuplas - Inmutabilidad
#Las tuplas, una vez declaradas, no pueden agregar más elementos ni cambiar sus valores
#En el caso de que el elemento de una tupla sea una lista, un diccionario o un conjunto, el contenido de los mismos puede ser modificado
"""tupla = ([1,2,3], {"a": 1, "b": 2}, {4, 5, 6})

print(f"Lista de una tupla sin modificar: {tupla[0]}")
tupla[0][2] = 10
print(f"Lista de una tupla modificada: {tupla[0]}")

print(f"Diccionario de una tupla sin modificar: {tupla[1]}")
tupla[1]["b"] = 0
print(f"Diccionario de una tupla modificada: {tupla[1]}")

print(f"Conjunto de una tupla sin modificar: {tupla[2]}")
tupla[2].remove(6)
tupla[2].add(30)
print(f"Conjunto de una tupla modificada: {tupla[2]}")"""

#Tuplas - Recorrido mediante For
"""tupla = ([1,2,3], {"a": 1, "b": 2}, {4, 5, 6})

for tuple_Value in range(len(tupla)):
    
    if type(tupla[tuple_Value]) == set:  
        print(f"Valores del conjunto: {tupla[tuple_Value]}")
        
    elif type(tupla[tuple_Value]) == dict:
        dict_Keys = list(tupla[tuple_Value].keys())
        for key in dict_Keys:
            print(f"Valor de la clave '{key}': {tupla[tuple_Value][key]}")
            
    else:
        for list_Value in range(len(tupla[tuple_Value])):
            print(f"Valor número {list_Value} de la lista: {tupla[tuple_Value][list_Value]}")"""

#Tuplas - Desempaquetado de tuplas
"""tupla = ("001", "Primera", "Tupla"), ("002", "Segunda", "Tupla")

#Al utilizar 3 variables para iterar, Python interpreta estas 3 variables como variables en las que se desempaquetará los valores de las tuplas
for num, pos, word in tupla:
    print(f"La {pos} {word} tiene el código {num}")"""

#Tuplas - Función tuple()
#tuple() solamente maneja un argumento y objetos iterables
"""x, y = 10, 5
coordenada = tuple([x, y])
print(coordenada)

#Al almacenar strings, cada uno de los caracteres que la componen se convertirá en un elemento de la tupla
#Al almacenar diccionarios únicamente se guardarán las claves. Podemos almacenar los valores del diccionario mediante el método values(), y para guardar los pares clave-valor solamente hace falta que utilizemos el método items():
dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
dict_Tuple = tuple(dictionary.items())
print(dict_Tuple)"""

#Tuplas - Concatenación de tuplas
"""tupla1, tupla2 = (1, 2, 3), (4, 5, 6)
concatenada = tupla1 + tupla2
print(concatenada)

tupla1 += tupla2
print(tupla1)"""

#Tuplas - Método zip()
#zip() genera una tupla que contrendrá tuplas por cada par de elementos (los que toma por argumentos) según el índice, los argumentos pueden ser strings, listas, tuplas, etc.
#Los objetos colocados dentro de zip() deben ser iterables (variables) y deben ser 2 o más objetos
"""names = ("Denis", "Franco", "Emi", "Eme")
ages = [10, 20, 30, 40, 50]
#Esto crea una tupla con tuplas dentro
combination = tuple(zip(names, ages))

print(combination)

for i in range(len(combination)):
    print(f"Tupla {i+1}: {combination[i]}")
    
for name, age in zip(names, ages):
    print(name, age)"""