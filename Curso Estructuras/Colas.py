from collections import deque
#Colas
#Creación de una cola
cola = deque(["Hola", "buenas", "gente"])
print(f"Cola inicial: {cola}")

#Agregar elementos a una cola
cola.append("bonita")
print(f"Cola Append: {cola}")

#Agregar elementos al inicio de una cola
cola.appendleft("XD")
print(f"Cola Appendleft: {cola}")

#Eliminar elementos
cola.popleft()
print(f"Cola Popleft: {cola}")

#Extender una lista desde la izquierda (considerar que los valores se toman de derecha a izquierda)
otra_cola = deque(["Valor 1", "Valor 2"])
cola.extendleft(otra_cola)
print(f"Cola Extendleft: {cola}")

#Rotar elementos
#Valores positivos equivalen a rotar a la derecha, osea d.appendleft(d.pop())
#Valores negativos equivalen a rotar a la izquierda, osea d.append(d.popleft())
cola.rotate(2)
print(f"Cola Rotate (derecho): {cola}")
cola.rotate(-2)
print(f"Cola Rotate (izquierdo): {cola}")

#Analizar tamaño máximo
cola_indefinida = deque(cola, 2)
cola_indefinida.append("XD")
print(f"Longitud máxima de cola definida: {len(cola_indefinida)}")
print(f"Contenido de cola indefinida: {cola_indefinida}")
print(f"Longitud máxima de cola indefinida: {len(cola_indefinida)}")
