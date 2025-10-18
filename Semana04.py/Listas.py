muebles = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
a = muebles[0:len(muebles)//2] # Para sacar la midad de una lista se utiliza el len(nombre de la lista)/2
print(a)

print('banco' in muebles) # Pregunta si banco esta dentro de la lista

cosas = ['table', 'chair', 'rack','shelf']
table, chair, rack, shelf = cosas
table, chair, rack, shelf = ['table', 'chair', 'rack','shelf']


# INTERCAMBIAR VALORES
e = 10
f = 20

tmp = e
e = f
f = tmp
print (e, '', f)

e,f = f,e