"""
muestra la suma de los numeros pares entre 0 y un numero indicado por 
el usuario. use una funcion recursiva
sumaPares(6) = 12
 01,2,3,4,5,6
 2+4+6=12
"""

def sumaPares(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        return n + sumaPares(n - 2)
    else:
        return sumaPares(n - 1)

num = int(input("Ingrese un número: "))
print("La suma de los números pares entre 0 y", num, "es:", sumaPares(num))