import pygame
import sys
import os

# Inicializar pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tela
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha - Perdeu, desligou!")

# Fonte
font = pygame.font.SysFont(None, 80)

# Tabuleiro
board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False

def draw_board():
    screen.fill(WHITE)
    # Linhas verticais
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), LINE_WIDTH)
    # Linhas horizontais
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), LINE_WIDTH)
    
    # Desenha X e O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * 100 + 25, row * 100 + 15))

def check_winner():
    # Linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def shutdown():
    if sys.platform.startswith("win"):
        os.system("shutdown /s /t 1")
    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        os.system("shutdown now")

# Loop principal
running = True
while running:
    draw_board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100

            if board[row][col] == "":
                board[row][col] = player
                winner = check_winner()
                if winner:
                    game_over = True
                    print(f"Jogador {winner} venceu! Desligando o PC...")
                    pygame.time.wait(2000)
                    shutdown()
                else:
                    player = "O" if player == "X" else "X"

pygame.quit()
