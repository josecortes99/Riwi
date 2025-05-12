Gestion = {}
Id = 0

def Agregar():
    while True:
        print("\n----- Ingresar estudiante -----")
        while True:
            Id = int(input("\nIngrese la identificacion del estudiante : "))
            if Id not in Gestion:
                break
            else:
                print("\nEl Id ya exite, agregue uno distinto")
        Nombre = input("\nIngrese el nombre del estudiante completo: ")
        Edad = int(input("\nIngrese la edad del estudiante: "))
        Nota = input("\nIngrese la nota del estudiante: ")
        Data = {"ID" : Id, "Nombre" : Nombre, "Edad" : Edad, "Nota" : Nota }
        Gestion[Id] = Data
        print(Gestion)
        break
    
def Buscar():
    while True:
        print("\n----- Buscar estudiante -----")
        Buscar = int(input("\nDesea buscarlo por (1. ID ó por 2. Nombre?): "))
        if Buscar == 1:
            while True:
                id = int(input("\nIngrese el ID que desea buscar: "))
                for Id, datos in Gestion.items():
                    if datos["ID"] == id:
                        print(f"\nDatos encontrados {Id} : {datos}")
                        return
                    else:
                        print("\nIngrese un ID valido")
        elif Buscar == 2:
            while True:
                Nombre = input("\nIngrese el nombre que desea buscar: ")
                if Nombre.isalpha():
                    for Id, datos in Gestion.items():
                        if datos["Nombre"] == Nombre:
                            print(Id, datos)
                            return
                else:
                    print("\nIngrese solo letras")
        else:
            print("\nOpcion no valida, ingrese existente")
            
def Actualizar():
    while True:
        print("\n------ Actualizar estudiante -----")
        act = int(input("\nQue desea actualizar? (1. Nota ó 2. Edad): "))
        if act == 1:
            nombre = input("\nIngrese nombre de un estudiante: ")
            for Id, datos in Gestion.items():
                if datos["Nombre"] == nombre:
                    nota = input("\nIngrese la nueva nota: ")
                    Gestion["Nota"] = nota
                    print(Gestion)
        
            
def menu():
    while True:
        try:
            print("\n-----Gestion de estudiantes-----")
            print("1. Agregar estudiante")
            print("2. Buscar estudiante")
            print("3. Actualizar datos del estudiante")
            print("4. Eliminar estudiante")
            print("5. Promedio notas estudaintes")
            print("6. Agregar estudiante")
            print("7. Lista estudiantes con notas inferiores")
            print("8. Salir")
            
            Opcion = int(input("\nIngrese una de las opciones: "))
            
            if Opcion == 1:
                Agregar()
            elif Opcion == 2:
                Buscar()
            elif Opcion == 3:
                Actualizar()
            elif Opcion == 8:
                print("\nHasta luego")
            else:
                print("\n### Error, ingrese un numero valido ###")
        except ValueError:
            print("\n### Error, ingrese solo numeros ###")
menu()