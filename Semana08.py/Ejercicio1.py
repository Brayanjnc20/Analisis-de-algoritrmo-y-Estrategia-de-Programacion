"""
Cree la funcion minPar qye reciba una lista de numeros enterios de parametro 
y retorne el minimo par, la lista esta desordenada. Use recursion
pe [8, 3, 6, 9, 10]
resultado: 6 

"""
#Ejemplo 1
def minPar(lista):
    if not lista:
        return None
    x = lista[0]
    m = minPar(lista[1:])
    if x % 2 != 0:
        return m
    if m is None or x < m:
        return x
    return m
numeros = [8, 3, 6, 9, 10]
print("Resultado:", minPar(numeros))

#Ejemplo2
def minpar(lista):
    if not lista:
        return None
    primero = lista[0]
    resto = minpar(lista[1:])
    if primero % 2 != 0:
        return resto
    if resto is None:
        return primero
    return primero if primero < resto else resto
numeros = [18,7,2,9,10]
print(minpar(numeros))