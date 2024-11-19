#Conjuntos - Declaración
#Los conjuntos son semejantes a las tuplas, no podemos alterar los elementos del conjunto, pero sí al conjunto en su totalidad
#Los datos del conjunto no se pueden repetir
"""conjunto = {"Valor 1", 2, True}

#Set maneja únicamente 1 argumento
#Los conjuntos (mediante set) pueden contener listas, siempre y cuando estas no cuente con otras listas como elementos. Esto debido a su mutabilidad
conjunto2 = set(["Dato 1", ["Subdato 1"]]) Esto nos lanzaría una excepción"""

#Conjuntos - Concatenación
"""conjunto1 = frozenset(["C1. Dato 1", "C1. Dato 2"])
conjunto2 = {conjunto1, "C2. Dato 1", "C2. Dato 2"}
print(conjunto2)"""

#Conjuntos - Acceso
#No se puede mostrar el valor individual de los elementos, solamente los valores del conjunto
"""conjunto = {1, 2, 3}
print(conjunto)"""

#Conjuntos - Verificación de subconjuntos
"""conjunto1 = {5, 4, 3, 2, 1}
conjunto2 = {3, 2, 1}

print(f"¿C2 es subconjunto de C1?: {conjunto2.issubset(conjunto1)}")
print(f"¿C2 es subconjunto de C1?: {conjunto2 <= conjunto1}")
print(f"¿C2 es superconjunto de C1?: {conjunto2.issuperset(conjunto1)}")
print(f"¿C2 es superconjunto de C1?: {conjunto2 > conjunto1}")

#Verifica si son diferentes (únicamente hace falta que coincida un número para que sean iguales)
print(f"¿C1 difiere de C2?: {conjunto1.isdisjoint(conjunto2)}")
conjunto2 = {13, 12, 11}
print(f"¿C1 difiere de C2?: {conjunto1.isdisjoint(conjunto2)}")"""

#Conjuntos - Iteración
"""animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {52, 16, 14, 72}

for animal in enumerate(animales):
    print(f"Animal {animal[0]+1}: {animal[1].capitalize()}")"""

"""conjunto_uno = {"Denis", "Franco", "Loera", "hola"}
conjunto_dos = {"Amy", "Castro", "Perez", "hola"}

#Conjuntos - Unión
print(conjunto_uno | conjunto_dos)

#Conjuntos - Intersección
print(conjunto_uno & conjunto_dos)

#Conjuntos - Diferencia X - Y (elementos contenidos en conjunto_uno (X) que no existen en conjunto_dos (Y))
print(conjunto_uno - conjunto_dos)

#Conjunos - Diferencia simétrica (elementos contenidos en solamente un conjunto, no en ambos)
print(conjunto_uno ^ conjunto_dos)"""