'''Gabriel Portillo Gonzalez'''

print("Hola Mundo")


suma = 25+15

resultado = suma/2

print("resultado = ",resultado)


archivo=open("C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documento.txt")
print(archivo.read())

archivo2=open("C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documento1.txt","w+")
archivo2.write("Buenos dias amigazo")

archivo2=open("C:\\Users\\gabri\\Documents\\6B\\IA\\python\\documento1.txt")
print(archivo2.read())

archivo.close()
archivo2.close()