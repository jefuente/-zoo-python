from .animal import Animal

class Tigre(Animal):
    def __init__(self, nombre, edad, salud=60, felicidad=70, paisOrigen="India"):
        super().__init__(nombre, edad)
        self.alimentacion()
        self.salud = salud
        self.felicidad = felicidad
        self.origen = paisOrigen

    def alimentacion(self):
        self.salud +=1
        self.felicidad +=1
        return self  

    def display_info(self):
        print(f"El nombre del animal es {self.nombre}, su salud es de {self.salud} y su felicidad es de {self.felicidad}")
        return self