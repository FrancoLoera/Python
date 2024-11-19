import datetime
import time

#datetime.time(W, X, Y, Z) nos permite determinar un formato de hora W, con X minutos, Y segundos y Z microsegundos
#Los valores de los parámetros deben ser acordes a la lógica del tiempo (máximo de 23 hrs, 59 minutos, 59 segundos, 999 microsegundos). Valores 0 permitidos
fecha = datetime.date(2024, 12, 1)
hora = datetime.time(10, 20, 30, 99)

hora = hora.replace(hour = 2)
print(f"Tipo de dato: {type(hora)}")
print(f"La hora es: {hora}")
print(f"La hora de {hora} es {hora.hour}")
print(f"El minuto de {hora} es {hora.minute}")
print(f"El segundo de {hora} es {hora.second}")
print(f"El microsegundo de {hora} es {hora.microsecond}")

#datetime.[date][datetime].today() determina la fecha actual del sistema
fecha = datetime.date.today()
print(f"\nTipo de dato: {type(fecha)}")
print(f"El día de {fecha} es {fecha.day}")
print(f"El mes de {fecha} es {fecha.month}")
print(f"El año de {fecha} es {fecha.year}")

#Si se le proporciona una fecha imposible, o en un formato inválido se producirá un error
#datetime.datetime() permite determinar un formato con fecha y tiempo (año, mes, día, hora, minuto, segundo y microsegundo)
fecha_capturada = input("Dime una fecha (dd/mm/aaaa): ")

#datetime.strptime(X, Y) verifica que una cadena X se encuentre en un formato Y
#.date() se encarga de convertir el objeto actual a un objeto tipo datetime.date
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()

print(fecha_procesada.strftime('%d-%m-%Y'))
print(datetime.datetime.strftime(fecha_procesada, '%d-%m-%Y'))
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f"Nuestra fecha actual es: {fecha_procesada}")

#strftime(X) es un método para modificar el formato de tiempo de objetos datetime.date o datetime.datetime. Retorna una cadena
print(f"Fecha actual con formato mm/dd/yyyy: {fecha_procesada.strftime("%m/%d/%Y")}")

cant_dias = int(input(f"Dime la cantidad de días a adelantar respecto a {fecha_procesada}:\n"))
#datetime.timedelta() permite realizar operaciones (siguiendo la lógica de fechas: años bisiestos, cantidad de meses, días, horas, minutos, etc) con cantidades. El mayor 'valor' modificable son las semanas
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print(f"La nueva fecha es {nueva_fecha}")