def busq_fuerza_fruta(lista,objet):
    for i in range(len(lista)):
        if lista[i] == objet:
            return i # si encuentra el objetivo retorna la posicion
    return -1 # si no lo encuentra , retorna a -1

ing = input("Ingrese lista de numeros separados por comas: ")
lis_ing = [int(num.strip()) for num in ing.split(',')]
objet = int (input("Indique el numero a buscar: "))
    
result = busq_fuerza_fruta(lis_ing,objet)

if result != -1:
    print(f"El numero encontrado en posicion {result}")
else:
    print(f"El numero buscado no se encuentra en la lista")  