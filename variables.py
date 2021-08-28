def cambia(b):
    b += [5]
    return

a, b = [3], [4]
print(f"Al principio        : a = {a} b = {b}")
cambia(a)
print(f"Después de cambia(a): a = {a} b = {b}")
cambia(b)
print(f"Después de cambia(b): a = {a} b = {b}")
print("Programa terminado")


# def subrutina_ModGlobal_desdeSub():
#     #global a #  se define a como  la definida en la parte global a=3    
#     global a
#     a=1
#     print( a)
    
#      # asignamos el valor uno a la variable 'a' que es la global ahora
#     aa = 2 
#     print(a)
#     return

# print ("las sub solo alteran globales si se define como global en la sub")
# a = 3
# subrutina_ModGlobal_desdeSub()

# print(a)

# def subrutina_lasSubNoAlteranglobales():
#     #global a #  se define a como  la definida en la parte global a=3    
#     a=1
#     print( a)
    
#      # asignamos el valor uno a la variable 'a' que es la global ahora
#     aa = 2 
#     print(a)
#     return
# print ("las sub no alteran globales aunqur sean  mismo valor")
# a = 3
# subrutina_lasSubNoAlteranglobales()

# print(a)


def doblar_valores(numeros):
    pos = 0
    for valor in numeros:
        print (numeros[pos])
        numeros[pos] = numeros[pos]*3
        pos = pos+ 1
    print("dentro de doblar valores")
    print (numeros)
    # for i,n in enumerate(numeros):
    #     print("valores de i,n ",i,n)
    #     numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns.copy())
#doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]

print(ns)
doblar_valores(ns)  # modificamos directamente los elementos en la sub y afecta al principal también
print(ns)

# Assign string value
text = "Learn Python Programming"

# Slice using one parameter
sliceObj = slice(5)
print(text[sliceObj])  

# Slice using two parameter
sliceObj = slice(6,12)
print(text[sliceObj])  

# Slice using three parameter
sliceObj = slice(6,25,5)
print(text[sliceObj])

# Define a dictionary
customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali',
'02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}

# Append a new data
customers['05634'] = 'Mehboba Ferdous'

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
#name = input("Enter customer ID:")
name = '02457'
# Search the ID in the dictionary
for customer in customers:
    if customer == name:
        print(f"encontrado {name} {customers[customer]} ")
        break
print("lo buscamos con get", name, customers.get(name,"not found"))
elem=customers.get(name,"not found")
print(elem)