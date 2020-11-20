import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Falling-Sky')


# ----- Inicia assets
#TAMANHO DO TRECO CAINDO
#TAMANHO DO TRECO CAINDO
JOG_WIDTH = 90
JOG_HEIGHT = 80
font = pygame.font.SysFont(None, 48) #FONTE DE LETRA UTILIZADA
background = pygame.image.load('img/Fundo.png').convert()
#CODIGO DO TRECO CAINDO
#CODIGO DO TRECO CAINDO
jog_img = pygame.image.load('img/Kirby parado.png').convert_alpha()
jog_img = pygame.transform.scale(jog_img, (JOG_WIDTH, JOG_HEIGHT))
inim_img = pygame.image.load('img/roda da morte.png').convert_alpha()
inim_img = pygame.transform.scale(inim_img, (140, 140))
#poder_img = pygame.image.load().convert_alpha()
#poder_img = pygame.transform.scale(poder_img, (20,20))

 # Redimensiona o fundo   
background = pygame.transform.scale(background, (700, 620))
background_rect = background.get_rect()

# Define a aceleração da gravidade
GRAVITY = 6
# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2

class jogador(pygame.sprite.Sprite):
    def __init__(self, jog_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL
        self.image = jog_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        #Movimentação em y
        self.speedy += GRAVITY
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy

        #Movimentação em x
        self.rect.x += self.speedx
        
        # Corrige a posição para não sair da janela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 4
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            self.state = STILL
            
            
    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 50
            self.state = JUMPING

class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)


        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = WIDTH - 500
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.rect.x += 6

        if self.rect.centerx > WIDTH:
            self.rect.centerx = -100



game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de TRECOS CAINDO
all_sprites = pygame.sprite.Group()
#CODIGO DAS SPRITES DO TRECO CAINDO all_XXX = pygame.sprite.Group()
# Criando o jogador
player = jogador(jog_img)
destruidor = inimigo(inim_img)
#podersinho = poder(poder_img)
all_sprites.add(player)
all_sprites.add(destruidor)
#all_sprites.add(podersinho)
# Criando os TRECOS CAINDO
#for i in range(8):
    #meteor = Meteor(meteor_img)
    #all_sprites.add(meteor)
    #all_meteors.add(meteor)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 9
            if event.key == pygame.K_RIGHT:
                player.speedx += 9
            elif event.key == pygame.K_UP:
                player.jump()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speedx = 0
            

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados