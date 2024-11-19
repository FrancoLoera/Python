#Prácticas
#Práctica 6. Curso Python (Eliminar una palabra)
#Desarrollar un programa que borre una palabra que forme parte de una cadena de caracteres

'''cadena = str(input("Introduzca su cadena: "))
eliminar = str(input("Introduzca la palabra a eliminar: "))

if (cadena.find(eliminar)):
    indice = cadena.find(eliminar)
    subcadena = cadena[0:indice] + cadena[indice + len(eliminar) + 1:]
    print(f"Cadena corregida: {subcadena}")
else:
    print("No se encontró la subcadena")'''
    
#Práctica 7. Curso Python (Invertir un String)
#Desarrollar un programa que invierta una cadena de caracteres, la cadena debe ser introducida por el usuario
'''cadena = str(input("Introduzca la cadena: "))
inversa = ""
for char in cadena:
    inversa = char + inversa
print(inversa)'''

#Práctica 8. Curso Python (Tabla de multiplicar, ciclo For)
#Desarrollar un programa que muestre en pantalla la tabla de multiplicar de un número introducido por el usuario (multiplicar de 0 a 10)
'''tabla = int(input("Introduzca el número a multiplicar: "))
print(f"TABLA DEL {tabla}")
for i in range(0,11,1):
    print(f"{tabla} X {i} = {tabla * i}")'''

#Práctica 9. Curso Python (String sin vocales)
#Desarrollar un programa que solicite una frase y un caracter específico, el programa debe imprimir la frase ingresada, sin vocales, y debe considerar el imprimir hasta antes de el caracter especificado (si el caracter es l, en el caso de "hola", se imprimiría únicamente la h)
'''frase = str(input("Introduzca la frase: "))
caracter = str(input("Introduzca el caracter: "))
for letra in frase:
    if (letra == caracter):
        break
    elif (letra.upper() == "A"):
        continue
    elif (letra.upper() == "E"):
        continue
    elif (letra.upper() == "I"):
        continue
    elif (letra.upper() == "O"):
        continue
    elif (letra.upper() == "U"):
        continue
    else:
        print(letra,end="")'''
        
#Preguntar correo al usuario e imprimirlo con el dominio modificado a ceu.es
'''correo = str(input("Introduzca su correo: "))
pos = correo.find("@")
inicio = correo[:pos+1]
print(f"Correo modificado: {inicio + 'ceu.es'}")'''

#Preguntar al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre en pantalla c/u.
#Adaptarlo a meses y dias con un único caracter
'''fecha = str(input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: "))
dia = fecha[:fecha.find("/")]
mesanio = fecha[fecha.find("/") + 1:]
mes = mesanio[:mesanio.find("/")]
anio = mesanio[mesanio.find("/") + 1:]
print(f"Dia: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")'''

#Preguntar: Nombre del producto, precio y número de unidades, mostar en pantalla el <producto>: <unidades> (con 5 dígitos) X <precio>$ (con 6 dígitos enteros y 2 decimales) = <total>$ (con 8 dígitos enteros y 2 decimales)
"""producto = str(input("Introduzca el nombre del producto: "))
precioU = float(input("Introduzca el precio por unidad: "))
cantidad = int(input("Introduzca la cantidad de unidades: "))
print(f"{producto}: {cantidad:5d} unidades X {precioU:9.2f}$ = {cantidad * precioU:11.2f}$")"""

#Almacenar asignaturas de un curso en una lista y mostrarlas en pantalla
#Modificarlo para que muestre el mensaje "Yo estudio {materia}" con cada una de las materias guardadas
#Modificarlo para que pregunte el puntaje en cada una de las materias e imprima el puntaje junto al mensaje anterior
"""salida = 1
materias = []
calificaciones = []
while (salida != 0):
    insertar = str(input("Materia a agregar: "))
    materias.append(insertar)
    puntos = float(input("Calificación: "))
    calificaciones.append(puntos)
    salida = int(input("Desea agregar otra materia? (0 = No): "))
    print("")
    if (salida == 0):
        print(f"Materias almacenadas: {materias}")
        largo = len(materias)
        for i in range(0,largo,1):
            print(f"Yo estudio {materias[i]} y mi calificación es {calificaciones[i]:.0f}")"""

#Preguntar al usuario los números ganadores de la lotería y los muestre por pantalla ordenados de menor a mayor
"""boletos = []
for i in range(6):
    boletos.append(int(input("Introduzca el número del boleto ganador: ")))
boletos.sort()
print(f"Los números ganadores son: {boletos}")"""

#Almacenar en una lista los números del 1 al 10 y mostrarlos en orden inverso separados por comas.
"""lista = [1,2,3,4,5,6,7,8,9,10]
lista.reverse()
for i in range(10):
    if (i < 9):
        print(lista[i], end=", ")
    else:
        print(lista[i])"""

#Almacenar en una lista materias de un curso, preguntar al usuario su calificación de cada materia y ,en caso de aprobar, se eliminará la materia, en caso de reprobar, se almacenará y se mostrará con las otras materias reprobadas
"""materias = ["Matemáticas", "Español", "Inglés", "Historia"]
aprobadas = []
for materia in materias:
    calificacion = float(input(f"¿Cuál es tu calificación en {materia}?: "))
    if (calificacion > 69):
        aprobadas.append(materia)

for materia in aprobadas:
    materias.remove(materia)
print(f"Tienes que repetir: {materias}")"""

#Práctica 10. Curso Python (Manejo de listas)
#Solicitar la longitud de una lista que contendrá únicamente elementos de tipo entero. Según la longitud, solicitar cada uno de los elementos. Mostrar la lista completa y la suma de todos los elementos
"""lista = []
largo = int(input("¿Cuántos elementos contendrá la lista?: "))
for i in range (largo):
    lista.append(int(input(f"{i+1}. Introduzca el valor: ")))
print(f"Contenido de la lista: {lista}")
print(f"Total: {sum(lista)}")"""

#Práctica 11. Curso Python (Una lista en dos listas)
#Según la lista, preguntar al usuario qué elemento desea eliminar, sin importar que se repita el elemento o se encuentre en mayúscula o minúscula
"""lista = ["A","B","b","c","E","E","f"]
caracter = input(f"{lista}\n ¿Qué caracter desea eliminar?: ")
for i in lista:
    if (caracter.lower() in lista):
        lista.remove(caracter.lower())
    elif (caracter.upper() in lista):
        lista.remove(caracter.upper())
print(f"Lista: {lista}")"""

#Almacenar el abecedario en una lista y eliminar los elementos que ocupen posiciones que sean múltiplos de tres
"""abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(abecedario), 1, -1):
    if (i % 3 == 0):
        abecedario.pop(i-1)
print(abecedario)"""

#Pedir una palabra al usuario, si es un palíndromo, mostrarla en pantalla
"""palabra = input("Introduzca la palabra: ")
inversa = palabra
palabra = list(palabra)
inversa = list(inversa)
inversa.reverse()
if (palabra == inversa):
    print(f"{palabra} Es un palíndromo")
else:
    print("f{palabra} No es un palíndromo")"""

#Solicitar una palabra y mostrar el número de veces que contiene cada vocal
"""palabra = input("Introduzca la palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    veces = 0
    for letra in palabra:
        if (letra == vocal):
            veces += 1
    print(f"La vocal {vocal} aparece {veces} veces")"""

#Almacenar los vectores (1,2,3) y (-1,0,2) en dos tuplas y mostrar su producto escalar
"""pro = (1,2,3)
sdo = (-1,0,2)
rdo = 0
for i in range(len(pro)):
    rdo += pro[i] * sdo[i]
print(f"El producto escalar es: {rdo}")"""

#Dada la lista, eliminar el primer y último elemento, seguido de esto, mostraremos dos listas, la primera contendrá los elementos no eliminados y la segunda los elementos eliminados
"""lista = [1,2,3,4,5]
eliminados = []
print(f"Lista original: {lista}")
eliminados.append(lista.pop(0))
eliminados.append(lista.pop())
print(f"Lista actualizada: {lista}")
print(f"Lista de eliminados: {eliminados}")"""

#Práctica 13. Curso Python (Crear una matriz desde teclado)
#El usuario genera una matriz indicando la cantidad de filas y columnas, se le solicitarán los valores de cada elemento
"""matrix = []
filas = int(input("¿Cuántas filas contendrá la matriz?: "))
columnas = int(input("¿Cuántas columnas contendrá la matriz?: "))

for fila in range(filas):
    lista = []
    for elemento in range(columnas):
        lista.append(int(input(f"Introduzca el nuevo elemento de la Fila {fila}, Columna {elemento}: ")))
    matrix.append(lista)
    
for fila in matrix:
    print(fila, end=" ")
    print()"""

#Práctica 14. Curso Python (Suma de matrices desde teclado)
#El usuario introduce la cantidad de matrices, se debe validar que sean dos o más. El usuario también indica la cantidad de filas y columnas, y sus elementos (indicando la matriz, fila y columna actual). Finalmente mostrar las matrices a sumar y la matriz resultante
"""cantidadMatrix = int(input("¿Cuántas matrices desea sumar?: "))
    
if (cantidadMatrix < 2):
     print("La cantidad de matrices a sumar debe ser superior a uno")
else:
     rows = int(input("¿Cuántas filas contendrán las matrices?: "))
     columns = int(input("¿Cuántas columnas contendrán las matrices?: "))
     matrixList = []
     
     for number in range(cantidadMatrix):
         matrix = []
         for row in range(rows):
             newRow = []
             for column in range(columns):
                 newRow.append(int(input(f"Introduce el elemento para la Matriz {number + 1} Fila {row} Columna {column}: ")))
             matrix.append(newRow)
         matrixList.append(matrix)
     
     matrix = []
     for row in range(rows):
         newRow = []
         for column in range(columns):
             sumMatrix = 0
             for matrixPosition in range(len(matrixList)):
                 sumMatrix += matrixList[matrixPosition][row][column]
             newRow.append(sumMatrix)
         matrix.append(newRow)
     matrixList.append(matrix)
     
     for matrixRow in range(rows):
         for matrixListPosition in range(len(matrixList)):
             if matrixRow != 1:
                  print(f"{matrixList[matrixListPosition][matrixRow]}", end="   ")
             else:
                 if ((matrixListPosition) < (len(matrixList) - 2)):
                      print(f"{matrixList[matrixListPosition][matrixRow]}", end=" + ")
                 elif ((matrixListPosition) < (len(matrixList) - 1)):
                      print(f"{matrixList[matrixListPosition][matrixRow]}", end=" = ")
                 else:
                      print(f"{matrixList[matrixListPosition][matrixRow]}", end="   ")
         print()"""

#Escribir un programa que almacene en una lista los siguientes numeros: 50, 75, 46, 22, 80, 68, 8 y muestre en pantalla el menor y el mayor
"""nums = [50, 75, 46, 22, 80, 68, 8]
min = max = nums[0]
#Se asigna a min y max el valor de nums[0] (50) para evitar un error al comparar entero con función
for num in nums:
    if num < min:
        min = num
    elif num > max:
        max = num
print("El mínimo es: " + str(min))
print("El máximo es: " + str(max))"""

#Almacenar las matrices en una lista y mostrar en pantalla su producto
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
#En este ejemplo tenemos una multiplicación de matrices de (2x3)(3x2)
#Se procede a multiplicar la primera fila de A (1, 2, 3) por la primera columna de B (-1, 0, 1) y se suman los productos
#Luego multiplicamos la primera fila de A (1, 2, 3) por la segunda columna de B (0, 1, 1) y se suman los productos
#Seguimos por la segunda fila de A (4, 5, 6) multiplicada por la primera columna de B
#Y finalmente la segunda fila de A por la segunda columna de B
#Obtendremos 4 productos, los cuales se colocan en "una matriz de 2x2"
"""result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])"""

#Pedir al usuario un número entero positivo y mostarr en pantalla todos los números impares desde 1 hasta ese número, separados por comas
"""num = int(input("Introduzca un número entero positivo: "))
for i in range(1, num):
    if (i % 2 != 0):
        print(i, end=", ")
print(num)"""

#Pedir un número al usuario y crear un triángulo rectángulo que tendrá como altura el número introducido
"""alt = int(input("Introduzca un número entero para representar la altura del triángulo: "))
tgl = ""

for i in range(alt):
    tgl += "*"
    print(tgl)"""

#Pedir al usuario un número entero y mostrar un triángulo basado en la altura brindada por el usuario, se mostrarán números impares
"""n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")"""

#Crear un diccionario con diversas divisas y preguntar al usuario por una, mostrar su símbolo o un mensaje de aviso según sea el caso
"""dict_Divisas = {'Euro':'€',
                'Dolar':'$',
                'Yen':'¥'}
divisa = str(input("Introduzca su divisa: "))

if divisa.title() in dict_Divisas:
    print(f"El símbolo de su divisa es: {dict_Divisas[divisa.title()]}")
else:
    print("La divisa no se encuentra almacenada")"""

#Preguntar al usuario su nombre, edad, dirección y teléfono, y guardarlo en un diccionario. Despues mostrar <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>
"""nombre = input("¿Cuál es su nombre?: ")
edad = input("¿Cuál es su edad?: ")
direccion = input("¿Cuál es su dirección?: ")
telefono = input("¿Cuál es su telefono?: ")

datos = {"nombre":nombre,
         "edad":edad,
         "telefono":telefono,
         "direccion":direccion
         }
print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")"""

#Curso Python - 5 ejercicios Diccionarios
#Mediante el diccionario proporcionado deberemos:
# - Devolver el número de manzanas
"""fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(f"Diccionario: {fruits}")
num_Manzanas = fruits.get("manzanas")
print(f"Total de manzanas (mediante get): {num_Manzanas}")

for key in fruits.keys():
    if (key == "manzanas"):
        print(f"Total de manzanas (mediante ciclo): {fruits[key]}")"""
        
# - Agregar tres nuevos items
"""fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(f"Diccionario antes de la modificación: {fruits}")
fruits.update({"bananas": 5})
fruits["mangos"] = 6
fruits.setdefault("uvas", 3)
print(f"Diccionario después de la modificación: {fruits}")"""

# - Eliminar el par clave valor "peras"
"""fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(f"Diccionario antes de eliminar par (mediante pop): {fruits}")
fruits.pop("peras")
print(f"Diccionario después de eliminar par (mediante pop): {fruits}")

fruits["peras"] = 2

print(f"\nDiccionario antes de eliminar par (mediante del): {fruits}")
del fruits["peras"]
print(f"Diccionario después de eliminar par (mediante del): {fruits}")"""

# - Retornar una lista que contenga las claves y otra que contenga sus valores
"""fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
llaves, valores = [], []

llaves = list(fruits.keys())
valores = list(fruits.values())

for column in range(len(llaves)):
    valor = ": Valor = "
    print(f"Clave = {llaves[column]}".ljust(16), end=" : ")
    print(f"Valor = {valores[column]}")"""

# - Retornar True si la clave manzanas existe en el diccionario
"""fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(f"¿La clave manzanas está dentro de fruits? {'manzanas' in fruits}")

if "manzanas" in fruits:
    print(f"¿'manzanas' en fruits? {True}")

if not("manzana" in fruits):
    print(f"¿'manzana' en fruits? {False}")"""

#Práctica 15. Curso Python (Frecuencia de letras en texto)
#Recibir un string y almacenar en un diccionario la cantidad de veces que aparece cada uno de las letras y caracteres que componen al string
#Curso (crea un diccionario en base a la cadena, ya que cada carácter del string es una clave, y les da valor 0. El ciclo se encarga de aumentar su valor conforme a su aparición)
"""cadena = str(input("Ingrese su cadena: "))
caracteres = dict.fromkeys(cadena, 0)

for char in cadena:
    caracteres[char] += 1

print(f"Caracteres: {caracteres}")

#Mía
for char in cadena:
    if (char in caracteres):
        caracteres[char] += 1
    else:
        caracteres[char] = 1"""

#Práctica 16. Curso Python (Modificación de una tupla)
#Dada la tupla inicial: mostrar la tupla inicial, solicitar un número existente, reemplazar por 0 el número solicitado y mostrar la tupla


#CURSO (modifica la tupla a lista y al final la modifica a tupla)
"""nums_Tuple = (5, 8, 3, 3, 1, 6, 2)
print(f"Table original: {nums_Tuple}")

num = int(input("¿Cuál de estos números quieres modificar por 0?: "))
nums_Tuple = list(nums_Tuple)
len_Tuple = len(nums_Tuple)

for i in range(len_Tuple):
    if (nums_Tuple[i] == num):
        nums_tuple[i] = 0
        
nums_Tuple = tuple(nums_Tuple)

print(f"Tupla modificada: {nums_Tuple}")"""

#MÍA (no es modificación ya que cree una lista nueva)
"""tupla_Nums = (5, 8, 3, 3, 1, 6, 2)
lista = []

print(f"Tupla inicial: {tupla_Nums}")
clear = int(input("¿Número a eliminar?: "))

for num in tupla_Nums:
    if (num == clear):
        lista.append(0)
    else:
        lista.append(num)
        
print(f"Tupla final: {tuple(lista)}")"""

#Práctica 17. Curso Python (Seleccionador de nombres)
#Dada la tupla: mostrar la tupla, solicitar un número entre 0 y 4, validar el número y, en caso de que sea válido, mostrar el nombre correspondiente según el índice, caso contrario mostrar una alerta y volver a solicitar
"""error = 1
tupla = ("Ana", "Gerardo", "María", "Carlos", "Valentina")

while (error == 1):
    print(f"Tupla inicial: {tupla}")
    num = int(input("Introduzca un número entre 0 y 4: "))
    
    if (num < 0) or (num > 4):
        print("\n - Introduzca un número válido (0-4) - \n")
    else:
        error = 0
        
print(f"Nombre: {tupla[num]}")"""

#Práctica 17. Curso Python (Suma de tuplas)
#Dadas las tuplas, sumar los elementos conforme a sus índices, luego mostrar la operación
"""tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)
resultado = []

for x, y in zip(tupla1, tupla2):
    resultado.append(x + y)

print(f"Tupla 1:".ljust(13), tupla1)
print("".ljust(14) + "+")
print(f"Tupla 2:".ljust(13), tupla2)
print("".ljust(14) + "===============")
print(f"Suma:".ljust(13), tuple(resultado))"""

#Práctica 18. Curso Python (Ordenamiento de una tupla)
#Dada la tupla personas, mostrar la tupla original, mostrar la información de la persona de menor y mayor edad
"""personas = (("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22))
print(f"{personas}\n")
personas = list(personas)

for i in range(len(personas)):
    for j in range(i + 1, len(personas)):
        if (personas[i][1]) > (personas[j][1]):
            aux = personas[i]
            personas[i], personas[j] = personas[j], aux
print(f"Persona menor: {personas[0]}")
print(f"Persona mayor: {personas[3]}")"""

#Práctica Dalto I - Básicos
#a) Diferencia en porcentaje entre el curso actual y: El más rápido, lento y promedio
#b) Porcentaje de material inservible que se reduce en: El promedio de los cursos y el curso actual
#C) ¿Ver 10 hrs de este curso a cuantas de otros cursos equivale? y viceversa
"""
#A
otros_Cursos_Min =  2.5
otros_Cursos_Max = 7
otros_Cursos_Promedio = 4
dalto_Curso = 1.5

def diferencias(x, y):
    diferencia = 100 - (x / y * 100)
    return diferencia
print("DIFERENCIAS DEL CURSO DE DALTO")
print(f"- Con cursos más lentos: {diferencias(dalto_Curso, otros_Cursos_Min):.1f}")
print(f"- Con cursos más rápidos: {diferencias(dalto_Curso, otros_Cursos_Max):.1f}")
print(f"- Con cursos promedio: {diferencias(dalto_Curso, otros_Cursos_Promedio):.1f}")
print("----------------------------")

#B
crudo_Promedio = 5
crudo_Dalto = 3.5

def crudos(x, y):
    tiempo_Vacio = 100 - (x * ((1000 // y) / 10))
    return tiempo_Vacio

print("TIEMPOS VACÍOS ELIMINADOS: ")
print(f"- De un curso promedio: {crudos(otros_Cursos_Promedio, crudo_Promedio)}%")
print(f"- Del curso de Dalto: {crudos(dalto_Curso, crudo_Dalto)}%")
print("----------------------------")

#C
def equivalencias(x, y):
    equivale = x * ((100 // y) / 10)
    return equivale

print("VER 10 HORAS")
print(f"- Del curso de Dalto equivale a {equivalencias(otros_Cursos_Promedio, dalto_Curso)} de otros cursos")
print(f"- De otros cursos equivale a {equivalencias(dalto_Curso, otros_Cursos_Promedio)} del curso de Dalto")
print("----------------------------")"""

#Práctica Dalto II - Primer ejercicio
#A) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
#B) El mayor es el profesor y el menor es el asistente
"""def cantidad_Compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del compañero {i+1}: ")
        edad = int(input(f"Ingrese la edad del compañero {i+1}: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    #Sort recibe como argumentos la forma en la que deseamos ordenar nuestros elementos
    #En este caso los ordenamos conforme a la edad contenida en cada tupla (x[1])
    compañeros.sort(key = lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = cantidad_Compañeros(5)
print(f"El asistente es {asistente} y el profesor es {profesor}")"""

#Práctica Dalto II - Segundo ejercicio
#Función que nos devuelva los números primos previos a nuestro número indicado
"""def num_Prim(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

def primos_Hasta(num):
    primos = []
    for i in range(3, num + 1):
        resultado = num_Prim(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_Hasta(96)
print(resultado)"""

#Práctica Dalto II - Tercer ejercicio
#Serie Fibonacci de 0 al número dado
"""def fibonacci(num):
    a, b = 0, 1
    fibo_List = [0]
    for i in range(num):
        if (b) > (num): return fibo_List
        else:
            fibo_List.append(b)
            a, b = b, a+b

resultado = fibonacci(34)
print(resultado)"""

#Realizar una función que reciba una muestra de números en una lista y determine su media
def media(*numeros):
    resultado = sum(numeros) / len(numeros)
    return resultado
    
lista = []
error = 0
while(error == 0):
    lista.append(int(input("Introduzca un número: ")))
    retry = (input("\n¿Desea introducir otro dígito?: "))
    if(retry == 0):
        error = 1
print(f"Media: {media(lista)}")