from os import path
import pygame
# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 500 # Altura da tela
FPS = 30 # Frames por segundo
GRAVITY = 2
JUMP_SIZE = 25
GROUND = 280

STILL = 0
JUMPING = 1
FALLING = 2
clock = pygame.time.Clock()
# Define tamanhos
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 90
SHOT_WIDTH = 40
SHOT_HEIGHT = 20


def health_bar(surface, x, y, health, max_health, color):
    # Desenha uma barra de vida na tela.
    BAR_LENGTH = 100
    BAR_HEIGHT = 20

    # Calcula a largura da barra de vida proporcional à saúde atual
    barra = (health / max_health) * BAR_LENGTH
    contorno = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    barra_rect = pygame.Rect(x, y, barra, BAR_HEIGHT)

    # Desenha a barra de vida
    pygame.draw.rect(surface, color, barra_rect)
    pygame.draw.rect(surface, (255, 255, 255), contorno, 2)



