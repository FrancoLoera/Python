#Funciones mediante args
#Args permite manejar la cantidad de argumentos que deseemos
#Este argumento se debe colocar al final
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus números es = {numeros}"

print("\033[1;33m"+"Números: 100 + 50 + 25 + 10 + 5 + 2 \n" + "\033[0;0m"+f"{suma("Franco", 100, 50, 20, 10, 5, 2)}")

#Para aplicar args a una lista, es necesario pasar la lista como un argumento (no args) y retornarla como una lista a la que se le aplica args (*)
def suma2(numeros):
    return sum([*numeros])

print(f"100 + 50 = {sum([100, 50])}")

#Forzar argumentos
"""def saludo(nombre, apellido):
    return f"Hola {nombre} {apellido}, ¿cómo estás?"

print(saludo(apellido = "Loera", nombre = "Franco"))"""

#Argumentos por default
#Al definir los argumentos en la función, en caso de que no nos brinder ningún valor, la función trabajará con los valores que declaramos "por default"
"""def fecha(dia, mes, año = 2024):
    return f"Hoy es {dia} de {mes} del {año}"

print(fecha(20, "Enero", 2023))
print(fecha(10, "Febrero"))"""

#Recursividad
"""def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)        
print(factorial(5))

def suma_De_Naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_De_Naturales(n)
print(suma_De_Naturales(5))"""

#Funciones Lambda
#Las funciones Lambda crean funciones "anónimas" ya que no tienen un nombre el cual las identifique. Para almacenar su valor de retorno es necesario asignarlas a alguna variable
"""funcion = lambda x: f"El valor introducido es {x}"
print(funcion(20))"""

#Método filter para funciones
"""numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def pares(nums):
    if (nums % 2 == 0):
        return True

#Filter selecciona la función a ejecutar y va probándola con cada uno de los elementos contenidos en la lista
#Filter retorna un objeto de tipo Filter con aquellos valores que hayan devuelto True
numeros_Pares = filter(pares, numeros)

#Para imprimir los valores "True" es necesario transformar de Filter a Lista
print(list(numeros_Pares))"""

"""#Filter x Lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda num: num % 2 == 0, numeros)
print(list(pares))"""