#Strip
#.strip() elimina caracteres especificados al inicio y al final de una cadena
#.strip(), al no contener parámetros, elimina espacios
"""cadena = "\t-Hola Franco-"
print(cadena.strip("\t-H"))"""

#Rstrip
#.rstrip() elimina caracteres especificados al final (right) de una cadena
"""cadena = "Nueva Cadena-*"
print(cadena.rstrip("-*"))"""

#Lstrip
#.lstrip() elimina caracteres especificados al inicio (left) de una cadena
"""cadena = "-*Otra Más"
print(cadena.lstrip("-*"))"""

#IsTitle y Title
#.istitle() analiza la cadena, en caso de contener el formato mayúscula-minúsculas (Hola), retorna verdadero
"""nombres = "denis franco"
if (nombres.istitle()):
    print("La cadena tiene el formato correcto")
else:
    nombres = nombres.title()
    print(f"Cadena: {nombres}")"""
    
#IsLower y Lower
#.islower() analiza la cadena, en caso de contar únicamente con minúsculas, retorna true
"""minuscula = "Holas"
if (minuscula.islower()):
    print("La cadena contiene solamente minúsculas")
else:
    print("Cadena:",minuscula.lower())"""
    
#IsUpper y Upper
#.isupper() analiza la cadena, en caso de contar únicamente con mayúsculas, retorna true
"""mayuscula = "MENSAJE"
if (mayuscula.isupper()):
    print("La cadena contiene solamente mayusculas")
else:
    print("Cadena:",mayuscula.upper())"""
    
#Swapcase
#.swapcase() invierte las letras a mayúsculas/minúsculas, según corresponda
"""swap = "MAYUSCULA / minuscula"
print(swap.swapcase())"""

#Capitalize
#.capitalize() convierte el primer carácter de una cadena en mayúscula y el resto en minúsculas
#a comparación del método .title(), .capitalize() únicamente convierte en mayúscula el primer carácter
"""cadena = "frase pAra ConvErtiR"
print(cadena.capitalize())"""

#Center
#.center(x,"-") alinea nuestra cadena según la cantidad de espacios definidos en sus argumentos (x) y el resto de espacios pueden ser rellenados con carácteres (-)
#En caso de que los espacios restantes no sean equitativos, se mantendrán más espacios a la izquierda de la cadena
"""cadena = "otra"
print(cadena.center(10," "))"""

#Ljust
#.ljust(x,"-") alinea nuestra cadena a la izquierda, coloca espacios vacíos a la derecha según los espacios restantes (x-cadena)
"""print(cadena.ljust(10,"-"))"""

#Rjust
#rjust(x,"-") alinea nuestra cadena a la derecha, coloca espacios vacíos a la izquierda según los espacios restantes (x-cadena)
"""print(cadena.rjust(10,"-"))"""

#Count
#.count("texto a buscar",x,z) x representa la posición inicial y z la posición final
#En caso de contar los carácteres de una cadena completa, count cuenta 1 más
"""cadena = "cinco"
print(cadena.count(""))

cadena = "mi mamá me mima"
print(cadena.count("m",-4,15))"""

#Startswith
#.startswith("subcadena a buscar",x,z) x es la posición inicial y z la posición final
#.startswith() analiza nuestra cadena para identificar si posee la subcadena que estableceremos, las posiciones que avanzará será igual al largo de la subcadena
#Puede utilizar números negativos
"""cadena = "Hola Lola"
if (cadena.startswith("Hola")):
    print("Tiene un Hola")
else:
    print("No tiene un Hola")"""

#Endswith
#.endswith("texto a buscar",x,z) x es la posición inicial (más cercana al final de la cadena) y z la posición final (más cercana al inicio de la cadena)
"""if (cadena.endswith("Lola")):
    print("Tiene un Lola")
else:
    print("No tiene un Lola")"""
    
#Substrings
#variable[inicio:fin:saltos] el inicio y fin pueden estar vacíos (::saltos)
"""string = "0123456789"
print(string[0:10:2])"""

#Find
#.find("subcadena") retorna el valor de la posición en la que inicia la subcadena
"""palabra = "busqueda"
print(f"El número de la posición en la que se encuentra la letra 'a' es: {palabra.find('a') + 1}")"""
 
#Isalnum
#.isalnum() analiza una cadena y retorna true en caso de que todos los caracteres sean alfanuméricos
"""cadena = "Hola1"
if (cadena.isalnum()):
    print("\nToda la cadena contiene caracteres alfanuméricos")
else:
    print("\nLa cadena contiene caracteres especiales")"""

#Ciclo For
#La variable character únicamente podra ser utilizada dentro del ciclo for
"""string = "Hola"
for character in string:
    print(character, end="")"""

#Range
#range(stop)	range(start, stop)	range(start,stop,step)
#range parte desde 0. Stop (valor final, no lo genera), Start (valor inicial) y Step (saltos)

#Ciclo For y clase Range
"""print("\n")
for indice in range(1,10,2):
    print(indice)
    
lista1 = ["Valor 1", "Valor 2", "Valor 3"]
lista2 = ["Valor 5", "Valor 6", "Valor 7"]
lista3 = [5, 10, 15, 20, 25]

for v1, v2 in zip(lista1, lista2):
    print(f"Lista 1 {v1}")
    print(f"Lista 2 {v2}")
 
#Num se transforma en una tupla que contiene el índice y su valor   
for num in enumerate(lista3):
    print(f"Índice {num[0]}: {num[1]}")

#Al manejar else, este siempre se ejecutará al final de nuestras iteraciones    
for num in lista3:
    print(f"Valor de num: {num}")
else:
    print("Fin del bucle")
    
frutas = ["Mango", "Manzana", "Pera", "Platano", "Durazno", "Uvas"]"""
    
#Continue permite CONTINUAR con las siguientes condiciones, mientras que break rompe el ciclo for
"""for fruta in frutas:
    if fruta == "Pera":
        continue
    elif fruta == "Durazno":
        break
    else:
        print(f"Comeré {fruta.lower()}")

#For en una línea     
numeros = [2, 5, 8, 10]
numeros_Duplicados = list(x*2 for x in numeros)
print(numeros_Duplicados)"""
    
#Imprimir variables mediante %
#"s" es la instancia de la variable y la cantidad previa a "s" determina su alineación (espacio + tamaño de la cadena)
"""saludo = "Hola querido"
usr = "usuario"
print("%s \n%s \n%10s" % (saludo, usr, usr))"""

#Min y Max
#min y max retorna el item con el menor/mayor valor, en el caso de cadenas, analiza caracter por caracter para mostrar el menor/mayor valor
"""x = min("xa", "xb", "xc")
print(x)
x = max("xa", "xb", "xc")
print(x)"""

#Try y except
"""try:
    num = int(input("Ingresa un número: "))
    print(f"Tú número es: {num}")
    
except ValueError:
    print("Esto no es un número")"""
    
#Replace
#Reemplaza el contenido especificado en X por el contenido Y, a lo largo de toda la cadena
#cadena.replace(X, Y)
"""cadena = "holala"
cadena_Nueva = cadena.replace("la", "lu")
print(cadena_Nueva)"""

#Split
#Separa una cadena mediante el contenido especificado en sus argumentos y convierte la separación en una lista
"""cadena = "Buenas, Cómo, Estamos"
cadena_Separada = cadena.split(", ")
print(cadena_Separada)
cadena_Separada = cadena.split("as")
print(cadena_Separada)"""

#Slicing
"""cadena = "0123456789"
#Imprimer desde el índice 0 hasta el índice 5
print(cadena[:5])"""

#Salida de texto con formato. \033[cod_formato;cod_color_texto;cod_color_fondom
#\033 maneja negritas por default
print("\033[;33m"+"Texto normal 1")
print("\x1b[;33m"+"Texto normal 2")
print("\033[1;36m"+"Texto en negrita 1")
print("\x1b[1;36m"+"Texto en negrita 2")
#Estilo(0-7); Color de letra (30-37); Color de fondo(40-47)
print("\033[0;31;41m"+"Texto normal, subrayado y con fondo 1"+"\033[0;m")
print("\033[4;32;42m"+"Texto en negrita, subrayado y con fondo 1.5"+"\033[0;m")
print("\x1b[4;33;43m"+"Texto normal, subrayado y con fondo 2"+"\x1b[0;m")
print("\x1b[4;34;44m"+"Texto normal, subrayado y con fondo 2.5"+"\x1b[0;m")

#Round()
"""numero = round(12.5213, 2)
print(numero)"""

#Bool
#Retorna False en caso de pasar como argumento: 0, Null, False, None
#Retorna True en caso de brindarle como argumento: True, cadena, datos no vacíos
"""print(bool(1))
print(bool(0))"""

#All
#Retorna True si todos los argumentos son verdaderos (solamente acepta 1 argumento, pero podemos brindarle una lista)
"""print(all([1, True, "Hola"]))
print(all([0, True, "Hola"]))

val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 3, 4, 5, 6, 7]

lista_resultado = [1, 2, 3]
if (len(val1) == max(len(val1), len(val2))):
    lista_resultado.extend(val1[len(val2):])
else:
    lista_resultado.extend(val2[len(val1):])
    
print(str(lista_resultado))"""

#Método reversed(i)
#i es el iterable, este puede ser cadenas, tuplas, listas o rangos.
#reversed no invierte un objeto, crea uno nuevo.
lista = [1, 2, 3, 4]
inversa = list(reversed(lista))
print(lista)