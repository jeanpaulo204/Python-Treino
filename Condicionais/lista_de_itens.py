# Lista de alimentos que já temos
listaDeAlimentos = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']

# Pede para o usuário digitar um alimento
usuario = input('Digite o nome de um alimento: ').lower()

# Verifica se o alimento está na lista
if usuario in listaDeAlimentos:
    print('✅ Sim! Esse alimento está na lista.')
else:
    print('❌ Não encontramos esse alimento na lista.')
