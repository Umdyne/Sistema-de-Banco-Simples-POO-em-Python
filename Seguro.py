class Seguro_Vida:
    def __init__(self, valor_mensal, valor_total):
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total

    @property
    def valor_mensal(self):
        return self._valor_mensal

    @valor_mensal.setter
    def valor_mensal(self, novo_valor_mensal):
        self._valor_mensal = novo_valor_mensal

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, novo_valor_total):
        self._valor_total = novo_valor_total
