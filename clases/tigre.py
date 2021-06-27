from .animal import Animal

class Tigre(Animal):
    def __init__(self, nombre, edad, salud=60, felicidad=60, paisOrigen):
        super().__init__(nombre, edad)
        self.salud = salud
        self.felicidad = felicidad
        self.origen = paisOrigen

    def alimentacion(self, alimento=True):
        if alimento:
           self.salud +=1
           self.felicidad +=1
        return self  