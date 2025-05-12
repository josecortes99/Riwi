lista =[]

for i in range(5):
    Numero = int(input ("\ningrese un numero: "))
    if Numero % 2 == 0:
        lista.append(Numero)
        print ("\nNumeros ingresados: ", lista)