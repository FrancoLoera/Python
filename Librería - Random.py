import random
#random.randrange permite retornar un valor entero desde y hasta cierto rango (no incluye el límite) y con ciertos saltos
#random.randrange(X) retorna un valor entero de 0 a X-1
print(f"Randrage con un único parámetro (0 a 10): {random.randrange(11)}")

#random.randrange(X, Y) retorna un valor entero de X a Y-1
print(f"Randrage con dos parámetros (10 a 20): {random.randrange(10, 21)}")

#random.randrange(X, Y, Z) retorna un valor entero de X a Y-1 con Z como valor de los saltos (salto de 2 a 4 = 2)
print(f"Randrage con tres parámetros (20 a 30, saltando 2): {random.randrange(20, 31, 2)}")

#random.randint(X, Y) retorna un valor desde X y Y (incluyendo Y)
print(f"Randint de 0 a 10: {random.randint(0, 10)}")

#random.random() retorna un valor flotante de 0.0 a 1.0 (excluye 1.0)
print(f"Valor random: {random.random()}")

#random.choice(X) retorna un elemento aleatorio contenido en alguna estructura X
lista = [10, 20, 30]
print(f"Elemento aleatorio de lista con .choice: {random.choice(lista)}")

#random.shuffle(X) altera el órden de alguna estructura X
print(f"Lista original: {lista}")
random.shuffle(lista)
print(f"Lista perturbada: {lista}")