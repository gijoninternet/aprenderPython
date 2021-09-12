def gen_diez_numeros(inicio):
    fin = inicio + 10    
    while inicio < fin:
        inicio+=1
        yield inicio, fin

for inicio, fin in gen_diez_numeros(23):
    #print("hola")
    print(inicio, fin)

    # Declara el generador con un bucle infinito que almacena los valores enviados
