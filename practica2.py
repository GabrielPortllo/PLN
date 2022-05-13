'''Gabriel Portillo Gonzalez'''

carpeta_nombre="C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"

archivo_nombre="UNION.txt"

palabra = input("Cual palabra quieres busacar: ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

if palabra in texto:
    print(palabra, " fue encontrada en el texto.")
else:
    print(palabra, " no fue encontrada en el texto.")