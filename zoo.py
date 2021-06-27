
from clases.leon import Leon
from clases.oso import Oso
from clases.tigre import Tigre
from colorama import init, Fore, Back, Style
init()

class Zoo:
    def __init__(self, nombre):
        self.animales = []
        self.name = nombre
    def add_leon(self, name):
        self.animales.append( Leon(name) )
    def add_tiger(self, name):
        self.animales.append( Tigre(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animales:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_leon("Nala")
zoo1.add_leon("Simba")
zoo1.add_tigre("Rajah")
zoo1.add_tigre("Shere Khan")
zoo1.print_all_info()

