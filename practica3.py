'''Gabriel Portillo Gonzalez'''

carpeta_nombre="C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"
archivo_nombre="UNION.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista = archivo.readlines()

palabra = input("Cual palabra quieres busacar: ")
num_palabras = 0
num_linea = 1
num_texto = 0
num_vacio = 0

for linea in lineas_lista:
    if linea.strip() == "":
        num_linea = num_linea + 1
        print("Linea", num_linea,": Esta linea esta vacia.")
        num_vacio = num_vacio+1
    else:
        num_linea = num_linea+1
        print("Linea", num_linea, ": ", linea)
        num_texto = num_texto+1
        if palabra in linea:
            num_palabras = num_palabras+1

print("Total de lineas: ", num_linea)
print("Lineas con texto: ", num_texto)
print("Lineas vacias: ", num_vacio)
print(palabra, " se encuentra: ", num_palabras," veces en el documento.")