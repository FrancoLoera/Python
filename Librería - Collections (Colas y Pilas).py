import collections

#COLAS
#deque es un tipo de objeto que se puede utilizar para el manejo de colas. Su manejo es similar al de una lista
cola = collections.deque(i for i in range(5))

#Agregar elementos
cola.append(5)

i = 1
while cola:
    print(f"{i}. Eliminando elemento {cola.popleft()} de la cola")
    i += 1

print()
#PILAS
pila = collections.deque(i for i in range(5))

#Agregar elementos
pila.append(5)

i = 1
while pila:
    print(f"{i}. Eliminando elemento {pila.pop()} de la pila")
    i += 1