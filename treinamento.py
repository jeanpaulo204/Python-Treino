import time
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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

# Mostra no terminal
print(f"Escalação do {team}")
print("Pensando enquanto o Líder escolhe os Jogadores ....")
time.sleep(3)
print("Jogadores convocados")
for jogador in time_corinthians:
    print(f"- {jogador}")

# Gera o PDF
pdf_nome = "escalacao_corinthians.pdf"
c = canvas.Canvas(pdf_nome, pagesize=A4)

# Título
c.setFont("Helvetica-Bold", 20)
c.drawString(200, 800, f"Escalação do {team}")

# Subtítulo
c.setFont("Helvetica", 14)
c.drawString(50, 770, "Jogadores convocados:")

# Lista de jogadores
y = 740
for jogador in time_corinthians:
    c.drawString(70, y, f"- {jogador}")
    y -= 20  # Espaço entre os nomes

# Salva o PDF
c.save()
print(f"\n✅ PDF '{pdf_nome}' gerado com sucesso!")
