#Listas
"""listaHomogenea = ["Denis", "Franco", "Loera Alvarez"]
listaHeterogenea = ["Cadena", 2, 3.14, True]

lista = []
print(f"Lista vacia: {lista}")
print(f"Primer Nombre: {listaHomogenea[0]}")
print(f"Segundo Nombre: {listaHomogenea[1]}")
print(f"Apellidos: {listaHomogenea[2]}")
print(f"La Lista Homogenea posee {len(listaHomogenea)} elementos")
print(f"Primeros dos elementos de la Lista Homogenea: {listaHomogenea[:2]}")
print(f"Ultimos dos elementos de la Lista Homogenea: {listaHomogenea[-2:]}")
print(f"Lista Homogenea completa: {listaHomogenea[:]}")

letras = ["a","b","c","d","e"]
letras[0:3] = "x", "y"
print(letras)"""

#Listas - Método append()
#lista.append(nuevoElemento) Agrega un nuevo elemento a nuestra lista
"""lista = ["a","b","c","d"]
lista.append("e")
print(lista)"""

#Listas - Método insert()
#lista.insert() Agrega un nuevo elemento a nuestra lista en la posición que indiquemos
#Si hay un elemento en la posición indicada, lo recorre a la siguiente posición
"""lista = ["b","c","d","e"]
lista.insert(0,"a")
lista.insert(2,"x")
print(lista)"""

#Listas - Método pop()
#lista.pop() elimina el elemento específicado según su posición en nuestra lista, puede ser especificado o no, elimina el último elemento por default
#Retorna el elemento eliminado
"""lista = ["a","b","Borrar 1","c","d", "Borrar 2"]
print(f"Lista original: {lista}\nElemento que se eliminará por default: {lista.pop()}")
print(f"Lista original: {lista}\nElemento que se eliminará: {lista.pop(-3)}")"""

#Listas - Método remove()
#lista.remove() elimina según el contenido especificado que se encuentre contenido en un elemento
#Lanza una excepción en caso de no encontrar el contenido
"""lista = ["a","b","Borrar","c","d","Borrar"]
lista.remove("Borrar")
print(lista)"""

#Listas - Método del
#del lista[inicio:fin] elimina toda una lista o uno o varios elementos simultanáneamente, según el rango de posiciones indicadas (x-y)
"""lista = [1,2,3,4,5,6,7]
print(f"Lista antes del método del: {lista}")
del lista[5:7]
print(f"Lista después del método del: {lista}")"""

#Listas - Método reverse()
#lista.reverse() invierte el contenido de una lista
"""lista = ["u","o","i","e","a"]
lista.reverse()
print(f"Lista al reves: {lista}")"""

#Listas - Método sort()
#lista.sort() ordena de forma ascendente o descendente (mayor a menor) los elementos de una lista, por default lo hace de forma ascendente
#Únicamente puede ordenar listas homogéneas (solamente cadenas o solamente numeros)
"""lista = ["a","b","c","d","e"]
lista.sort(reverse = True)
print(f"Lista en orden descendente: {lista}")
lista.sort()
print(f"Lista en orden ascendente: {lista}")"""

#Listas - Método index()
#lista.index() devuelve un valor entero que representa la posición de la primera coincidencia
"""lista = ["encuentra","este","elemento"]
print(lista.index("elemento", 0, 3))"""

#Listas - Método extend()
#lista.extend() concatena listas o extiende el contenido de las mismas, no se pueden pasar elementos individuales
"""invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]
invitados.extend(amigos)
print(invitados)

numeros = [10,20]
numeros.extend(range(30,100,10))
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