import pygame
clock = pygame.time.Clock()
import time
from config import WIDTH,HEIGHT,FPS
from assets import INICIO,ESCOLHE_MAPA,B_MAPA_1,B_MAPA_2,B_MAPA_3,B_MAPA_4,VITORIA_P1,VITORIA_P2, SND_INICIO,SND_MAPA_1,SND_MAPA_2,SND_MAPA_3,SND_MAPA_4,SND_FATALITY
from assets import P1_D,P1_E,P2_D,P2_E,TIRO_P1_D,TIRO_P1_E,TIRO_P2_D,TIRO_P2_E

from classes import Player, Bullet

p1 = Player(P1_D, 100)
p2 = Player(P2_E, 700)
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)
fonte = pygame.font.Font(None, 40)
vida1 = 200
vida2 = 200
wins1 = 0
wins2 = 0

last_shoot = 0
# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
def game_logic(window):
    while game != 'encerrar':
        if game:
            window.blit(image, (0, 0))
            clock.tick(FPS)
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = 'encerrar'
                    

                if event.type == pygame.KEYDOWN:
                    if game_start == False:
                        if escolheu_mapa == False:
                            if event.key == pygame.K_RETURN:
                                image = pygame.image.load('assets/img/Escolha_mapas.png')
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                window.blit(image, (0,0))
                                escolheu_mapa = True
                        else:
                            if event.key == pygame.K_1:
                                image = pygame.image.load('assets/img/Background_1.jpg').convert()
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                window.blit(image, (0,0))
                                game_start = True
                                musica = pygame.mixer.music.load('assets/som/mapa1.mp3')
                                pygame.mixer.music.play(loops=-1)
                                GROUND = 440
                            if event.key == pygame.K_2:
                                image = pygame.image.load('assets/img/Background_2.jpg').convert()
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                window.blit(image, (0,0))
                                game_start = True
                                musica = pygame.mixer.music.load('assets/som/mapa2.mp3')
                                pygame.mixer.music.play(loops=-1)
                                GROUND = 450
                            if event.key == pygame.K_3:
                                image = pygame.image.load('assets/img/Background_3.jpg').convert()
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                window.blit(image, (0,0))
                                game_start = True
                                musica = pygame.mixer.music.load('assets/som/mapa3.mp3')
                                pygame.mixer.music.set_volume(1.0)
                                pygame.mixer.music.play(loops=-1)
                                GROUND = 460
                            if event.key == pygame.K_4:
                                image = pygame.image.load('assets/img/Background_4.jpg').convert()
                                image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                                window.blit(image, (0,0))
                                game_start = True
                                musica = pygame.mixer.music.load('assets/som/mapa4.mp3')
                                pygame.mixer.music.play(loops=-1)
                                GROUND = 460

                    else:
                        if event.key == pygame.K_a:
                            p1.speedx -= 8
                            p1.image = P1_E
                        if event.key == pygame.K_d:
                            p1.speedx += 8
                            p1.image = P1_D
                        if event.key == pygame.K_w:
                            p1.jump()
                        if event.key == pygame.K_SPACE:
                            current_time = time.time()
                            if current_time - last_shoot > 0.2:
                                new_bullet = Bullet(TIRO_P1_D, p1)  # Cria um novo tiro
                                all_sprites.add(new_bullet)
                                all_bullets.add(new_bullet)
                                last_shoot = current_time
                            


                            
                        if event.key == pygame.K_LEFT:
                            p2.speedx -= 8
                            p2.image = P2_E
                        if event.key == pygame.K_RIGHT:
                            p2.speedx += 8
                            p2.image = P2_D
                        if event.key == pygame.K_UP:
                            p2.jump()
                        if event.key == pygame.K_p:
                            current_time = time.time()
                            if current_time - last_shoot > 0.2:
                                new_bullet = Bullet(TIRO_P2_E, p2)  # Cria um novo tiro
                                all_sprites.add(new_bullet)
                                all_bullets.add(new_bullet)
                                last_shoot = current_time

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        p1.speedx += 8
                    if event.key == pygame.K_d:
                        p1.speedx -= 8

                    if event.key == pygame.K_LEFT:
                        p2.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        p2.speedx -= 8
            if game_start == True:

                # Detecta colisões entre os tiros e os jogadores
                hits1 = pygame.sprite.spritecollide(p2, all_bullets, True)
                if hits1:
                    if vida2 != 0:
                        vida2 -= 5

                hits2 = pygame.sprite.spritecollide(p1, all_bullets, True)
                if hits2:
                    if vida1 != 0:
                        vida1 -= 5

                all_sprites.update()

                window.blit(image, (0, 0))

                all_sprites.draw(window)

                texto_vida1 = fonte.render(f'Player 1: {vida1}', True, (255, 255, 255), (0, 0, 0))
                texto_vida2 = fonte.render(f'Player 2: {vida2}', True, (255, 255, 255), (0, 0, 0))

                placar = fonte.render(f'{wins1} X {wins2}', True, (255, 255, 255))

                window.blit(texto_vida1, (10, 10))
                window.blit(texto_vida2, (618, 10))

                window.blit(placar, (WIDTH / 2 - 25, 10))

                if vida1 == 0 or vida2 == 0:
                    if vida1 == 0:
                        wins2 += 1
                    if vida2 == 0:
                        wins1 += 1
                    
                    musica = pygame.mixer.music.load('assets/som/fatality.mp3')
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play()
                    game = False
            
            pygame.display.update()  # Mostra o novo frame para o jogador

        if game == False:
            window.blit(image, (0, 0))
            clock.tick(FPS)
            # ----- Trata eventos
            all_sprites.empty()
            if vida1 == 0:
                image = pygame.image.load('assets/img/vitoria2.png').convert_alpha()
                image = pygame.transform.scale(image, (WIDTH, HEIGHT))

            elif vida2 == 0:
                image = pygame.image.load('assets/img/vitoria1.png').convert_alpha()
                image = pygame.transform.scale(image, (WIDTH, HEIGHT))

            for event in pygame.event.get():
            # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = 'encerrar'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        vida1 = 200
                        vida2 = 200
                        image = pygame.image.load('assets/img/inicio.png').convert_alpha()
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        game_start = False
                        p1 = Player(P1_D, 100)
                        p2 = Player(P2_E, 700)
                        all_sprites.add(p1)
                        all_sprites.add(p2)
                        GROUND = 280
                        musica = pygame.mixer.music.load('assets/som/inicio.mp3')
                        pygame.mixer.music.set_volume(0.4)
                        pygame.mixer.music.play(loops=-1)
                        escolheu_mapa = False
                        game = True

            pygame.display.update() 