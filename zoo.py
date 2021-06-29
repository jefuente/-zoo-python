from clases.animal import Animal
from clases.leon import Leon
from clases.oso import Oso
from clases.tigre import Tigre
from colorama import init, Fore, Back, Style
init()

class Zoo:
    def __init__(self, nombre):
        self.animales = []
        self.nombre = nombre
    def add_leon(self, nombre):
        self.animales.append(nombre)
        return self
    def add_oso(self, nombre):
        self.animales.append(nombre)   
        return self 
    def add_tigre(self, nombre):
        self.animales.append(nombre)
        return self
    def print_all_info(self):
        print("-"*30, self.nombre, "-"*30)
        for animal in self.animales:       
            animal.display_info()
        return self
zoo1 = Zoo("Zoo_Metropolitano")
nala=Leon("Nala", 10)
zoo1.add_leon(nala)
simba=Leon("Simba", 20)
zoo1.add_leon(simba)
rajah=Tigre("Rajah", 15)
zoo1.add_tigre(rajah)
sherekhan=Tigre("Shere Khan", 12)
zoo1.add_tigre(sherekhan)
yogui=Oso("Yogui", 15)
zoo1.add_oso(yogui)
winniethepoo=Oso("Winnie The Poo", 15)
zoo1.add_oso(winniethepoo)

zoo2 = Zoo("Zoo_Quilpue")
leoncio=Leon("Leoncio", 15)
zoo2.add_leon(leoncio)
mufasa=Leon("Simba", 10)
zoo2.add_leon(mufasa)
tiguer=Tigre("Tiguer", 5)
zoo2.add_tigre(tiguer)
tigresadeloriente=Tigre("Tigresa del oriente", 25)
zoo2.add_tigre(tigresadeloriente)
cariñosito=Oso("Cariñosito", 7)
zoo2.add_oso(cariñosito)
anteojitos=Oso("Anteojitos", 17)
zoo2.add_oso(anteojitos)

zoo1.print_all_info()
zoo2.print_all_info()

simba.alimentacion()
sherekhan.alimentacion()
cariñosito.alimentacion()
tiguer.alimentacion()

zoo1.print_all_info()
zoo2.print_all_info()

