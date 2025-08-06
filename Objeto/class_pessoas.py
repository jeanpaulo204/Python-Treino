class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Eu sou {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("João", 20)
p2 = Pessoa("Maria", 25)

p1.apresentar()
p2.apresentar()
