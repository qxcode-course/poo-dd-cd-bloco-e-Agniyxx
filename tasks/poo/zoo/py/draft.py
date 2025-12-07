from abc import ABC, abstractmethod

class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print("Eu sou um(a) {self.nome}!")
    
    @abstractmethod
    def fazerSom(self):
        pass
    def mover(self):
        pass

class Lontra(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def fazerSom(self):
        return super().fazerSom()
    
    def mover(self):
        return super().mover()

class Furao(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazerSom(self):
        return super().fazerSom()
    
    def mover(self):
        return super().mover()
    
class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazerSom(self):
        return super().fazerSom()
    
    def mover(self):
        return super().mover()

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazerSom()
    animal.mover()

    print("{type(animal).__name__}")


zoo: list[Animal] = [
    Lontra("Otto")
    Furao("Pan")
    Rato("Stuart")
    ]

print("# teste")
print()

for animal_inst in zoo:
    apresentar(animal_inst)