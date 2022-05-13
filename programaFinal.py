'''
Gabriel Portillo Gonzalez    6°B    ICI
PROGRAMA FINAL DE OPTATIVA I

'''

import os 

carpeta_nombre="C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos\\"

archivo_salida="UNION.txt"

simbolos = ["(",")",",",".",";",":","\""]

texto_junto = ""

archivos_lista = os.listdir(carpeta_nombre)

#contar las lineas con texto y vacias.
print("numero de lineas, lineas con texto, lineas vacias\n")
for archivo_nombre in archivos_lista:
    with open(carpeta_nombre+archivo_nombre,"r") as archivo:
        lineas_lista = archivo.readlines()
    num_linea = 1
    num_texto = 0
    num_vacio = 0
    for linea in lineas_lista:
        if linea.strip() == "":
            num_linea = num_linea + 1
            num_vacio = num_vacio+1
        else: 
            num_linea = num_linea+1
            num_texto = num_texto+1
    print(f"{archivo_nombre}, tiene: {num_linea} lineas, {num_texto} lineas con texto y {num_texto} lineas con texto\n")

print("\n")

#Muestra cuantas palabras contiene cada documento, las muestra ordenada en una lista y elimina los simbolos de puntacion.
print("muestra el total de palabras y las imprime en una lista\n")
for archivo_nombre in archivos_lista:
    print("\nARCHIVO ", archivo_nombre)
    with open(carpeta_nombre+archivo_nombre,"r") as archivo:
        texto = archivo.read()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " ")
    texto_junto = texto_junto + texto + "\n"
    palabras_lista = texto.split()
    palabras_lista.sort()
    print("Tiene ", len(palabras_lista), " palabras.")
    
    print(f"{palabras_lista}\n")

#une los textos, muestra cuantas palabras tiene, las imprime en lista y elimina los simbolos de puntacion.
print("une los documentos, muestra el numero de palabras y las imprime en una lista")
with open(carpeta_nombre+archivo_salida,"w") as salida:
    salida.write(texto_junto)

with open(carpeta_nombre+archivo_salida,"r") as archivo:
    texto = archivo.read()

print("\nArchivo ", archivo_salida)
palabras_lista = texto.split()
palabras_lista.sort()
print("\nTiene ", len(palabras_lista), " palabras.")

print(palabras_lista)

with open(carpeta_nombre+archivo_salida,"r") as archivo:
    lineas_lista = archivo.readlines()

#buscar la palabra
palabra = input("\n¿cual palabra desea buscar?: ")
num_palabras=0

for linea in lineas_lista:
    if linea.strip() != "":
        if palabra in linea:
            num_palabras = num_palabras+1

print(f"{palabra} hay:{num_palabras} veces en el documento.")

