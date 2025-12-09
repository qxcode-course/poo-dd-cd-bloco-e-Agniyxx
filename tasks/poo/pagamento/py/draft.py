from abc import ABC, abstractmethod

class MetodoPag(ABC):
    @abstractmethod
    def processar_pag(self, valor: float, descricao: str):
        pass

# valha fiquei gag

class Pagamento:
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self):
        return f" Pagamento de R$ {self.valor}: {self.descricao}"

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("fail: valor inválido")
        
    def processar(self):
        self.validar_valor()
        self.resumo()
        self.metodo.processar_pag() 

class CartaoCredito(Pagamento):
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

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

class Pix(Pagamento):
    def __init__(self, chave: str, banco: str, valor, descricao):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        if self.valor <= self.limite:
            print("Valor recusado, saldo insuficiente")
            self.limite -= self.valor
        else:
            self.limite -= self.valor
        print("Pagamento realizado para {self.banco} e chave {self.chave}")

class Boleto(Pagamento):
    def __init__(self, codigo_barras, vencimento: str, valor, descricao):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        self.validar_valor()
        self.resumo()
        self.metodo.processar_pag()

Metodo = 