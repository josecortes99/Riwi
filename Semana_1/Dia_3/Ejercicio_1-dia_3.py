Biblioteca = {
    '001': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967},
    '002': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949},
    '003': {'titulo': 'Orgullo y prejuicio', 'autor': 'Jane Austen', 'año': 1813},
    '004': {'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'año': 1605},
    '005': {'titulo': 'El nombre de la rosa', 'autor': 'Umberto Eco', 'año': 1980}
}

while True:
    
    print("\n---Bienvenido a la biblioteca Riwi, elija una opcion---")
    print("1: Crear libro")
    print("2: Lista de libros")
    print("3: Buscar un libro")
    print("4: Modificar libros")
    print("5: Eliminacion de libros")
    print("6: Salir")
        
        
    opcion = int(input("\nIngrese una opcion: "))
            
    if opcion == 1:
        CrearLibro()
    elif opcion == 2:
        ListaLibros()
    elif opcion == 3:
        Buscar()
    elif opcion == 4:
        Actualizar()
    elif opcion == 5:
        Eliminar()
    elif opcion == 6:
            print("\n---Gracias por visitarnos---")
            break
    else:
            print("\n###Error, Ingrese una opcion valida###")

def CrearLibro():
    
 
def ListaLibros():
    print("\nLista de libros:")
    for valor in Biblioteca.items():
        print(f"{valor}")

def Eliminar():
    while True:
        Id = input("\nIngrese el id a eliminar: ")
        if Id in Biblioteca:
            Biblioteca.pop(Id)
            print("Biblioteca actualizada: ")
            for valor in Biblioteca.items():
                print(f"{valor}")
            break
        else:
            print("\nIngrese un id valido")
            
def Actualizar():
    while True:
        Id = input("\nIngrese el id a actualizar: ")
        if Id in Biblioteca:
            Actualiza = int(input("\nQue quieres actualizar? (1. Titulo, 2. Autor, 3. año de publicacion) ó ingrese alguna letra para salir: "))
            if Actualiza == 1:
                Titulo = input("\nAgregue el nuevo Titulo: ").strip()
                Biblioteca[Id]["titulo"] = Titulo
                break
            elif Actualiza == 2:
                Autor = input("\nIngrese el nuevo autor: ").strip()
                Biblioteca[Id]["autor"] = Autor
                break
            elif Actualiza == 3:
                Year = int(input("\nIngrese un año nuevo: "))
                Biblioteca[Id]["año"] = Year
                break
            else:
                print("\nHasta luego")
                break
        else:
            print("\n###Error, ingrese un id valido###")

def Buscar():
    
            
def menu():
             
menu()
    
        



    
    
    
             
             
         



