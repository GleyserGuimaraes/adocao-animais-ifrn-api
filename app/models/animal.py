class Animal:

    def __init__(self, nome, especie, raca, idade, porte, status="Disponível", id=None):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.porte = porte
        self.status = status