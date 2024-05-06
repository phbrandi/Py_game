# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('assets/img/Background_1.jpg').convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

p1 = pygame.image.load('assets/img/player1.png').convert_alpha()
p1 = pygame.transform.scale(p1, (50, 70))

p2 = pygame.image.load('assets/img/player2.png').convert_alpha()
p2 = pygame.transform.scale(p2, (50, 70))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    window.blit(image, (0, 0))
    window.blit(p1, (100, 295))
    window.blit(p2, (650, 295))



    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
