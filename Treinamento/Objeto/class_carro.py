class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def buzinar(self):
        print("Bibi! Bibi!")

    def mostrar_info(self):
        print(f"Carro: {self.marca} {self.modelo}, Cor: {self.cor}, Ano: {self.ano}")

# Criando um objeto carro:
meu_carro = Carro("Ford", "Mustang", "Vermelho", 2022)

# Usando os métodos:
meu_carro.mostrar_info()  # Mostra as informações
meu_carro.buzinar()       # Faz o som da buzina
