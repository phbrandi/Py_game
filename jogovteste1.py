# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH,HEIGHT
from events import game_logic

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DESSOFT FIGHTERS')
fonte = pygame.font.Font(None, 40)

# ----- Inicia estruturas de dados

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
game_logic(window)