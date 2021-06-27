from .animal import Animal

class Oso(Animal):
    def __init__(self, nombre, edad, salud=40, felicidad=40, peso):
        super().__init__(nombre, edad)
        self.salud = salud
        self.felicidad = felicidad
        self.peso = peso

    def alimentacion(self, alimento=True):
        if alimento:
           self.salud +=5
           self.felicidad +=5
        return self  