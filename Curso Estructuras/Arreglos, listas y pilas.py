#Los arreglos mantienen la misma sintaxis y métodos que las listas, la única diferencia es que los métodos mantienen un único tipo de dato, mientras que las listas pueden contener múltiples tipos de datos e incluso otras estructuras de datos.
#Las pilas/stacks funcionan mediante FiLo (First in, Last out), por lo que para implementar su uso únicamente necesitamos utilizar el método pop para eliminar el elemento más reciente, y el método append para agregar un nuevo elemento en la parte "superior" de nuestra pila.
#Listas
"""
#Listas homogeneas (mismo tipo de dato)
listaHomogenea = ["Denis", "Franco", "Loera Alvarez"]
#Listas heterogeneas (distinto tipo de dato)
listaHeterogenea = ["Cadena", 2, 3.14, True]

#Recorrido de lista mediante rangos (x:y). x es el índice inicial, y el índice final
print(f"Primeros dos elementos de la Lista Homogenea: {listaHomogenea[:2]}")

#Indicar valores negativos en los rangos indica que el rango se tomará en cuenta desde los valores finales
print(f"Ultimos dos elementos de la Lista Homogenea: {listaHomogenea[-2:]}")

#un rango sin valores implica mostrar todos los valores de la lista (los muestra con el formato de lista, no con el formato de elemento)
print(f"Lista Homogenea completa: {listaHomogenea[:]}")

letras = ["a","b","c","d","e"]
letras[0:3] = "x", "y"
print(letras)"""

#Listas - Método append()
#lista.append(nuevoElemento) Agrega un nuevo elemento al final de nuestra lista
"""lista = ["a","b","c","d"]
lista.append("e")
print(lista)"""

#Listas - Método insert()
#lista.insert(x, y) Agrega un nuevo elemento a nuestra lista en la posición que indiquemos. x indica la posición, y el elemento.
#Si hay un elemento en la posición indicada, lo recorre a la siguiente posición. En el caso de que el índice indicado supere al rango, se colocará en el último índice.
"""lista = ["b","c","d","e"]
lista.insert(0,"a")
lista.insert(10,"x")
print(lista)"""

#Listas - Método pop()
#lista.pop() elimina el elemento específicado según su posición en nuestra lista, puede ser especificado o no, elimina el último elemento por default. También retorna el valor. Retorna IndexError si la lista está vacía o si el valor está fuera de rango
#Retorna el elemento eliminado.
"""lista = ["a","b","Borrar 1","c","d", "Borrar 2"]
print(f"Lista original: {lista}\nElemento que se eliminará por default: {lista.pop()}")

#Eliminar antepenúltimo elemento
print(f"Lista original: {lista}\nElemento que se eliminará: {lista.pop(-3)}")"""

#Listas - Método remove()
#lista.remove() elimina el primer elemento encontrado según el contenido especificado.
#Lanza una excepción en caso de no encontrar el contenido
"""lista = ["a","b","Borrar","c","d","Borrar"]
lista.remove("Borrar")
print(lista)"""

#Listas - Método del
#del lista[inicio:fin] elimina toda una lista o uno o varios elementos simultanáneamente, según el rango de posiciones indicadas (x-y). Elimina de izquierda a derecha.
"""lista = [1,2,3,4,5,6,7]
print(f"Lista antes del método del: {lista}")
del lista[1:-1]
print(f"Lista después del método del: {lista}")"""

#Listas - Método reverse()
#lista.reverse() invierte el contenido de una lista
"""lista = ["u","o","i","e","a"]
lista.reverse()
print(f"Lista al reves: {lista}")"""

#Listas - Método sort(x, y)
#y es nuestra key (método en base al cual ordenaremos), z es nuestro orden (por default es ascendente).
#Únicamente puede ordenar listas homogéneas (solamente cadenas o solamente numeros)
"""lista = ["a","ba","ced","deca","edeca"]
lista.sort(reverse = True)
print(f"Lista en orden descendente: {lista}")
lista.sort()
print(f"Lista en orden ascendente: {lista}")
lista.sort(key = len, reverse = True)
print(f"Lista con todos los parámetros: {lista}")"""

#Listas - Método index()
#Recuerda que .find() es para valores específicos, no para listas
#.index(x, y, z) x es el valor a buscar, y el rango inicial, z el rango final
#.index() devuelve un valor entero que representa la posición de la primera coincidencia. Lanza una excepción en caso de no encontrar coincidencias.
"""lista = ["encuentra","este","elemento"]
print(lista.index("elemento", 0, 3))"""

#Listas - Método extend()
#lista.extend() concatena listas o extiende el contenido de las mismas, no se pueden pasar elementos individuales.
"""invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
invitados.extend(amigos)
print(invitados)

numeros = [10,20]
numeros.extend(range(30,110,10))
print(numeros)
numeros.extend([110, 120, 130])
print(numeros)"""

#Listas - Método sum()
#sum() suma el contenido de todos los elementos de una lista
"""numeros = [1,2,3,True]
print(sum(numeros,10))"""

#Listas - Método list()
#list() convierte cada caracter de un string en un elemento de una lista
"""palabra = "Hola"
lista = list(palabra)
print(lista)"""

#Listas - Listas anidadas
"""listaA = [1,2,3,4,5,[6,7,8,[9,10,11]]]
print(listaA[5][3][2])"""

#Listas - Método clear()
#clear() elimina todo el contenido de la lista, mas no elimina a la lista
"""lista = ["Hola", "Soy", "Franco"]
print(lista)
lista.clear()
print(lista)"""

#Listas - Método copy()
#copy() retorna una copia de nuestra lista equivalente a [:]
lista = ["Buenas", "Tardes"]
lista2 = lista.copy()
print(lista2)

#Listas - Método count()
#count(x) retorna el número de veces que x aparece en la lista. Los rangos únicamente funcionan con cadenas.
lista = ["Buenas", "Tardes", "Buenas", "Gente"]
cadena = "Holala"

print(cadena.count("a", 0, 3))
print(lista.count("Buenas"))