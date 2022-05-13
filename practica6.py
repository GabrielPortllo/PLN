'''
Gabriel Portillo Gonzalez    6°B    ICI

'''
import os

carpeta_nombre = "C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos\\"

archivo_lista = os.listdir(carpeta_nombre)
for archivo_nombre in archivo_lista:
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_listas = archivo.readline()
    archivo.close()
    logitud = len(lineas_listas)
    print(f"{archivo_nombre} tiene {logitud} lineas\n")

    archivo = open(carpeta_nombre+archivo_nombre)
    texto = archivo.read()
    archivo.close()

    simbolos = ["(",")",",",".",";",":","\""]
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " " + simbolo + " ")

    palabras_lista = texto.split()
    palabras_lista.sort()
    for palabra in palabras_lista:
        print(palabra)

