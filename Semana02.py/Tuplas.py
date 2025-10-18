#EJERCICIO 01
tupla1 = (1,2,3,4,5)
print(tupla1[0]) #imprime el primer elemento de la tupla
print(len(tupla1)) #imprime la longitus de la tupla

print("\n") # salto de linea

#EJERCICIO 02
tupla_num = (1,2,3,2,4,2)
print(tupla_num.count(2))

#EJERCICIO 03 (UNION DE TUPLAS)
tupla_1 = ('P','a','s')
tupla_2 = ('i','p','n')
tupla_unida = tupla_1 + tupla_2
print(tupla_unida)

print("\n")


#EJERCICIO 04 RECORRIDO DE TUPLAS
recorrer_tupla = ('Pedro','Ana','Samuel')
i=0
while i<len(recorrer_tupla):
     print(recorrer_tupla[i])
     i+=1
