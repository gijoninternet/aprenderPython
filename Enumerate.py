# users = ["Test User", "Real User 1", "Real User 2"]
# for index, user in enumerate(users):
#      if index == 0:
#          print("Extra verbose output for:", user)
#      print(index, user)

def even_items(iterable):
 #   """Return items from ``iterable`` when their index is even.""", devuelve las lineas pares
    values = []
    for index, value in enumerate(iterable, start=1):
            #if not index % 2: 
            if index % 2 == 0:
                values.append(value)
    return values

lineas=["la bella y graciosa moza","marchose a lavar la ropa","la mojo en el arroyuelo","y cantando","la lavo"]
print(lineas)
print(even_items(lineas))

def even_items2(iterable):
 #   """Return items from ``iterable`` when their index is even.""", devuelve las lineas pares
    values = []
    print([v for i, v in enumerate(iterable, start=1) if not i % 2])
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]
    

lineas=["la bella y graciosa moza","marchose a lavar la ropa","la mojo en el arroyuelo","y cantando","la lavo"]
print("even_items2")
print(lineas)
print(even_items2(lineas))
print(even_items2("abcdefghijklmnopqrstuvwxyz"))

lista = [1, 3.1416, 'j', 'j','jarroba.com',  True]
print ('Imprimimos los elementos de una lista y el tipo de dato de cada elemento', lista)
for l in lista:
    print ('%s - %s' %(l, type(l)))
#del lista[:]
print(lista.index('j'))
print(lista.index('j',3))
print('cuenta jotas',lista.count('j'))

print("longitud de la lista",len(lista))

print("que es esto")
n_range=[2**k for k in range(2, 20)]
n_range2=[k for k in range(2, 20)]
print (n_range)
print (n_range2)
arr=[]
for k in range(2, 20):
    arr.append (k)
print("array", arr)

lista = [x for x in range(6)]
print(lista)

print(range(7))
lista2=range(6)
print(lista2)
print([x for x in "banana" if (x in 'aeioun')])