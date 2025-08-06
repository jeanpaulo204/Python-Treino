class ComputadorGamer:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O computador {self.marca} {self.modelo} está ligado!")

pc = ComputadorGamer("Alienware", "M15 R6")
pc.ligar()
# Exemplo: ligar o computador gamer