import pickle
# lista_nombres=["Miguel","Cathy","Catina","Guz"]

# fichero_binario=open("lista_nombres","wb")
# pickle.dump(lista_nombres,fichero_binario)

# fichero_binario.close()

fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)