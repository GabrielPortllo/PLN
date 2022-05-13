'''Gabriel Portillo Gonzalez'''

from tkinter import simpledialog
import nlkt
import matplotlib

carpeta_nombre="C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documentos"

archivo_nombre = "DocCompleto.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

for token in tokens:
    print(token)

palabras_totales = len(tokens)
print("Palabras totales: ", palabras_totales)

print("\n")

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto)

distribucion.plot()

print("\n")

hapaxes = distribucion.hapaxes()

for hapax in hapaxes:
    print(hapax)
