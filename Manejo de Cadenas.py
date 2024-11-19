import math

#Al agregar texto a una variable, su ID cambia
texto = "Hola"
print(id(texto))
texto += " Pipol"
print(id(texto))

var = math.pi

#f-strings
#Mostar valor de variable (se agrega textualmente 'var = ')
print(f"Contenido de {var}\n")
print(f"Contenido de {var = }\n")

#Alineación de contenido
print("=" * 20)
print(f"{'20 Caracteres':^20}")
print("=" * 20, end="\n\n")

#Alineación de contenido con relleno
print("-" * 20)
print(f"{'20 Caracteres':-^20}")
print("-" * 20)

#Tipos de datos en f-strings (d, n, e, f, %)
#Tipo d (entero decimal). Permite establecer espacios a su izquierda, no acepta flotantes
numero = 1000000
print(f"{numero:d}")
print(f"{numero:10d}")

#Tipo n (número). Permite establecer espacios a su izquierda Y maneja valores flotantes, permitiendo como máximo 6 caracteres enteros antes de utilizar notación exponencial
numero = 1000.1
print(f"{numero:n}")

numero = 10000000.1
print(f"{numero:10n}")

#Tipo e (notación exponencial).
numero = 1000000000.123123123
print(f"{numero:e}")

#Tipo f (flotante). Muestra el valor con punto decimal. Por defecto la precisión es 9
numero = 12345678.12345678
print(f"{numero:f}")
print(f"{numero:.3f}")
print(f"{numero:,.3f}")

#Tipo % (porcentaje). Multiplica por 100 el valor, lo muestra con el formato tipo f y agrega '%'
numero = 12345678.12345678
print(f"{4:%}")
print(f"{numero:.2%}")

cadena = 'Buenas noches gente'
print(cadena[::-1])
print(cadena[::5])