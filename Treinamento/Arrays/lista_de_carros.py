carros = ["Gol", "Onix", "Civic", "Corolla", "Uno", "Hilux", "HB20", "Toro", "Argo", "T-Cross"]

# Exemplo: mostrar todos os carros
for carro in carros:
    print(carro)


carros.append("Compass")      # Adiciona um carro ao final
carros.remove("Uno")          # Remove um carro específico
print(carros[0])              # Mostra o primeiro carro
print(len(carros))            # Quantos carros tem na lista
