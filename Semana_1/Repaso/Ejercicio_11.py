lista =[]

name = int(input("ingrese cuantos nombres desea ingresar: "))

for i in range(name):
    nombre = input ("\ningrese un nombre: ")
    lista.append(nombre)
    print ("\nNombres ingresados: ", lista)