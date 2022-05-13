carpeta_nombre="C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"
archivo_nombre="UNION.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," "+simbolo+" ")

palabras_lista=texto.split()

palabras_unicas=[]

for palabra in palabras_lista:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)

print(palabras_unicas)
num=len(palabras_unicas)
print(num, " palabras en el documento")
print(len(palabras_lista), " palabras en todo el documento")