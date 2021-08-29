lista_primos_menos= [2,3,5,7,11,13,17,19,23]
lista_primos=[]
numero_inicial=403
numero=numero_inicial
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
    #se prueba con el 2 y numeros impares
    lista_numeros_probar=[2] + list(range(3, int(numero/2 +1),2))
    for primo_prueba in lista_numeros_probar:
        if numero%primo_prueba == 0:
            primo_encontrado=primo_prueba
            break
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
    numero=int(numero/primo)
    primo=divisores_primos(numero)
else:
    print("buscar primos dividiendo hasta numero/2 de ", numero )
    primo=divisores_dividiendo(numero)
    print("divisores_dividiendo de,", numero,primo)
    while (primo is not None):
        contador = dic_divisores.get(primo)
        if contador is not None:
            dic_divisores[primo] = contador + 1    
        else:
            dic_divisores[primo] = 1 
        numero=int(numero/primo)
        print("tipo",type(numero))
        primo=divisores_dividiendo(numero)
    else:
        #no ha encontrado divisor pero el numero existe
        if numero!=numero_inicial:
            contador = dic_divisores.get(numero)
            if contador is not None:
                dic_divisores[numero] = contador + 1    
            else:
                dic_divisores[numero] = 1 

    

print("divisores encontrados de ",numero,dic_divisores)


