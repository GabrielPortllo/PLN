'''Gabriel Portillo Gonzalez'''

from distutils import archive_util
import re

carpeta_nombre = "C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"

archivo_nombre = "docmento4.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

expresion_regular = re.compile(r"cliente")

resultados_busqueda = expresion_regular.finditer(texto)

for resultado in resultados_busqueda:
    print(resultado.group(0))

expresion_regular = re.compile(r"se+")

resultados_busqueda = expresion_regular.finditer(texto)

for resultado in resultados_busqueda:
    print(resultado.group(0))