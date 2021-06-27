
class Animal:
    def __init__(self, nombre, edad, salud=50, felicidad=50):
        self.nombre=nombre
        self.edad=edad
        self.salud=salud
        self.felicidad=felicidad
   
    def display_info (self):
        print(f"El nombre del animal es {self.nombre}, su salud es de {self.salud} y su felicidad es de ${self.felicidad}")
        return self

    def alimentacion(self, alimento=True):
        if alimento:
            self.salud +=10
            self.felicidad +=10
        return self    
