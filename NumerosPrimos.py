lista_primos= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#lista_primos=[]
numero_inicial=888844555


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
    return primo_encontrado

def primos_dividiendo(numero):
    primo_encontrado = None
    #se prueba con el 2 y numeros impares
    print("primos_dividiendo numero:", numero)
    lista_numeros_probar=[2] + list(range(3, int(numero/2 +1),2))
    print("numeros a dividir", lista_numeros_probar)
    for primo_prueba in lista_numeros_probar:
        if numero%primo_prueba == 0:
            primo_encontrado=primo_prueba
            print("encontrado:", primo_prueba )
            break
    return primo_encontrado
   

print("calculo divisores del numero ",numero_inicial)

dic_primos[numero_inicial]=1
primo=primos_util_lista_primos(numero_inicial)
while (primo is not None):
    contador = dic_primos.get(primo)
    if contador is not None:
        dic_primos[primo] = contador + 1

    else:
       dic_primos[primo] = 1 
    numero=int(numero/primo)
    
    primo=primos_util_lista_primos(numero)
else:
    print("buscar primos dividiendo hasta numero/2 de ", numero )
    primo=primos_dividiendo(numero)
    print("primos_dividiendo de,", numero,primo)
    while (primo is not None):
        contador = dic_primos.get(primo)
        if contador is not None:
            dic_primos[primo] = contador + 1    
        else:
            dic_primos[primo] = 1 
        numero=int(numero/primo)
        primo=primos_dividiendo(numero)
    else:
        #no ha encontrado divisor pero el numero existe
        if numero!=numero_inicial and numero!=1:
            contador = dic_primos.get(numero)
            if contador is not None:
                dic_primos[numero] = contador + 1    
            else:
                dic_primos[numero] = 1 

    

print("primos encontrados de ",numero_inicial,dic_primos)


