
import pygame
import sys
from config import FPS,WIDTH,HEIGHT,clock
import time
pygame.init()
pygame.mixer.init()
fonte = pygame.font.Font(None, 40)
window = pygame.display.set_mode((WIDTH, HEIGHT))
from assets import assets 
from sprites import player,Bullet
from config import GROUND, health_bar
from game_logic import gamelogic


all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

vida1 = 200
vida2 = 200
wins1 = 0
wins2 = 0
last_shoot1 = 0
last_shoot2 = 0

instru = False
game = True
game_start = False
escolheu_mapa = False

image = assets["INICIO"]

p1 = player(assets['P1_D'], 100, GROUND)
p2 = player(assets['P2_E'], 700, GROUND)
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)

# ===== Loop principal =====
pygame.mixer.music.load(assets['SND_INICIO'])
pygame.mixer.music.play(loops=-1)

gamelogic()




