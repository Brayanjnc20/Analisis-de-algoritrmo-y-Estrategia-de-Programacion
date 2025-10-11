"""
Cree la funcion PrimMayusc que pondra en mayuscula la primera letra de cualquier
palabra de una oracion. Use recursion, que cordar un string se coporta como 
lista de letras
pe: el joven saca su celular
retorna:El Joven Saca Su Celular
"""

def longitud(texto):
    if texto == "":
        return 0
    return 1 + longitud(texto[1:])


def PrimMayusc(texto, i=0):
    if i == longitud(texto):
        return ""
    if i == 0 or texto[i - 1] == " ":
        return texto[i].upper() + PrimMayusc(texto, i + 1)
    else:
        return texto[i] + PrimMayusc(texto, i + 1)
print("Retorna:", PrimMayusc("el joven saca su celular"))