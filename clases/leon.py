from .animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad, salud=30, felicidad=40, sexo="masculino"):
        super().__init__(nombre, edad)
        self.alimentacion()
        self.salud = salud
        self.felicidad = felicidad
        self.sexo = sexo

    def alimentacion(self):
        self.salud +=20
        self.felicidad +=20
        return self 

    def display_info(self):
        print(f"El nombre del animal es {self.nombre}, su salud es de {self.salud} y su felicidad es de {self.felicidad}")
        return self  