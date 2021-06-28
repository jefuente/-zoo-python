from .animal import Animal

class Oso(Animal):
    def __init__(self, nombre, edad, salud=40, felicidad=50, peso=100):
        super().__init__(nombre, edad)
        super().display_info()
        self.alimentacion()
        self.salud = salud
        self.felicidad = felicidad
        self.peso = peso

    def alimentacion(self):
        self.salud +=5
        self.felicidad +=5
        return self  