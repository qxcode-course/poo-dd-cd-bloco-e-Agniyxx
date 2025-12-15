from abc import ABC, abstractmethod

class MetodoPag(ABC):
    def __init__(self, valor: float, descricao: str, metodo):
        self.valor = valor
        self.descricao = descricao
        self.metodo = metodo

    @abstractmethod
    def processar_pag(self, valor: float):
        pass

    def pagar(self):
        self.metodo.processar_pag(self.valor)

    def resumo(self):
        return f" Pagamento de R$ {self.valor} descrição: {self.descricao}"

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("Erro de pagamento, valor precisa ser maior que 0")
        
    def processar(self):
        self.validar_valor()
        self.resumo()
        self.metodo.processar_pag(self.valor, self.descricao)

class MetodoPix(MetodoPag):
    def __init__(self, chave: str):
        self.chave = chave
    def processar_pag(self, valor):
        print(f"Pagamento realizado para {self.chave}, valor {valor} com pix")

class CartaoCredito(MetodoPag):
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(MetodoPag):
    def __init__(self, chave: str, valor, descricao):
        super().__init__(valor, descricao)

        self.chave: str = chave
        
        def getChave(self):
            return self.chave

    def processar(self):
        if self.valor <= self.limite:
            print("Valor recusado, saldo insuficiente")
            self.limite -= self.valor
        else:
            self.limite -= self.valor
        print("Pagamento realizado para {self.banco} e chave {self.chave}")

class Boleto(MetodoPag):
    def __init__(self, codigo_barras, vencimento: str, valor, descricao):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        self.validar_valor()
        self.resumo()
        self.metodo.processar_pag()
        print(f"Boleto gerado. Aguerdando pagammento...")

def processar_pagamentos(pagamentos: list[MetodoPag]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

pix = MetodoPix("pinheiro@gmail.com")
pag = Pagamento(12.00, "ingresso para cinema", pix)
pag.pagar()
