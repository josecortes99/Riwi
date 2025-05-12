Inventario = []
Id = 0

#Añadir un producto
def Añadir():
    global Id
    
    while True:
        
        print("\033[34m\n-----Añadir producto-----")
        Id += 1 #Aumentomos el id 
        
        while True:
            Nombre = input("\033[0m\nIngrese el nombre del producto: ")    #Pedimos un nombre de producto
            if Nombre.isalpha():   #verificamos que nombre sea solo letras
                Ver = [producto["Nombre"] for producto in Inventario ]
                if Nombre in Ver:
                    print("\033[93m\nProducto ya existe, agregue otro")
                else:    
                    break
            else:
                print("\033[91m\n## Error, Ingrese solo letras ##")
                
        while True:
            Precio = input("\033[0m\nIngrese el precio del producto ej (7.800): ")    #Pedimos un precio
            if Precio.replace('.', '').isdigit():   #verificamos que el precio solo sea numeros
                Precio = float(Precio)
                break
            else:
                print("\033[91m\n## Error, Ingrese solo numeros ##")
                
        while True:
            Cantidad = input("\033[0m\nIngrese la cantidad disponible: ")    #Pedimos una cantidad
            if Cantidad.isdigit():   #verificamos que la cantidad solo sea numeros
                break
            else:
                print("\033[91m\n## Error, Ingrese solo numeros")
                
        Datos = {"ID" : Id, "Nombre" : Nombre, "Precio" : Precio, "Cantidad" : Cantidad}   # guardamos en una variable llamada data los datos del diccionario a agregar a la lista
        Inventario.append(Datos)    # se guarda el diccionario en la lista
        
        # preguntamos si desea agregar otro estudiante si si pide los dtos de nuevo si no continua 
        Opcion = input("\033[0m\nDesea agregar otro poducto? (si ó no): ").strip().lower()    #Pedimos una opcion para agregar otro producto
        if Opcion.isalpha():    # verificamos que nombre sea solo letras
            if Opcion == "no":
                print("\033[92m\nAgregado correctamente")
                print(f"\033[92mInventario actuaizado: {Inventario}")
                break
            else:
                print("\033[92m\nAgregado correctamente")
                print(f"\033[92m\nInventario actuaizado: {Inventario}")
        else:
            print("\033[91m\n## Error, Ingrese solo letras ##")
            
#Consultar un estudiante por nombre
def Consultar():
    
    while True:
        print("\033[34m\n-----Buscar producto-----")
        Buscar = input(("\033[0m\nIngrese el nombre del producto que quiere buscar: ")).strip()   #Pedimos un estudiante
        
        if Buscar.isalpha():    #Verificamos que nombre sea solo letras
            for datos in Inventario:    #Recorremos la lista 
                if datos["Nombre"] == Buscar:    #Si buscar es igual al nombre que esta en los datos muestra el diccionario con todos los datos
                    print("\033[92m\nInformacion: ") 
                    print(f"\033[92mUsuario encontrado: {datos}")
                    return
            else:
                print("\033[91m\n## Error, ingrese un nombre que este en el diccionario ##")
        else:
            print("\033[91m\n## Error, ingrese solo letras ##")        

#Actualizar el precio de un producto
def Actualizar():
    while True:
        print("\033[34m\n-----Actualizar precio-----")
        act = input("\033[0m\nInserte un producto para actualizar su precio: ")    #Pedimos un producto
        if act.isalpha():    #Verificamos que nombre sea solo letras
            for datos in Inventario:     #Recorremos la lista 
                if datos["Nombre"] == act:    #Si act es igual al nombre etre al if
                    while True:
                        valor = input("\033[0m\nInserte el nuevo valor: ")    #Pedimos el nuevo valor
                        if valor.replace('.', '').isdigit():    #Verificamos que nombre sea solo numeros
                            valor = float(valor)
                            datos["Precio"] = valor     #Si valor es igual al precio actualiza el precio de ese producto
                            print("\033[92m\nPrecio atualizado:")
                            print(f"{datos}")
                            return
                        else:
                            print("\033[91m\n## Error, ingrese solo numeros")    
            else:
                print("\033[91m\n## Error, ingrese un nombre existente ##")
        else:
            print("\033[91m\n## Error, ingrese solo letras ##")
            
#Eliminar un producto 
def Eliminar():
    while True:
        print("\033[34m\n---Eliminar producto---")
        eliminar = input("\033[0m\nIngrese el nombre del producto que quiere eliminar: ")    #Pedimos el prodcuto a eliminar 
        for datos in Inventario:    #Recorremos la lista 
            if datos["Nombre"] == eliminar:    #Verificamos que eliminar sea igual al nombre del diccionario
                Inventario.pop()    #Utilizamos pop() para eliminar todo el elemnto de la lista
                print(f"\033[92m\nInventario actualizado: {Inventario}")
                return
        else:
            print("\033[91m\n## Error, ingrese un usuario que exista ##")
    
#Creamos el menu
def menu():
    while True:
            
        #Opciones del menu 
        print("\033[0m\n-----Inventario de productos-----")
        print("\033[0m1. Añadir productos")
        print("\033[0m2. consultar productos")
        print("\033[0m3. Actualizar productos")
        print("\033[0m4. Eliminar productos")
        print("\033[0m5. Ver valor total del inventario")
        print("\033[0m6. Salir")
        
        opcion = input("\033[0m\nIngrese una opcion: ")    #Pedimos una opcion
        
        #segun la ocion que se ingrese ya ingresa a la opcion valida 
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                Añadir()
            elif opcion == 2:
                Consultar()
            elif opcion == 3:
                Actualizar()
            elif opcion == 4:
                Eliminar()
            elif opcion == 5:
                sumatoria = lambda Inventario: sum(float(producto["Precio"]) * int(producto["Cantidad"]) for producto in Inventario)   #Funcion lambda para calcular el total del inventario
                total=sumatoria(Inventario)
                total = float(total)
                print(f"\033[92m\nValor total de los productos del inventario: ${total:.3f}")
            elif opcion == 6:
                print("\n-----Hasta luego-----")
                break
            else:
                print("\033[91m\n### Error, ingrese una opcion valida ##")
        else:
            print("\033[91m\n###Error, solo ingrese numeros###")
menu()