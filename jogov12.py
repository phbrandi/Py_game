# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from time import sleep
import time
clock = pygame.time.Clock()
FPS = 30

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 800
HEIGHT = 500

GRAVITY = 2
JUMP_SIZE = 25
GROUND = 280

STILL = 0
JUMPING = 1
FALLING = 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIROTEIO')
fonte = pygame.font.Font(None, 40)

# ----- Inicia estruturas de dados
game = True
game_start = False
wait = False


# ----- Inicia assets 

p1_img = pygame.image.load('assets/img/player1.png').convert_alpha()
p1_img = pygame.transform.scale(p1_img, (60, 90))

p2_img = pygame.image.load('assets/img/player2.png').convert_alpha()
p2_img = pygame.transform.scale(p2_img, (60, 90))

p1_e = pygame.image.load('assets/img/p1_esquerda.png').convert_alpha()
p1_e = pygame.transform.scale(p1_e, (60, 90))

p2_d = pygame.image.load('assets/img/p2_direita.png').convert_alpha()
p2_d = pygame.transform.scale(p2_d, (60, 90))

tiro_p1_img = pygame.image.load('assets/img/tiro1.png').convert_alpha()
tiro_p1_img = pygame.transform.scale(tiro_p1_img, (40, 20))

tiro_p2_img = pygame.image.load('assets/img/tiro2.png').convert_alpha()
tiro_p2_img = pygame.transform.scale(tiro_p2_img, (40, 20))

tiro_p1_e= pygame.image.load('assets/img/tiro1_esquerda.png').convert_alpha()
tiro_p1_e = pygame.transform.scale(tiro_p1_e, (40, 20))

tiro_p2_d= pygame.image.load('assets/img/tiro2_direita.png').convert_alpha()
tiro_p2_d = pygame.transform.scale(tiro_p2_d, (40, 20))

image = pygame.image.load('assets/img/inicio.png').convert_alpha()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

pygame.mixer.music.load('assets/som/Wave Saver - 8-bit Sheriff (Royalty Free Music).mp3')
pygame.mixer.music.set_volume(0.4)

class player(pygame.sprite.Sprite):
    def __init__(self, img, pos):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.orig_image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = pos
        self.rect.bottom = GROUND
        self.speedx = 0
        self.speedy = 0

    def update(self):

        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.speedy += GRAVITY
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy

        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, player):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
    
        if player == p1:
            if player.image == p1_img:
                self.rect.centerx = player.rect.x + 80
                self.rect.centery = player.rect.y + 55
                self.speedx = 10  # Velocidade do tiro
                self.image = tiro_p1_img
            if player.image == p1_e:
                self.rect.centerx = player.rect.x - 20
                self.rect.centery = player.rect.y + 55
                self.speedx = -10  # Velocidade do tiro
                self.image = tiro_p1_e

        if player == p2:
            if player.image == p2_img:
                self.rect.centerx = player.rect.x - 20
                self.rect.centery = player.rect.y + 55
                self.speedx = -10  # Velocidade do tiro
                self.image = tiro_p2_img
            if player.image == p2_d:
                self.rect.centerx = player.rect.x + 80
                self.rect.centery = player.rect.y + 55
                self.speedx = 10  # Velocidade do tiro
                self.image = tiro_p2_d

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill() 
                
p1 = player(p1_img, 100)
p2 = player(p2_img, 700)
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)

vida1 = 200
vida2 = 200

last_shoot = 0
# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
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
                    if event.key == pygame.K_RETURN:
                        image = pygame.image.load('assets/img/Escolha_mapas.png')
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        window.blit(image, (0,0))
                    if event.key == pygame.K_1:
                        image = pygame.image.load('assets/img/Background_1.jpg').convert()
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        window.blit(image, (0,0))
                        game_start = True
                        GROUND = 440
                    if event.key == pygame.K_2:
                        image = pygame.image.load('assets/img/Background_2.jpg').convert()
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        window.blit(image, (0,0))
                        game_start = True
                        GROUND = 450
                    if event.key == pygame.K_3:
                        image = pygame.image.load('assets/img/Background_3.jpg').convert()
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        window.blit(image, (0,0))
                        game_start = True
                        GROUND = 460
                    if event.key == pygame.K_4:
                        image = pygame.image.load('assets/img/Background_4.jpg').convert()
                        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                        window.blit(image, (0,0))
                        game_start = True
                        GROUND = 460

                else:
                    if event.key == pygame.K_a:
                        p1.speedx -= 8
                        p1.image = p1_e
                    if event.key == pygame.K_d:
                        p1.speedx += 8
                        p1.image = p1_img
                    if event.key == pygame.K_w:
                        p1.jump()
                    if event.key == pygame.K_SPACE:
                        current_time = time.time()
                        if current_time - last_shoot > 0.2:
                            new_bullet = Bullet(tiro_p1_img, p1)  # Cria um novo tiro
                            all_sprites.add(new_bullet)
                            all_bullets.add(new_bullet)
                            last_shoot = current_time
                        


                        
                    if event.key == pygame.K_LEFT:
                        p2.speedx -= 8
                        p2.image = p2_img
                    if event.key == pygame.K_RIGHT:
                        p2.speedx += 8
                        p2.image = p2_d
                    if event.key == pygame.K_UP:
                        p2.jump()
                    if event.key == pygame.K_p:
                        current_time = time.time()
                        if current_time - last_shoot > 0.2:
                            new_bullet = Bullet(tiro_p2_img, p2)  # Cria um novo tiro
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

            window.blit(texto_vida1, (10, 10))
            window.blit(texto_vida2, (618, 10))

            if vida1 == 0 or vida2 == 0:
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    vida1 = 200
                    vida2 = 200
                    image = pygame.image.load('assets/img/inicio.png').convert_alpha()
                    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
                    game_start = False
                    p1 = player(p1_img, 100)
                    p2 = player(p2_img, 700)
                    all_sprites.add(p1)
                    all_sprites.add(p2)
                    GROUND = 280
                    game = True

        pygame.display.update() 