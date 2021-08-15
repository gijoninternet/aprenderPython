from io import open
# archivo_texto=open("archivo.txt","w")
# frase_grabar="esto es un ejemplo \n otra linea"
# archivo_texto.write(frase_grabar)
# archivo_texto.close() 

# archivo_texto =open("archivo.txt","r")
# lectura=archivo_texto.read()
# print(lectura)
# archivo_texto.close() 

# archivo_texto =open("archivo.txt","r")
# lectura=archivo_texto.readlines()
# print(lectura)
# archivo_texto.close()
# print("lectura de array")
# for linea in lectura:
#     print(linea)

# archivo_texto =open("archivo.txt","a") #lo añade al principio
# lectura=archivo_texto.write("\notra linea mas")
# archivo_texto.close()

archivo_texto =open("archivo.txt","a")
lectura=archivo_texto.write("\notra linea mas")
archivo_texto.close()

