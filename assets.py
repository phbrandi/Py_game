import pygame
import os
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, SHOT_WIDTH, SHOT_HEIGHT, IMG_DIR, SND_DIR

#SPRITES JOGADORES E TIRO
P1_D = 'player1.png'
P2_E = 'player2.png'
P1_E = 'p1_esquerda.png'
P2_D = 'p2_direita.png'
TIRO_P1_D = 'tiro1.png'
TIRO_P2_E = 'tiro2.png'
TIRO_P1_E= 'tiro1_esquerda.png'
TIRO_P2_D= 'tiro2_direita.png'

#BACKGROUNDS
INICIO = 'inicio.jpg'
ESCOLHE_MAPA = 'Escolha_mapas.jpg'
INSTRUCOES = 'instrucoes.jpg'
B_MAPA_1 = 'Background_1.jpg'
B_MAPA_2 = 'Background_2.jpg'
B_MAPA_3 = 'Background_3.jpg'
B_MAPA_4 = 'Background_4.jpg'
VITORIA_P1 = 'vitoria1.jpg'
VITORIA_P2 = 'vitoria2.jpg'

#AUDIOS
SND_INICIO = 'inicio.mp3'
SND_MAPA_1 = 'mapa1.mp3'
SND_MAPA_2 = 'mapa2.mp3'
SND_MAPA_3 = 'mapa3.mp3'
SND_MAPA_4 = 'mapa4.mp3'
SND_FATALITY = 'fatality.mp3'

assets = {}
assets[INICIO] = pygame.image.load(os.path.join(IMG_DIR, INICIO)).convert()
assets[INICIO] = pygame.transform.scale(assets[INICIO], (WIDTH, HEIGHT))

assets[B_MAPA_1] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_1)).convert()
assets[B_MAPA_1] = pygame.transform.scale(assets[B_MAPA_1], (WIDTH, HEIGHT))

assets[B_MAPA_2] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_2)).convert()
assets[B_MAPA_2] = pygame.transform.scale(assets[B_MAPA_2], (WIDTH, HEIGHT))

assets[B_MAPA_3] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_3)).convert()
assets[B_MAPA_3] = pygame.transform.scale(assets[B_MAPA_3], (WIDTH, HEIGHT))

assets[B_MAPA_4] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_4)).convert()
assets[B_MAPA_4] = pygame.transform.scale(assets[B_MAPA_4], (WIDTH, HEIGHT))

assets[VITORIA_P1] = pygame.image.load(os.path.join(IMG_DIR, VITORIA_P1)).convert()
assets[VITORIA_P1] = pygame.transform.scale(assets[VITORIA_P1], (WIDTH, HEIGHT))

assets[VITORIA_P2] = pygame.image.load(os.path.join(IMG_DIR, VITORIA_P2)).convert()
assets[VITORIA_P2] = pygame.transform.scale(assets[VITORIA_P2], (WIDTH, HEIGHT))

assets[P1_D] = pygame.image.load(os.path.join(IMG_DIR, P1_D)).convert()
assets[P1_D] = pygame.transform.scale(assets[P1_D], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[P1_E] = pygame.image.load(os.path.join(IMG_DIR, P1_E)).convert_alpha()
assets[P1_E] = pygame.transform.scale(assets[P1_E], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[P2_E] = pygame.image.load(os.path.join(IMG_DIR, P2_E)).convert_alpha()
assets[P2_E] = pygame.transform.scale(assets[P2_E], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[P2_D] = pygame.image.load(os.path.join(IMG_DIR, P2_D)).convert_alpha()
assets[P2_D] = pygame.transform.scale(assets[P2_D], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[TIRO_P1_D] = pygame.image.load(os.path.join(IMG_DIR, TIRO_P1_D)).convert_alpha()
assets[TIRO_P1_D] = pygame.transform.scale(assets[TIRO_P1_D], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[TIRO_P1_E] = pygame.image.load(os.path.join(IMG_DIR, TIRO_P1_E)).convert_alpha()
assets[TIRO_P1_E] = pygame.transform.scale(assets[TIRO_P1_E], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[TIRO_P2_E] = pygame.image.load(os.path.join(IMG_DIR, TIRO_P2_E)).convert_alpha()
assets[TIRO_P2_E] = pygame.transform.scale(assets[TIRO_P2_E], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[TIRO_P2_D] = pygame.image.load(os.path.join(IMG_DIR, TIRO_P2_D)).convert_alpha()
assets[TIRO_P2_D] = pygame.transform.scale(assets[TIRO_P2_D], (PLAYER_WIDTH, PLAYER_HEIGHT))

assets[INICIO] = pygame.image.load(os.path.join(IMG_DIR, INICIO)).convert()
assets[INICIO] = pygame.transform.scale(assets[INICIO], (WIDTH, HEIGHT))

assets[INSTRUCOES] = pygame.image.load(os.path.join(IMG_DIR, INSTRUCOES)).convert()
assets[INSTRUCOES] = pygame.transform.scale(assets[INSTRUCOES], (WIDTH, HEIGHT))

assets[ESCOLHE_MAPA] = pygame.image.load(os.path.join(IMG_DIR, ESCOLHE_MAPA)).convert()
assets[ESCOLHE_MAPA] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[B_MAPA_1] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_1)).convert()
assets[B_MAPA_1] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[B_MAPA_2] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_2)).convert()
assets[B_MAPA_2] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[B_MAPA_3] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_3)).convert()
assets[B_MAPA_3] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[B_MAPA_4] = pygame.image.load(os.path.join(IMG_DIR, B_MAPA_4)).convert()
assets[B_MAPA_4] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[VITORIA_P1] = pygame.image.load(os.path.join(IMG_DIR, VITORIA_P1)).convert()
assets[VITORIA_P1] = pygame.transform.scale(assets[ESCOLHE_MAPA], (WIDTH, HEIGHT))

assets[VITORIA_P2] = pygame.image.load(os.path.join(IMG_DIR, VITORIA_P2)).convert()
assets[VITORIA_P2] = pygame.transform.scale(assets[VITORIA_P2], (WIDTH, HEIGHT))