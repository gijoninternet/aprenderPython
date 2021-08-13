class Vehiculo:
    def __init__(self,marca,ruedas,motor):
        self.marca = marca
        self.ruedas =ruedas
        self.motor = motor

    def __str__(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde __str")
    def __descripcion__(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde __descripcion__")
    def descripcion(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde descripcion")

vehi= Vehiculo("Kia ceed",4,"diesel")
print(str(vehi))
print(vehi.__str__())
print((vehi.__descripcion__()))
print(vehi.descripcion()) # este no se va a ver porque empieza por __ y no acaba por __

## Ejemplo de polimorfismo

class Moto(Vehiculo):
    def __init__(self,marca,ruedas,motor, cilindrada):
        super().__init__(marca,ruedas,motor)
        self.cilindrada = cilindrada
        
    def descripcion(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas}, cilindrada:{self.cilindrada}  desde descripcion")

class Bicicleta(Vehiculo):
    def __init__(self,marca,ruedas,motor, peso):
       super().__init__(marca,ruedas,motor)
       self.peso = peso
    def descripcion(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas}, peso:{self.peso}  desde descripcion")




moto = Moto("yamaha",2,"Gasolina","500cc")
print(moto.descripcion())

bici = Bicicleta("BH",2,"piernas","700gr")
print(bici.descripcion())

def polimorfismo(auto):
    print(auto.descripcion())

polimorfismo(moto)
polimorfismo(bici)

## Aqui se ve como se hace el polimorfismo, en la funcion polimorfismo se le mete una moto o una bici y llamamos a su descripcion porque su clase
## base también tiene el metodo descripcion pero sabe llamar a la implementación adecuada de cada objeto.