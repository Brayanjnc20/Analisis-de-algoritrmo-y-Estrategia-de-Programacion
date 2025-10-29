import random

entrada = input("Ingrese el tamaño de la matriz  que desea generar: ")
partes = entrada.split("x")
filas = int(partes[0])
columnas = int(partes[1])

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        palabra = ""
        for k in range(4):
            letra = chr(random.randint(97, 122))
            palabra += letra
        fila.append(palabra)
    matriz.append(fila)

for fila in matriz:
    print(" ".join(fila))

def Vocal(palabra):
    for letra in palabra:
        if letra in "aeiou":
            return True
    return False

def contar(m):
    if len(m) == 1:
        c = 0
        for p in m[0]:
            if Vocal(p):
                c += 1
        return c
    else:
        mitad = len(m) // 2
        return contar(m[:mitad]) + contar(m[mitad:])

total = contar(matriz)
print("Las Palabras econtradas con vocal son :", total)
