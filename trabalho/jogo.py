import pygame  
import random


pygame.init()

#tela
largura = 480
altura = 600

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Falling Sky')

largura_meteoro = 50
altura_meteoro = 38
font = pygame.font.SysFont(None,48)
background = pygame.image.load("starfield.png").convert()
imagem_meteoro = pygame.image.load('meteorodragon.png').convert_alpha()
imagem_meteoro = pygame.transform.scale(imagem_meteoro, (largura_meteoro, altura_meteoro))

largura_chao = 480
altura_chao = 100

imagem_chao = pygame.image.load("plataforma.png").convert_alpha()
imagem_chao = pygame.transform.scale(imagem_chao, (largura_chao, altura_chao))

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,imagem_meteoro):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem_meteoro
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,largura-largura_meteoro)
        self.rect.y = random.randint(-100,-altura_meteoro)
        self.velocidadex = random.randint(0,3)
        self.velocidadey = random.randint(2,6)
    
    def update(self):
        #atualizando a posicao do meteoro
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0,largura-largura_meteoro)
            self.rect.y = random.randint(-100,-altura_meteoro)
            self.velocidadex = random.randint(0,3)
            self.velocidadey = random.randint(2,6)
            

class Plataforma (pygame.sprite.Sprite):
    def __init__(self,imagem_chao):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = imagem_chao
        self.rect = self.image.get_rect()
        self.rect.y = altura-30
        self.rect.x = largura-480

chao = Plataforma(imagem_chao)
all_sprite = pygame.sprite.Group()
all_sprite.add(chao)
all_sprite.add()
varios_meteoros = pygame.sprite.Group()
# Meteor assets
game = True
clock = pygame.time.Clock()
fps = 30


for i in range(4):
    meteoro = Meteoro(imagem_meteoro)
    varios_meteoros.add(meteoro)
    all_sprite.add(meteoro)

while game:
    clock.tick(fps)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    
    #atualiza meteoros
    
    all_sprite.update()
    colisao = pygame.sprite.spritecollide(chao, varios_meteoros, True)
    
    for colide in colisao:
        meteoro = Meteoro(imagem_meteoro)
        varios_meteoros.add(meteoro)
        all_sprite.add(meteoro)
    #Gera saidas(imagens)

    tela.fill((0,0,0))
    tela.blit(background, (0,0))
    
    
    all_sprite.draw(tela)
    pygame.display.update()

pygame.quit()