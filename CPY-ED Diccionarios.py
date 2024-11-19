#Diccionarios - Declaración
#Los diccionarios almacenan elementos de forma no ordenada, pueden ser homogéneos (tener solo un tipo de dato) o heterogéneos (más de un tipo de dato).
#Estos pueden contener almacenados otros diccionarios, listas, variables y valores de diferentes tipos
#Para declararlo se coloca el nombre del diccionario y su contenido se coloca dentro de las llaves {}, se crea una clave (puede ser string o entero) y el elemento (el dato almacenado) al que hace referencia
#Si nos encontramos en un mismo nivel la misma clave, la clave hará referencia al último valor que haga referencia
"""dictionary = {}
dictionaryHomo = {"Juan": 32,
                   "Gerardo": 21,
                   "Luis": 25
                   }
dictionaryHetero = {"name": "Brenda",
                    "last name": "Flores",
                    "age": 22
                    }
                    
dictionary_Tuple = dict({"Dato 1", "Dato 2"}: "Datos")
                    
#Útila para crear diccionarios vacíos                  
dictionary_Xtra = dict(nombre = "Franco", edad = 18)

print(f"Diccionario vacío: {dictionary}\n")
print(f"Diccionario de edades homogéneo: {dictionaryHomo}\n")
print(f"Diccionario de edades heterogéneo: {dictionaryHetero}\n")
print(f"Diccionario extra {dictionary_Xtra}")

dictionaryList = {"a": {"a": 1},
                  "b": [0, 1, 2]
                  }
print(f"Diccionario con lista: {dictionaryList}\n")"""

#Diccionarios - Acceso al diccionario
"""dictionary = {"numeros": [18, 19, 20],
              "grupo": {"a": 1, "b": 2}
              }
print(f"{dictionary['numeros'][0]} - {dictionary['grupo']['a']} = 17")"""

#Diccionarios - Método items()
#Devuelve todos los elementos del diccionario como una lista de tuplas
#Un item es el conjunto formado por la clave y su valor
"""dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Diccionario antes del método List(): {dictionary.items()}")
#Para poder trabajar de forma indepentiende con los elementos contenidos dentro del diccionario, es necesario convertirlos a una lista
listItems = list(dictionary.items())
print(f"Diccionario después del método List(): {listItems}")
for i in range(len(listItems)): print(f"Posición {i+1} de la lista: {listItems[i]}")"""

#Diccionarios - Método keys()
#Devuelve todas las claves del diccionario como una lista
"""dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Claves del diccionario antes del método List(): {dictionary.keys()}")
listKeys = list(dictionary.keys())
print(f"Claves después del método List(): {listKeys}")
for i in range(len(listKeys)): print(f"Posición {i+1} de la lista: {listKeys[i]}")"""

#Diccionarios - Método values()
#Devuelve todos los valores del diccionario como una lista
"""dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Valores del diccionario antes del método List(): {dictionary.values()}")
list_Values = list(dictionary.values())
print(f"Valores del diccionario después del método List(): {list_Values}")
for i in range(len(list_Values)): print(f"Posición {i+1} de la lista: {list_Values[i]}")"""

#Método clear
#.clear() elimina todos los elementos de una lista, diccionario o un conjunto
"""dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }

print(f"Diccionario antes del método .clear(): {dictionary}")
dictionary.clear()
print(f"Diccionario después del método .clear(): {dictionary}")"""

#Diccionarios - Modificar y agregar elementos
"""dictionary = {"a":1,
              "b":2,
              "c":3
              }
MODIFICAR
dictionary["a"] = -1

AGREGAR
dictionary["d"] = 4

print(dictionary)"""

#Diccionarios - Método copy()
#.copy() crea una copia de un objeto (listas, matrices, diccionarios)
"""dictionary = {"a":1,
              "b":2,
              "c":3
              }

dict_copy = dictionary.copy()
print(dict_copy)"""

#Diccionarios - Método fromkeys()
#.fromkeys() crea un diccionario y provee las claves que son la sequence y sus valores (por default None) que son value
"""sequence = ["uno", "dos", "tres"]
value = 5
dictionary = dict.fromkeys(sequence, value)
print(f"Primer diccionario (básico): {dictionary}")"""

"""dictionary = dict.fromkeys(["uno", "dos", "tres"], [1, 2, 3])
print(f"Segundo diccionario (listas): {dictionary}")"""

#En el caso de colocar un diccionario en sequence, solamente se tomarán las claves
"""dictionary = dict.fromkeys({"uno": 1, "dos": 2, "tres": 3}, 1)
print(f"Tercer diccionario (diccionario): {dictionary}")"""

#Si utilizamos una cadena como sequence, cada letra será una clave
"""dictionary = dict.fromkeys("holas", 2)
print(f"Cuarto diccionario (string): {dictionary}")"""

#Diccionarios - Método get()
#get() obtiene los valores asociados a las claves de un diccionario
#Dentro de get(key,value) se establece una clave y su valor. Se retornará value en caso de no existir dicha key
"""dictionary = {"a":1,
              "b":2,
              "c":3
              }
print(f'Retornando el valor de la key c: {dictionary.get("c", 4)}')"""

#Diccionarios - Método popitem()
#popitem() elimina el par clave-valor de un diccionario, retornando el par como una tupla, elimina el último par clave-valor por default
"""dictionary = {'a':1,
              'b':2,
              'c':3
              }
item = dictionary.popitem()
print(f'Clave-valor eliminado: {item}')"""

#Diccionarios - Método pop() aplicado a diccionarios
#pop(clave, valor) elimina el par clave-valor y retorna únicamente el valor
#Si únicamente colocamos la clave en el método pop(), en caso de no encontrarla, se retornará un error. El segundo argumento (valor) servirá como valor de retorno por default
"""dictionary = {'a': 1,
                'b': 2,
                'c': 3,
                'd': 4
                }
print(f"Eliminando el primer par clave-valor: {dictionary.pop('a')}")
print(f"Diccionario después del método pop(): {dictionary}")
print(f"Aplicación del método pop() en clave no existente: {dictionary.pop('z', 'No se ha encontrado dicha clave')}")
dictionary.pop('b')
print(f"Diccionario final: {dictionary}")"""

#Diccionarios - Método setdefault()
#.setdefault(key, value) crea un par clave-valor
#si la clave ya existe, retorna el valor correspondiente a dicha clave, sin modificar
#si agregamos una clave sin valor, crea el par y se asigna None como valor
#si agregamos una clave con valor, el método crea el par y nos retorna el valor
"""dictionary = {'a':1,
              'b':2,
              'c':3
              }
print(f"Setdefault() con clave existente: {dictionary.setdefault('a', 4)}")
print(f"Setdefault() con clave inexistente, pero sin valor: {dictionary.setdefault('d')}")
print(f"Setdefault() con clave inexistente y valor: {dictionary.setdefault('e', 5)}")
print(f"Diccionario: {dictionary}")"""

#Diccionarios - Método update()
#Actualiza o agrega elementos a un diccionario (al agregar elementos existentes, los sobrescribe) en base a otro diccionario
"""dictionary = {'a':1,
              'b':2,
              'c':3
              }
dictionary2 = {'d':5}
print(f"Diccionario original: {dictionary}")
dictionary.update({'d':4})
print(f"Diccionario después de .update(): {dictionary}")
dictionary.update(dictionary2)
print(f"Diccionario al sobrescribir con .update(): {dictionary}")"""

#Diccionario - Recorrer diccionarios
"""dictionary = {'a':1,
              'b':2,
              'c':3
              }
print("Recorriendo diccionario mediante Key")
for key in dictionary:
    print(f"Clave = {key} : Valor = {dictionary[key]}")
    
print("\nRecorriendo diccionario mediante Key y Value")
for key, value in dictionary.items():
    print(f"Clave = {key} : Valor = {value}")

print("\nRecorriendo diccionario mediante Value")
for value in dictionary.values():
    print(f"Valor = {value}")"""