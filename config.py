from os import path

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

# Define tamanhos
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 90
SHOT_WIDTH = 40
SHOT_HEIGHT = 20

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
