def seelec_ordenar(valor):
    for i in range(len(valor)):
        for j in range(i, len(valor)):
             if valor[i] > valor[j]:
                 valor[i],valor [j] = valor[j],valor[i] # Se intercambia los valores


lista = [64, 25, 12, 22, 11]
print("Lista original: ",lista)
seelec_ordenar(lista)
print("Lista ordenada: ",lista)