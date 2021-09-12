# numero=20
# lista=[2] + list(range(3, int(numero/2 +1),2))
# #lista2= range(2) + lista

# print(lista)
# #listados= list(lista)
# #print(lista2)
# for primo_prueba in lista:
#     print(primo_prueba)

lista_primos= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#lista_primos=[]
numero_inicial=5


numero=numero_inicial
dic_primos={1:1}



def primos_util_lista_primos(numero):
    primo_encontrado = None
    
    for primo in lista_primos:
        if primo>numero:
            break
        if numero %primo==0:
            primo_encontrado=primo
            print("encontrado primos_util_lista_primos ",numero,primo)
            break 
    yield primo_encontrado

dic_primos[numero_inicial]=1
primo=primos_util_lista_primos(numero_inicial)
print("primo",primo)
while (primo is not None):
    contador = dic_primos.get(primo)
    if contador is not None:
        dic_primos[primo] = contador + 1

    else:
       dic_primos[primo] = 1 
    
    #numero=int(numero/primo)
    
    #primo=primos_util_lista_primos(numero)
    #primo=next(primo)