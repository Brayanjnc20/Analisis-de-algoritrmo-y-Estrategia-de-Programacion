
def duplicados(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i+1,n):
            if lista[i] == lista[j]:
                return "Verdadero" # Se encontro un valor duplicado
    return "Falso"

lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,2,5]    

print(duplicados(lista1)) # No existe valores duplicados
print(duplicados(lista2)) # Si existe valores duplicados
