from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, id: str, entrada: int, tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self):
        pass

    def __str__(self):
        pass

class Estacionamento(Veiculo):     
    def __init__(self, id, entrada, tipo):
        super().__init__(id, entrada, tipo)

    def procurarVeiculo(self, id: str):

    def estacionar(self, veiculo: Veiculo):
        