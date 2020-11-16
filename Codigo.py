import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')


# ----- Inicia assets
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/starfield.png').convert()
meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
meteor_img = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))
jog_img = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
jog_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))



# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados