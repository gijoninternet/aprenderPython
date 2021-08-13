class Vehiculo:
    def __init__(self,marca,ruedas,motor):
        self.marca = marca
        self.ruedas =ruedas
        self.motor = motor

    def __str__(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde __str")
    def __descripcion__(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde __descripcion__")
    def __descripcion(self):
        return (f" Marca: {self.marca}, Motor: {self.motor}, Ruedas: {self.ruedas} desde descripcion")

vehi= Vehiculo("Kia ceed",4,"diesel")
print(str(vehi))
print(vehi.__str__())
print((vehi.__descripcion__()))
print(vehi.__descripcion())