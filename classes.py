import pygame
from config import GROUND, WIDTH, GRAVITY, FALLING, STILL, JUMP_SIZE, JUMPING
from assets import P1_D,P1_E,P2_D,P2_E,TIRO_P1_D,TIRO_P1_E,TIRO_P2_D,TIRO_P2_E

class Player(pygame.sprite.Sprite):
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
    
        if player == P1:
            if player.image == P1_D:
                self.rect.centerx = player.rect.x + 80
                self.rect.centery = player.rect.y + 55
                self.speedx = 10  # Velocidade do tiro
                self.image = TIRO_P1_D
            if player.image == P1_E:
                self.rect.centerx = player.rect.x - 20
                self.rect.centery = player.rect.y + 55
                self.speedx = -10  # Velocidade do tiro
                self.image = TIRO_P1_E

        if player == P2:
            if player.image == P2_E:
                self.rect.centerx = player.rect.x - 20
                self.rect.centery = player.rect.y + 55
                self.speedx = -10  # Velocidade do tiro
                self.image = TIRO_P2_E
            if player.image == P2_D:
                self.rect.centerx = player.rect.x + 80
                self.rect.centery = player.rect.y + 55
                self.speedx = 10  # Velocidade do tiro
                self.image = TIRO_P2_D

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill() 