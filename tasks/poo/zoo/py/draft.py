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
        

def apresentar(animal: Animal):
    




        