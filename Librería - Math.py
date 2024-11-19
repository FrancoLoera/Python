import math

valorFlotante = float(input("Introduce un valor con fracción decimal: "))

#Redondear número a un entero menor 5.3 = 5 | -5.3 = -6
print(f"Redondear {valorFlotante} (floor): {math.floor(valorFlotante)}")

#Redondear número a un entero mayor 5.3 = 6 | -5.3 = -5
print(f"Redondear {valorFlotante} (ceil): {math.ceil(valorFlotante)}")

#Redondea en dirección al 0. Elimina decimales
print(f"La parte entera truncada de {valorFlotante} es {math.trunc(valorFlotante)}")

#Raíz cuadrada
print(f"Raíz cuadrada de 100: {math.sqrt(100)}")

#Valor absoluto
print(f"Valor absoluto de {valorFlotante}: {abs(valorFlotante)}")
valorFlotante = abs(valorFlotante)

#Factorial
print(f"El factorial de {math.trunc(valorFlotante)} es igual a {math.factorial(math.trunc(valorFlotante))}")

potencia = int(input("\nDame un valor entero:\n"))

#Potencia math.pow(valor, potencia)
print(f"El resultado de elevar {valorFlotante} a la {potencia} es igual a: {math.pow(valorFlotante,potencia)}")

#Valor de pi (15 dígitos)
print(f"El valor de Pi es {math.pi}")

#math.isclose(X, Y, Z) determina si X es cercano a Y con una tolerancia Z (la tolerancia es la diferencia máxima permitida entre X y Y). La tolerancia indica que la diferencia debe ser <= a Z
# Determinar si los números comparados son suficientemente cercanos
print(math.isclose(2.005, 2.125, abs_tol = 0.25))
print(math.isclose(2.547, 2.047, abs_tol = 0.5))
print(math.isclose(2.0214, 2.00214, abs_tol = 0.02))
print(math.isclose(3.532, 4.734, abs_tol = 1.201))