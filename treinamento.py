import time

team = 'Corinthians'

time_corinthians = [
"Cassio",
"Fagner",
"Caetano",
"Félix Torres",
"Hugo",
"Raniele",
"Maycon",
"Igor Coronado",
"Romero",
"Pedro Raul",
"Wesley",
]


print (f"Escalacao do {team}")
print ("Pensando enquanto o Lider escolhe os Jogadores ....")
time.sleep(5)
print ("Jogadores convocados")
for jogadores in time_corinthians:
    print(f"- {jogadores}")