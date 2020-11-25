# criando um chao para interagir com o jogador
import pygame 
import random

pygame.init()

#tela
largura = 480
altura = 600

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Falling Sky')

largura_chao = 400
altura_chao = 200

imagem_chao = pygame.image.load("plataforma.png").convert_alpha()
imagem_chao = pygame.transform.scale(imagem_chao, (largura_chao, altura_chao))

background = pygame.image.load("starfield.png").convert()

class Plataforma (pygame.sprite.Sprite):
    def __init__(self,imagem_chao):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = imagem_chao
        self.rect = self.image.get_rect()
        self.rect.y = altura-90
        self.rect.x = largura-450

chao = Plataforma(imagem_chao)
all_sprite = pygame.sprite.Group()
all_sprite.add(chao)
game = True
while game:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    all_sprite.update()
    tela.fill((0,0,0))
    tela.blit(background, (0,0))
    all_sprite.draw(tela)
    pygame.display.update()

pygame.quit()