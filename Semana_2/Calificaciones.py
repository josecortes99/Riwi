print("\n---Sistema de calificaciones---") 
calificaciones = []  # creamos lista vacia

while True:
    try:
        calificacion = float(input("\nIngrese una calificacion de 0 a 100: "))  #pedimos al usuario un calificacion 

        if 0 <= calificacion <= 49:  #verificammos que la calificacion este en el rango de 0 a 49 es repobrado
            print("\nReprobaste")
            break
        elif 50 <= calificacion <= 100:  #verificammos que la calificacion este en el rango de 50 a 100 es aprobado
            print("\nAprovaste, felicitaciones")
            break
        else:
            print("\n###Error, ingrese una nota valida")  #Error si se ingresa una nota que se salga del rango de 0 a 100
                
    except ValueError:
        print("\n###Error, Ingrese solo numeros")  #Error si se ingresa un caracter o una letra diferente a un numero

print("\n---Agregue calificaciones a la lista---")
while True:
    try:
        numero = int(input("\nCuantas calificaciones desea agregar?: "))  #pedimos al usuario un cuantas calificacines desea ingresar a la lista 
        
        for i in range(numero):  #el ciclo for es para que pida la informacion tantas veces se desea
            Calificacion = float(input("\nIngrese la calificacion: "))  #pedimos al usuario que ingrese las calificaciones
            calificaciones.append(Calificacion)  #agregamos los datos a la lista 
        
        print(f"\nLista actualizada: {calificaciones}")
        suma = sum(calificaciones)  #se suman los elementos de la lista con sum()
        cantidad = len(calificaciones)  #trae el numero de registros la lista
        promedio = suma / cantidad  #se hace la operacion para el promedio
        print(f"\nEl promerdio de las notas es: {promedio}")
        break
    
    except ValueError:
        print("\n###Error, ingrese solo numeros###")  #Error si se ingresa un caracter o una letra diferente a un numero
        
print("\n---Ingrese una calificacion para ver cuantas hay mayores a la nota ingresada---")
while True:
    try:
        numesp = float(input("\nIngrese una calificacion : "))  #pedimos al usuario una calificacion
        if numesp in calificaciones:  #verificamos que el numero ingresado este dento de la lista 
            cant = sum(1 for cali in calificaciones if cali > numesp)  #expresion generadora para obtener la cantidad de numero de notas mayores a la ingresada
            print(f"\ncantidad de notas mayores: {cant}")
            break
        else:
            print("\n###Ingrese una calificacion que este dentro de la lista###")  #Error si se ingresa una nota que no este en la lista 
        
    except ValueError:
        print("\n###Error, Ingrese solo numeros###")  #Error si se ingresa un caracter o una letra diferente a un numero
        
print("\n---Ingrese una calificacion para ver cuantas veces se repite en la lista---")
while True:
    try:
        calesp = float(input("\nIngrese una calificacion: "))  #pedimos al usuario una calificacion
        
        if calesp in calificaciones:  #verificamos que la calificacion ingresada este dento de la lista 
            cont = calificaciones.count(calesp)  #utilizamos count para contar cuantas veces esta el dato ingresado
            print(f"\n{calesp} esta {cont} veces en la lista")
            break
        else:
            print("\n###Error, la calificacion no esta en la lista###")  #Error si se ingresa una nota que no este en la lista 
        
    except ValueError:
        print("\n###Error, ingrese solo numeros###")  #Error si se ingresa un caracter o una letra diferente a un numero
    
print("\n-----Hasta luego,-----")