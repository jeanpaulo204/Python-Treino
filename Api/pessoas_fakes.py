import requests

# URL da API
url = "https://randomuser.me/api/?results=1"

# Fazendo a requisição GET
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converte JSON para dicionário Python

    # Acessando os dados do usuário
    user = data['results'][0]
    nome = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    cidade = user['location']['city']
    pais = user['location']['country']
    foto = user['picture']['large']

    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Localização: {cidade}, {pais}")
    print(f"Foto: {foto}")

else:
    print(f"Erro ao acessar API: {response.status_code}")
