from abc import ABC, abstractmethod

preço_carro = 5.0
preço_moto = 3.0
preço_bike = 1.0

class Veiculo:
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.entrada: float | None = None
        self.tipo = tipo

    def setEntrada(self, horaEntrada: int):
        self.entrada = horaEntrada

    def getEntrada(self):
        return self.entrada 
    
    def getTipo(self):
        return self.tipo
    
    def getId(self):
        return self.id

    @abstractmethod
    def calcularValor(self):
        pass

    def __str__(self):
        tipo_str = self.tipo.rjust(10, "-")
        id_str = self.id.rjust(10, "-")
        return f"{tipo_str}, {id_str}, {self.entrada}"

class Bike(Veiculo):
    def __init__(self, id, entrada, tipo):
        super().__init__(id, entrada, tipo)

    def calcularValor(self):
        return super().calcularValor()

class Moto(Veiculo):
    def __init__(self, id, entrada, tipo):
        super().__init__(id, entrada, tipo)

    def calcularValor(self):
        return super().calcularValor()

class Carro(Veiculo):
    def __init__(self, id, entrada, tipo):
        super().__init__(id, entrada, tipo)

    def calcularValor(self):
        return super().calcularValor()
    
class Estacionamento():     
    def __init__(self, veiculos: Veiculo, horaAtual: int):
        self.veiculos = {}
        self.horaAtual = horaAtual

    def procurarVeiculo(self, id: str):
        return self.id.veiculos.get(id)

    def estacionar(self, veiculo: Veiculo):
        if veiculo.getId() in self.veiculos:
            print("Erro: ")
        return

    def pagar(self):
        veiculo = self.procurarVeiculo(id)
        if not veiculo:
            print(f"Erro: veiculo {id} não encontrado")
            return
        valor = veiculo.calcularValor(self.horaAtual)
        veiculo.setPago(True)

    def sair(self, id: str):
        veiculo = self.procurarVeiculo(id)
        if not veiculo:
            print("")

    def passarTempo(self, tempo: int):
        self.horaAtual += tempo
        print(f"Hora Atual: {self.horaAtual:02d}h")

    def __str__(self):
        return super().__str__()

def main():
    estacionamento = Estacionamento()
    while True:

        line = input()
        print(f"$+{line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "estacionar":
            tempo = args[1]
            estacionamento.passarTempo(tempo)
        elif args[0] == "pagar":
            id = args[1]
            estacionamento.pagar(id)
        elif args[0] == "sair":
            id = args[1]
            estacionamento.sair(id)    

main()