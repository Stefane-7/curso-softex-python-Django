class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome    