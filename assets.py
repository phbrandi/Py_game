import pygame
import os
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, SHOT_WIDTH, SHOT_HEIGHT

pygame.init()
pygame.mixer.init()

# Define o diretório de imagens
IMG_DIR = 'assets/img/'

# SPRITES JOGADORES E TIRO
P1_D = 'player1.png'
P2_E = 'player2.png'
P1_E = 'p1_esquerda.png'
P2_D = 'p2_direita.png'
TIRO_P1_D = 'tiro1.png'
TIRO_P2_E = 'tiro2.png'
TIRO_P1_E = 'tiro1_esquerda.png'
TIRO_P2_D = 'tiro2_direita.png'

# BACKGROUNDS
INICIO = 'inicio.jpg'
ESCOLHE_MAPA = 'Escolha_mapas.jpg'
INSTRUCOES = 'instrucoes.jpg'
B_MAPA_1 = 'Background_1.jpg'
B_MAPA_2 = 'Background_2.jpg'
B_MAPA_3 = 'Background_3.jpg'
B_MAPA_4 = 'Background_4.jpg'
VITORIA_P1 = 'vitoria1.jpg'
VITORIA_P2 = 'vitoria2.jpg'

#SONS


assets = {}

# Carregar e transformar os ativos
INICIO = pygame.image.load(os.path.join(IMG_DIR, 'inicio.png')).convert_alpha()
INICIO = pygame.transform.scale(INICIO, (WIDTH, HEIGHT))
assets["INICIO"] = INICIO

ESCOLHE_MAPA = pygame.image.load(os.path.join(IMG_DIR, 'Escolha_mapas.png')).convert()
ESCOLHE_MAPA = pygame.transform.scale(ESCOLHE_MAPA, (WIDTH, HEIGHT))
assets["ESCOLHE_MAPA"] = ESCOLHE_MAPA

INSTRUCOES = pygame.image.load(os.path.join(IMG_DIR, 'instrucoes.png')).convert()
INSTRUCOES = pygame.transform.scale(INSTRUCOES, (WIDTH, HEIGHT))
assets["INSTRUCOES"] = INSTRUCOES

B_MAPA_1 = pygame.image.load(os.path.join(IMG_DIR, 'Background_1.jpg')).convert()
B_MAPA_1 = pygame.transform.scale(B_MAPA_1, (WIDTH, HEIGHT))
assets["B_MAPA_1"] = B_MAPA_1

B_MAPA_2 = pygame.image.load(os.path.join(IMG_DIR, 'Background_2.jpg')).convert()
B_MAPA_2 = pygame.transform.scale(B_MAPA_2, (WIDTH, HEIGHT))
assets["B_MAPA_2"] = B_MAPA_2

B_MAPA_3 = pygame.image.load(os.path.join(IMG_DIR, 'Background_3.jpg')).convert()
B_MAPA_3 = pygame.transform.scale(B_MAPA_3, (WIDTH, HEIGHT))
assets["B_MAPA_3"] = B_MAPA_3

B_MAPA_4 = pygame.image.load(os.path.join(IMG_DIR, 'Background_4.jpg')).convert()
B_MAPA_4 = pygame.transform.scale(B_MAPA_4, (WIDTH, HEIGHT))
assets["B_MAPA_4"] = B_MAPA_4

VITORIA_P1 = pygame.image.load(os.path.join(IMG_DIR, 'vitoria1.png')).convert()
VITORIA_P1 = pygame.transform.scale(VITORIA_P1, (WIDTH, HEIGHT))
assets["VITORIA_P1"] = VITORIA_P1

VITORIA_P2 = pygame.image.load(os.path.join(IMG_DIR, 'vitoria2.png')).convert()
VITORIA_P2 = pygame.transform.scale(VITORIA_P2, (WIDTH, HEIGHT))
assets["VITORIA_P2"] = VITORIA_P2

P1_D = pygame.image.load(os.path.join(IMG_DIR, 'player1.png')).convert_alpha()
P1_D = pygame.transform.scale(P1_D, (PLAYER_WIDTH, PLAYER_HEIGHT))
assets["P1_D"] = P1_D

P1_E = pygame.image.load(os.path.join(IMG_DIR, 'p1_esquerda.png')).convert_alpha()
P1_E = pygame.transform.scale(P1_E, (PLAYER_WIDTH, PLAYER_HEIGHT))
assets["P1_E"] = P1_E

P2_E = pygame.image.load(os.path.join(IMG_DIR, 'player2.png')).convert_alpha()
P2_E = pygame.transform.scale(P2_E, (PLAYER_WIDTH, PLAYER_HEIGHT))
assets["P2_E"] = P2_E

P2_D = pygame.image.load(os.path.join(IMG_DIR, 'p2_direita.png')).convert_alpha()
P2_D = pygame.transform.scale(P2_D, (PLAYER_WIDTH, PLAYER_HEIGHT))
assets["P2_D"] = P2_D

TIRO_P1_D = pygame.image.load(os.path.join(IMG_DIR, 'tiro1.png')).convert_alpha()
TIRO_P1_D = pygame.transform.scale(TIRO_P1_D, (SHOT_WIDTH, SHOT_HEIGHT))
assets["TIRO_P1_D"] = TIRO_P1_D

TIRO_P1_E = pygame.image.load(os.path.join(IMG_DIR, 'tiro1_esquerda.png')).convert_alpha()
TIRO_P1_E = pygame.transform.scale(TIRO_P1_E, (SHOT_WIDTH, SHOT_HEIGHT))
assets["TIRO_P1_E"] = TIRO_P1_E

TIRO_P2_E = pygame.image.load(os.path.join(IMG_DIR, 'tiro2.png')).convert_alpha()
TIRO_P2_E = pygame.transform.scale(TIRO_P2_E, (SHOT_WIDTH, SHOT_HEIGHT))
assets["TIRO_P2_E"] = TIRO_P2_E

TIRO_P2_D = pygame.image.load(os.path.join(IMG_DIR, 'tiro2_direita.png')).convert_alpha()
TIRO_P2_D = pygame.transform.scale(TIRO_P2_D, (SHOT_WIDTH, SHOT_HEIGHT))
assets["TIRO_P2_D"] = TIRO_P2_D

assets['SND_INICIO'] = 'assets/som/inicio.mp3'

assets['SND_MAPA_1'] = 'assets/som/mapa1.mp3'

assets['SND_MAPA_2'] = 'assets/som/mapa2.mp3'

assets['SND_MAPA_3'] = 'assets/som/mapa3.mp3'

assets['SND_MAPA_4'] = 'assets/som/mapa4.mp3'

assets['FATALITY'] = 'assets/som/fatality.mp3'


