
import pygame
from config import FPS,WIDTH,HEIGHT,clock
import time
pygame.init()
pygame.mixer.init()
fonte = pygame.font.Font(None, 40)
window = pygame.display.set_mode((WIDTH, HEIGHT))
from assets import assets
from sprites import player,Bullet


all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

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


vida1 = 200
vida2 = 200
wins1 = 0
wins2 = 0
game = True
game_start = False
escolheu_mapa = False
last_shoot = 0
# ===== Loop principal =====
#pygame.mixer.music.play(loops=-1)
image = assets['INICIO']
window.blit(image, (0,0))
while game != 'encerrar':
    
    if game:
        
        # window.blit(image, (0,0))
        #window.blit(assets['INICIO'], (0, 0))
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
                            image = assets['ESCOLHE_MAPA']
                            window.blit(image, (0,0))
                            escolheu_mapa = True
                    else:
                        if event.key == pygame.K_1:
                            image = assets['B_MAPA_1']
                            window.blit(image, (0,0))
                            game_start = True
                            #musica = pygame.mixer.music.load('assets/som/mapa1.mp3')
                            #pygame.mixer.music.play(loops=-1)
                            GROUND = 440
                            p1 = player(assets["P1_D"], 100)
                            p2 = player(assets["P2_E"],700)
                            all_sprites.add(p1)
                            all_sprites.add(p2)

                        if event.key == pygame.K_2:
                            image = assets['B_MAPA_2']
                            window.blit(image, (0,0))
                            game_start = True
                            GROUND = 450

                        if event.key == pygame.K_3:
                            image = assets['B_MAPA_3']
                            window.blit(image, (0,0))
                            game_start = True
                            GROUND = 460

                        if event.key == pygame.K_4:
                            image = assets['B_MAPA_4']
                            window.blit(image, (0,0))
                            game_start = True
                            GROUND = 460

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
                        if current_time - last_shoot > 0.2:
                            new_bullet = Bullet(assets['TIRO_P1_D'], p1)  # Cria um novo tiro
                            all_sprites.add(new_bullet)
                            all_bullets.add(new_bullet)
                            last_shoot = current_time
                        


                        
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
                        if current_time - last_shoot > 0.2:
                            new_bullet = Bullet(assets['TIRO_P2_D'], p2)  # Cria um novo tiro
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

            

            all_sprites.draw(window)

            health_bar(window, 10, 10, vida1, 200, (0, 255, 0))  # Barra de vida do Player 1
            health_bar(window, 690, 10, vida2, 200, (0, 255, 0))  # Barra de vida do Player 2

            placar = fonte.render(f'{wins1} X {wins2}', True, (255, 255, 255))

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
        
        
        clock.tick(FPS)
        # ----- Trata eventos
        all_sprites.empty()
        if vida1 == 0:
            image = assets['VITORIA_P1']
            window.blit(image, (0,0))

        elif vida2 == 0:
            image = assets['VITORIA_P2']
            window.blit(image, (0, 0))

        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = 'encerrar'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    vida1 = 200
                    vida2 = 200
                    
                    game_start = False
                    p1 = player(assets['P1_D'], 100)
                    p2 = player(assets['P2_E'], 700)
                    all_sprites.add(p1)
                    all_sprites.add(p2)
                    GROUND = 280
                    escolheu_mapa = False
                    game = True

        pygame.display.update() 