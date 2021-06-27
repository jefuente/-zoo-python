from .animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, salud=30, felicidad=30, sexo):
        super().__init__(nombre, edad)
        self.salud = salud
        self.felicidad = felicidad
        self.sexo = sexo

    def alimentacion(self, alimento=True):
        if alimento:
           self.salud +=20
           self.felicidad +=20
        return self   
    