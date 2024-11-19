import sys

"""def suma():
    while True:
        a = input("Introduzca el primer número: ")
        b = input("Introduzca el segundo número: ")
        try:
            resultado = int(a) + int(b)
        #Se puede tener más de una excepción
        except Exception as e:
            print(f"\nPor favor, introduzca un número \nERROR {type(e).__name__}\n")
        #El else se realiza en caso de no ejecutarse la excepción
        else:
            break
        finally:
            print("\nEsta sentencia se ejecuta siempre\n")
        
    return resultado
    
print(suma())"""

#Excepciones propias
"""class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"El error es: {err}")

#Manejando la excepción        
try:
    #raise sirve para lanzar expepciones
    raise MiExcepcion("Suceso de la excepción")
except:
    print("Lanzando except")
    
#Lanzando la excepción
raise MiExcepcion("Lanzamiento de la excepción")"""

#Filtrado de excepciones
lista_valores = ['x', 0, 4]

for valor in lista_valores:
    try:
        print(f"El valor en turno es {valor}")
        reciproco = 1 / int(valor)
        print(f"El recíproco es {reciproco}")
    except ValueError:
        print(f"El valor proporcionado ({valor}) no es compatible con la operación solicitada")
    except ZeroDivisionError:
        print("La división sobre cero no está permitida")
    except Exception:
        print(f"Ocurrió un problema {sys.exc_info()[0]}")
        Excepcion = sys.exc_info()
        for elemento in Excepcion:
            print(elemento)
    else:
        print("AHORA SI FUNCIONÓ BIEN")
    finally:
        print("**  Esta línea siempre se ejecutará  **\n")
        
valores = ["x", 0, 4]

for valor in valores:
    try:
        print(f"El valor actual es: {valor}")
        reciproco = 1 / int(valor)
        print(f"El reciproco es: {reciproco}")
    except ValueError:
        print(f"El valor proporcionado ({valor}) no es válido para la operación realizada")
    except ZeroDivisionError:
        print(f"No se puede dividir entre cero")
    except Exception:
        print(f"Ocurrió un problema {sys.exc_info()[0]}")
        Excepcion = sys.exc_info()
        for i in Excepcion:
            print(i)
    else:
        print("El funcionamiento fue correcto")
    finally:
        print("Esta línea se ejecuta siempre")