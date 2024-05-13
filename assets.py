import pygame
from config import PLAYER_WIDTH, PLAYER_HEIGHT, SHOT_WIDTH, SHOT_HEIGHT

#SPRITES JOGADORES E TIRO
P1_D = pygame.image.load('assets/img/player1.png').convert_alpha()
P1_D = pygame.transform.scale(P1_D, (PLAYER_WIDTH, PLAYER_HEIGHT))

P2_E = pygame.image.load('assets/img/player2.png').convert_alpha()
P2_E = pygame.transform.scale(P2_E, (PLAYER_WIDTH, PLAYER_HEIGHT))

P1_E = pygame.image.load('assets/img/p1_esquerda.png').convert_alpha()
P1_E = pygame.transform.scale(P1_E, (PLAYER_WIDTH, PLAYER_HEIGHT))

P2_D = pygame.image.load('assets/img/p2_direita.png').convert_alpha()
P2_D = pygame.transform.scale(P2_D, (PLAYER_WIDTH, PLAYER_HEIGHT))

TIRO_P1_D = pygame.image.load('assets/img/tiro1.png').convert_alpha()
TIRO_P1_D = pygame.transform.scale(TIRO_P1_D, (SHOT_WIDTH, SHOT_HEIGHT))

TIRO_P2_E = pygame.image.load('assets/img/tiro2.png').convert_alpha()
TIRO_P2_E = pygame.transform.scale(TIRO_P2_E, (SHOT_WIDTH, SHOT_HEIGHT))

TIRO_P1_E= pygame.image.load('assets/img/tiro1_esquerda.png').convert_alpha()
TIRO_P1_E = pygame.transform.scale(TIRO_P1_E, (SHOT_WIDTH, SHOT_HEIGHT))

TIRO_P2_D= pygame.image.load('assets/img/tiro2_direita.png').convert_alpha()
TIRO_P2_D = pygame.transform.scale(TIRO_P2_D, (SHOT_WIDTH, SHOT_HEIGHT))

#BACKGROUNDS
INICIO = pygame.image.load('assets/img/inicio.png').convert()
ESCOLHE_MAPA = pygame.image.load('assets/img/Escolha_mapas.png').convert()
B_MAPA_1 = pygame.image.load('assets/img/Background_1.jpg').convert()
B_MAPA_2 = pygame.image.load('assets/imgass/Background_2.jpg').convert()
B_MAPA_3 = pygame.image.load('assets/img/Background_3.jpg').convert()
B_MAPA_4 = pygame.image.load('assets/img/Background_4.jpg').convert()
VITORIA_P1 = pygame.image.load('assets/img/vitoria1.png').convert()
VITORIA_P2 = pygame.image.load('assets/img/vitoria2.png').convert()

#MUSICA
SND_INICIO = pygame.mixer.music.load('assets/som/inicio.mp3')
SND_MAPA_1 = pygame.mixer.music.load('assets/som/mapa1.mp3')
SND_MAPA_2 = pygame.mixer.music.load('assets/som/mapa2.mp3')
SND_MAPA_3 = pygame.mixer.music.load('assets/som/mapa3.mp3')
SND_MAPA_4 = pygame.mixer.music.load('assets/som/mapa4.mp3')
SND_FATALITY = pygame.mixer.music.load('assets/som/fatality.mp3')