import re
texto = '''Hola maestro, esta es la cadena 1, como estas mi capitan ababababab
Esta es la linea 2 de texto 22542342 abbye
Y esta es la linea 3 definitiva mi capitan'''

#findall busca todas las coincidencias. flags sirve para agregar parametros como ignorecase (para ignorar mayúsculas y minúsculas)
"""resultado = re.findall("esta", texto, flags=re.IGNORECASE)
print(resultado)"""

#\d - busca dígitos numéricos del 0-9
#r nos sirve para indicar que buscaremos Regex
"""resultado = re.findall(r"\d", texto)
print(resultado)"""

#\D - busca todo, menos dígitos numéricos del 0-9
"""resultado = re.findall(r"\d", texto)
print(resultado)"""

#\w - busca alfanuméricos (A/a, Z-z, 0-9 y _)
"""resultado = re.findall(r"\w", texto)
print(resultado)"""

#\W - busca todo, menos alfanuméricos (A/a, Z-z, 0-9 y _)
"""resultado = re.findall(r"\W", texto)
print(resultado)"""

#\s - busca espacios en blanco (espacios, tabulaciones, saltos de línea)
"""resultado = re.findall(r"\s", texto)
print(resultado)"""

#\S - busca todo, espacios en blanco (espacios, tabulaciones, saltos de línea)
"""resultado = re.findall(r"\S", texto)
print(resultado)"""

#\n busca menos saltos en línea (\n)
"""resultado = re.findall(r'\ n', texto) (verificar el espacio en n)
print(resultado)"""

#\. busca todo, menos saltos en línea (\n)
"""resultado = re.findall(r'.', texto)
print(resultado)"""

#\- CANCELAR CARACTERES ESPECIALES
"""resultado = re.findall(r'\.', texto)
print(resultado)"""

#Buscar una cadena que busque un numero, seguido de un punto y un espacio
"""resultado = re.findall(r'\d.\s', texto)
print(resultado)"""

#^ (Alt Gr + { ) - Busca el contenido al comienzo de una línea
#flag M indica Multilínea (todas son nuevas líneas)
"""resultado = re.findall(r'^Esta', texto, flags=re.M)
print(resultado)"""

#$ - Busca el contenido al final de una línea
#flag M indica Multilínea (todas son nuevas líneas)
"""resultado = re.findall(r'capitan$', texto, flags=re.M)
print(resultado)"""

#{n} busca n cantidad de veces el valor de la izquierda
"""resultado = re.findall(r"\d{3}\s", texto)
print(resultado)"""

#{n, m} n es el mínimo, m es el máximo (dividirá la cadena en caso de ser más grande)
"""resultado = re.findall(r"\d{1,4}", texto)
print(resultado)"""

#busca la letra a, seguido de mínimo 2 o 3 letras b
"""resultado = re.findall(r"ab{2,3}", texto)
print(resultado)"""

#busca el conjunto de la letra ab mínimo 2 veces, máximo 3
"""resultado = re.findall(r"(ab){2,3}", texto)
#si encuentra 6 "ab", devolverá 2 "ab". Si encuentra 3, devolverá 1
print(resultado)"""

#busca las coincidencias de la letra a y/o b, cuando sean al menos 2 veces
"""resultado = re.findall(r"[ab]{2,3}", texto)
#si encuentra 6 "aababb", devolverá 3 elementos. Si encuentra "aabab", devolverá 1 elemento de 3 dígitos y un elemento de 2 dígitos
print(resultado)"""

# | busca una u otra (). No importa el orden en que las coloquemos, siempre mostrará primero aquella expresión a la que encuentre primero
resultado = re.findall(r"\d{2,4}|Hola", texto)
print(resultado)