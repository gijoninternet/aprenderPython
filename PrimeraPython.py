texto = "en un lugar de la mancha de cuyo nombre no puedo acordarme hace mucho que vivia a a a b b b c c"

texto_dividido= texto.split()

d= {'a':3}

#d = {'uno': 1, 'dos': 2, 'tres': 3}
#print(d.get('a'))
for palabra in texto_dividido:
    print (palabra)
    contador = d.get(palabra)
    if contador is not None:
        d[palabra] = contador + 1
    else:
        d[palabra] =  1


print (d)

print (d.keys)
