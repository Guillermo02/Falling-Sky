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
imagem_meteoro = pygame.image.load('meteoro.png').convert_alpha()
imagem_meteoro = pygame.transform.scale(imagem_meteoro, (largura_meteoro, altura_meteoro))

largura_nave = 50
altura_nave = 50
imagem_nave = pygame.image.load("playerShip1_orange.png").convert_alpha()
imagem_nave = pygame.transform.scale(imagem_nave, (largura_nave, altura_nave))

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,img):

        pygame.sprite.Sprite.__init__(self)

        self.imagem_meteoro = img
        self.rect = self.imagem_meteoro.get_rect()
        self.rect.x = random.randint(0,largura-largura_meteoro)
        self.rect.y = random.randint(-100,-altura_meteoro)
        self.velocidadex = random.randint(-3,3)
        self.velocidadey = random.randint(2,9)
    
    def update(self):
        #atualizando a posicao do meteoro
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0,largura-largura_meteoro)
            self.rect.y = random.randint(-100,-altura_meteoro)
            self.velocidadex = random.randint(-3,3)
            self.velocidadey = random.randint(2,9)
            

class nave(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        
        self.imagem_nave = img
        self.rect = self.imagem_nave.get_rect()

        self.rect.centerx = largura/2
        self.rect.bottom = altura - 10


# Meteor assets
game = True
clock = pygame.time.Clock()
fps = 30

varios_meteoros = pygame.sprite.Group()

for i in range(8):
    meteoro = Meteoro(imagem_meteoro)
    varios_meteoros.add(meteoro)

while game:
    clock.tick(fps)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    
    #atualiza meteoros
    
    varios_meteoros.update()
        

    #Gera saidas(imagens)

    tela.fill((0,0,0))
    tela.blit(background, (0,0))
    
    varios_meteoros.draw(tela)
    pygame.display.update()

pygame.quit()