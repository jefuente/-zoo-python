from .animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, salud=30, felicidad=40, sexo="masculino"):
        super().__init__(nombre, edad)
        super().display_info()
        self.alimentacion()
        self.salud = salud
        self.felicidad = felicidad
        self.sexo = sexo

    def alimentacion(self):
        self.salud +=20
        self.felicidad +=20
        return self   