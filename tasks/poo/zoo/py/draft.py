from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou {self.nome}!")
    
    @abstractmethod
    def fazerSom(self):
        pass
    @abstractmethod
    def mover(self):
        pass

class Lontra(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def fazerSom(self):
        print("ohohoh uhuh oh")

    def mover(self):
        print("nadar")

class Furao(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazerSom(self):
        print("haahha ahaha")
    
    def mover(self):
        print("correr, pular")
    
class Porquinho_da_india(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazerSom(self):
        print("uiuiui uiiui")
    
    def mover(self):
        print("correr")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazerSom()
    animal.mover()
    print(f"{type(animal).__name__}")


zoo: list[Animal] = [
    Lontra("Otto"),
    Furao("Pan"),
    Porquinho_da_india("Hilary"),
    ]

print("# teste")
print()

for animal_inst in zoo:
    apresentar(animal_inst)