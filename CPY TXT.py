#Esto únicamente abre el archivo y se asigna a una variable para consultar su información
"""apertura = open("texto.txt", encoding="UTF-8")"""

#Al leer, es necesario considerar que hace falta cerrar el archivo para cada "repetición de lectura"

#Leer hasta
"""char = apertura.readline(4)
print(char)"""

#Leer una sola línea
"""linea = apertura.readline()
print(linea)"""

#Leer todas las lineas
"""lineas = apertura.readlines()
print(lineas)"""

#Para poder consultar su contenido se utiliza el método .read()
#Esto lee el archivo completo, en caso de desear leer una sola línea, es necesario hacerlo antes de leerlo de esta forma ya que no lo leerá por temas de seguridad
"""lectura = apertura.read()"""

#Cerrar el archivo
"""apertura.close()"""


#Leer optimamente .txt


#Sin "as", nos encontraremos únicamente en el modo de lectura
"""with open("texto.txt", encoding="UTF-8") as archivo:
    print("Hola, este archivo ya se abrió")
    contenido = archivo.read()
    print(contenido)"""
    
    
#Escritura


#Para determinar que utilizaremos permisos de escritura, se agrega el parámetro write ("w")
#En caso de no encontrar el archivo, lo crea
with open("texto.txt", "w", encoding="UTF-8") as archivo:
    #Esto sobreescribe en el archivo
    """archivo.write("Estamos escribiendo en el archivo")"""
    #Es el proceso inverso a readlines(), se necesita pasar como una lista en caso de contener más de una línea
    #Si se utilizan dos líneas de código con writelines(), el contenido se "concatena"
    archivo.writelines(["Estamos escribiendo nuevamente\n", "Otras líneas\n"])
    archivo.writelines("Y esto se esta agregando")
    
#Con el parámetro append ("a") agregamos lo que deseemos escribir (no lo sobrescribe)
with open("texto.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Hola jiji\n")