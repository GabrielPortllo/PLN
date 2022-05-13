'''Gabriel Portillo Gonzalez'''

import os

carpeta_nombre = "C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"

carpeta_salida = "C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"

archivo_saldia = "UNION.txt"

archivo_lista = os.listdir(carpeta_nombre)

union =""
for archivo_nombre in archivo_lista:
    archivo = open(carpeta_nombre + archivo_nombre)
    texto = archivo.read()
    archivo.close()
    union+=texto

with open(carpeta_salida+archivo_saldia, "w") as salida:
    salida.write(union)