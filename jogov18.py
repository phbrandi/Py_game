import pygame
import sys
from config import FPS, WIDTH, HEIGHT, clock
import time
pygame.init()
pygame.mixer.init()
fonte = pygame.font.Font(None, 40)
window = pygame.display.set_mode((WIDTH, HEIGHT))
from assets import assets 
from sprites import player, Bullet
from config import GROUND, health_bar

def escolhe_mapa(tecla):
    global image, game_start, GROUND    
    
    mapas = {
        pygame.K_1: ['B_MAPA_1', 'SND_MAPA_1', 440, 0.8],
        pygame.K_2: ['B_MAPA_2', 'SND_MAPA_2', 450, 1.0],
        pygame.K_3: ['B_MAPA_3', 'SND_MAPA_3', 460, 1.0],
        pygame.K_4: ['B_MAPA_4', 'SND_MAPA_4', 460, 1.0]
    }
    
    if tecla in mapas:
        mapa = mapas[tecla][0]
        som = mapas[tecla][1]
        ground = mapas[tecla][2]
        volume = mapas[tecla][3]

        image = assets[mapa]

        game_start = True
        tocar_musica(som,volume,True)
        GROUND = ground

def tocar_musica(arquivo, volume,loops):
    pygame.mixer.music.load(assets[arquivo])
    pygame.mixer.music.set_volume(volume)
    if loops:
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.play()
        
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
all_sprites.add(p1, p2)

tocar_musica('SND_INICIO', 0.8, True)

while game != 'encerrar':
    if game:
        window.blit(image, (0, 0))
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = 'encerrar'
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if game_start == False:
                    if instru == False:
                        if event.key == pygame.K_RETURN:
                            image = assets['INSTRUCOES']
                            instru = True
                    elif escolheu_mapa == False:
                        if event.key == pygame.K_RETURN:
                            image = assets['ESCOLHE_MAPA']
                            escolheu_mapa = True
                    else:
                        escolhe_mapa(event.key)
                else:
                    if event.key == pygame.K_a:
                        p1.speedx -= 8
                        p1.image = assets['P1_E']
                    if event.key == pygame.K_d:
                        p1.speedx += 8
                        p1.image = assets['P1_D']
                    if event.key == pygame.K_w:
                        p1.jump()
                    if event.key == pygame.K_SPACE:
                        current_time = time.time()
                        if current_time - last_shoot1 > 0.2:
                            new_bullet = Bullet(assets["TIRO_P1_D"], p1)
                            all_sprites.add(new_bullet)
                            all_bullets.add(new_bullet)
                            last_shoot1 = current_time
                    if event.key == pygame.K_LEFT:
                        p2.speedx -= 8
                        p2.image = assets['P2_E']
                    if event.key == pygame.K_RIGHT:
                        p2.speedx += 8
                        p2.image = assets['P2_D']
                    if event.key == pygame.K_UP:
                        p2.jump()
                    if event.key == pygame.K_p:
                        current_time = time.time()
                        if current_time - last_shoot2 > 0.2:
                            new_bullet = Bullet(assets["TIRO_P2_E"], p2)
                            all_sprites.add(new_bullet)
                            all_bullets.add(new_bullet)
                            last_shoot2 = current_time
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    p1.speedx += 8
                if event.key == pygame.K_d:
                    p1.speedx -= 8
                if event.key == pygame.K_LEFT:
                    p2.speedx += 8
                if event.key == pygame.K_RIGHT:
                    p2.speedx -= 8
        
        if game_start:
            hits1 = pygame.sprite.spritecollide(p2, all_bullets, True)
            if hits1 and vida2 > 0:
                vida2 -= 5

            hits2 = pygame.sprite.spritecollide(p1, all_bullets, True)
            if hits2 and vida1 > 0:
                vida1 -= 5

            all_sprites.update()
            all_sprites.draw(window)

            health_bar(window, 10, 10, vida1, 200, (0, 255, 0))
            health_bar(window, 690, 10, vida2, 200, (0, 255, 0))
            placar = fonte.render(f'{wins1} X {wins2}', True, (255, 255, 255))
            window.blit(placar, (WIDTH / 2 - 25, 10))

            if vida1 == 0 or vida2 == 0:
                if vida1 == 0:
                    wins2 += 1
                if vida2 == 0:
                    wins1 += 1
                
                tocar_musica('FATALITY', 0.8, False)
                game = False
        
        pygame.display.update()
    
    if not game:
        clock.tick(FPS)
        all_sprites.empty()
        image = assets['VITORIA_P2'] if vida1 == 0 else assets['VITORIA_P1']
        window.blit(image, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                vida1 = vida2 = 200
                image = assets['INICIO']
                game_start = escolheu_mapa = False
                GROUND = 280
                p1 = player(assets['P1_D'], 100, GROUND)
                p2 = player(assets['P2_E'], 700, GROUND)
                all_sprites.add(p1, p2)
                tocar_musica('SND_INICIO', 0.4, True)
                game = True
        
        pygame.display.update()