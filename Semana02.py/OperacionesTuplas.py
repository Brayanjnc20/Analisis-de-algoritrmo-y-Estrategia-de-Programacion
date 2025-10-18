#EJERCICIO01 : CREACION DE TUPLAS
tupla1 = (1,2,3,2,4,5)
tupla2 = (3,4,5,6)

print(f"Tupla 1 : {tupla1}")
print(f"Tupla 2 : {tupla2}")

#EJERCICIO 02 : CONVERTIR SETS
set1 = set(tupla1)
set2 = set(tupla2)
print(f"\nSet 1 (de la tupla 1): {set1}")
print(f"\nSet 2 (de la tupla 2): {set2}")


#EJERCICIO 02 : UNION DE TUPLAS
unir_sets = set1.union(set2)
print(f"\nUnion de set: {unir_sets}")


#EJERCICIO 04 : INTERSECCION DE TUPLAS
intersec_sets = set1.intersection(set2)
print(f"\nInterseccion de set: {intersec_sets}")

diferen_sets = set1.difference(set2)
print(f"\nInterseccion de set: {diferen_sets}")
