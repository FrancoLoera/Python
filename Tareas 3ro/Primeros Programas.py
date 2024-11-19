#1- Calcular el área de un círculo a partir de la longitud de su radio expresado en centímetros.
"""import math

radio = float(input("Introduzca la longitud de su radio (en centimetros): "))
print(f"El área de su círculo con {radio}cm de radio, es: {math.pi * (pow(radio, 2)):,.2f}cm^2")"""

#2- "Cantar" las cartas de la lotería cuidando de no repetir cartas que ya hayan salido y que en cada ocasión se presenten en un orden diferente
"""import random

while True:
    try:
        cartas = ["El gallo", "El diablo", "La dama", "El catrín", "El paraguas", "La sirena", "La escalera", "La botella"]
        random.shuffle(cartas)
        
        print("1- Cantar las cartas")
        print("2- Salir")
        opc = int(input("Introduzca una opción: "))
        print("\n")
        
        if opc == 2:
            break
        elif opc != 1 and opc != 2:
            print("No es muy difícil introducir 1 o 2...\n")
            continue
        
        for carta in cartas:
            print(f"¡{carta}!")
        print("\n")
        
    except:
        print("\nNo es muy difícil introducir 1 o 2...\n")"""
        
#Determinar la edad, a la fecha actual (Determinada automáticamente), de una persona considerando su fecha de nacimiento
import datetime, time
from dateutil.relativedelta import relativedelta

fecha_Actual = datetime.date.today()

fecha_Nacimiento = input("Introduzca su fecha de nacimiento con formato 'dd/mm/yyy': ")
fecha_Nacimiento = datetime.datetime.strptime(fecha_Nacimiento, "%d/%m/%Y").date()

edad = relativedelta(fecha_Actual,fecha_Nacimiento)
print (f"Tienes {edad.years} años, {edad.months} meses y {edad.days} días de edad")