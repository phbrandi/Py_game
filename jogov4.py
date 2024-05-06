# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from time import sleep
clock = pygame.time.Clock()
FPS = 30

pygame.init()

# ----- Gera tela principal
WIDTH = 800
HEIGHT = 500

GRAVITY = 2
JUMP_SIZE = 25
GROUND = 363

STILL = 0
JUMPING = 1
FALLING = 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('assets/img/Background_1.jpg').convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

p1_img = pygame.image.load('assets/img/player1.png').convert_alpha()
p1_img = pygame.transform.scale(p1_img, (50, 70))

p2_img = pygame.image.load('assets/img/player2.png').convert_alpha()
p2_img = pygame.transform.scale(p2_img, (50, 70))

class player1(pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
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

class player2(pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
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



p1 = player1(p1_img)
p2 = player2(p2_img)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                p1.speedx -= 8
            if event.key == pygame.K_d:
                p1.speedx += 8
            if event.key == pygame.K_w:
                p1.jump()

            if event.key == pygame.K_LEFT:
                p2.speedx -= 8
            if event.key == pygame.K_RIGHT:
                p2.speedx += 8
            if event.key == pygame.K_UP:
                p2.jump()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                p1.speedx += 8
            if event.key == pygame.K_d:
                p1.speedx -= 8

            if event.key == pygame.K_LEFT:
                p2.speedx += 8
            if event.key == pygame.K_RIGHT:
                p2.speedx -= 8

    all_sprites.update()

    window.blit(image, (0, 0))

    all_sprites.draw(window)
    #window.blit(p1_img, (100, 295))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
