from os import path
import pygame
# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 500 # Altura da tela
FPS = 30 # Frames por segundo
GRAVITY = 2
JUMP_SIZE = 25

STILL = 0
JUMPING = 1
FALLING = 2
clock = pygame.time.Clock()
# Define tamanhos
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 90
SHOT_WIDTH = 40
SHOT_HEIGHT = 20



