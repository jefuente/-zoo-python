from .animal import Animal

class Tigre(Animal):
    def __init__(self, nombre, edad, salud=60, felicidad=70, paisOrigen="India"):
        super().__init__(nombre, edad)
        super().display_info()
        self.alimentacion()
        self.salud = salud
        self.felicidad = felicidad
        self.origen = paisOrigen

    def alimentacion(self):
        self.salud +=1
        self.felicidad +=1
        return self  