def funcion_decoradora(funcion_parametro):
        def funcion_interior():
            print("lo que quiero poner antes")
            funcion_parametro()
            print("lo que quiero poner despues")

        return funcion_interior
@funcion_decoradora
def suma():
    print(2+5)

def resta():
    print(10-8)

suma()

resta()

def funcion(valor,tasa = 0.15):
    print("funcion tasa")
    print (tasa, valor)

funcion(3, tasa = 0.25)