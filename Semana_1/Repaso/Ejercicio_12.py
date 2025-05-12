frutas = ["manzana", "arroz", "pera"]
print ("\nLista de frutas", frutas)
eliminar = input ("\nElimine el elemento que no es una fruta: ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print ("\nFruta eliminada")
else:
    print ("\nLa fruta no esta en la lista")
    
print ("\nlista actualizada de frutas: ", frutas)