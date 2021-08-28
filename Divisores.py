lista_primos_menos= [2,3,5,7,11,13,17,19,23]
lista_primos=[2,3,5]
numero=121
dic_divisores={1:1}



def divisores_primos(numero):
    primo_encontrado = None
    for primo in lista_primos:
        if numero %primo==0:
            primo_encontrado=primo
            break 
    return primo_encontrado

def divisores_dividiendo(numero):
    primo_encontrado = None
    for primo_prueba in range(2, int(numero/2)):
        if numero%primo_prueba == 0:
            primo_encontrado=primo_prueba

    return primo_encontrado
   

print("calculo divisores del numero ",numero)

dic_divisores[numero]=1
primo=divisores_primos(numero)
while (primo is not None):
    contador = dic_divisores.get(primo)
    if contador is not None:
        dic_divisores[primo] = contador + 1
        
        
    else:
       dic_divisores[primo] = 1 
    numero=numero/primo
    primo=divisores_primos(numero)
else:
    print("buscar primos dividiendo hasta numero/2 de ", numero )
    primo=divisores_dividiendo(numero)
    while (primo is not None):
        contador = dic_divisores.get(primo)
        if contador is not None:
            dic_divisores[primo] = contador + 1    
        else:
            dic_divisores[primo] = 1 
        numero=numero/primo
        primo=divisores_dividiendo(numero)

    

print("divisores encontrados de ",numero,dic_divisores)


