# Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta"

while (True):
    
    Password = input ("\nIngrese su contraseña: ")
    
    if Password == "python123":
        print ("Acceso concedido")

    else:
        print ("\nContrasña incorrecta, ingrese la contraseña correcta")
    