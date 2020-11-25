import pygame
import random

pygame.init()

pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Falling-Sky')


# ----- Inicia assets

#assets jogador

JOG_WIDTH = 90

JOG_HEIGHT = 70

#assets jogador
jog_img = pygame.image.load('img/kirby parado.png').convert_alpha()
jog_img = pygame.transform.scale(jog_img, (JOG_WIDTH, JOG_HEIGHT))

#assets inimigos

inim_img = pygame.image.load('img/roda da morte.png').convert_alpha()
inim_img = pygame.transform.scale(inim_img, (60, 60))

#assets gemas

gemab_img = pygame.image.load('img/gemas/hab b.png').convert_alpha()
gemay_img = pygame.image.load('img/gemas/hab y.png').convert_alpha()
gemag_img = pygame.image.load('img/gemas/hab g.png').convert_alpha()
t_gemas = [gemab_img, gemay_img, gemag_img]

#assets background

background = pygame.image.load('img/Fundo.png').convert()
background = pygame.transform.scale(background, (700, 620))
background_rect = background.get_rect()

#assets fonte de texto

score_font = pygame.font.Font('font/PressStart2P.ttf', 28)

# Carrega os sons do jogo

pygame.mixer.music.load('snd/Ketsa_-_10_-_wallow.mp3')
pygame.mixer.music.set_volume(0.4)

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



        #Se estiver no ar sprite = kirby no ar

        if self.rect.bottom < HEIGHT-10:
            self.image = pygame.image.load('img/kirby saltando.png').convert_alpha()

        #Se estiver parado = kirby parado

        if self.rect.bottom > HEIGHT-9 and self.speedx==0:
            self.image = pygame.image.load('img/kirby parado.png').convert_alpha()

        #Se estiver correndo para a direita = kirby direita

        if self.speedx > 0:
            self.image = pygame.image.load('img/kirby correndo d.png').convert_alpha()

        #Se estiver correndo para a esquerda = kirby esquerda

        if self.speedx < 0:

            self.image = pygame.image.load('img/kirby correndo e.png').convert_alpha()
        
        self.image = pygame.transform.scale(self.image, (JOG_WIDTH, JOG_HEIGHT))

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
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = WIDTH -100
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.rect.x += 4

        if self.rect.centerx > WIDTH:
            self.rect.centerx = -100

class poder(pygame.sprite.Sprite):

    def __init__(self, gema_img):

    # Construtor da classe mãe (Sprite).

        pygame.sprite.Sprite.__init__(self)

        self.image = gema_img

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(30,670)

        self.rect.centery = random.randint (WIDTH-300,WIDTH-200)

        self.speedx = 0

        self.speedy = 0


game = True
# Variável para o ajuste de velocidade
Tempo = pygame.time.Clock()
FPS = 30
gema = random.choice(t_gemas)
gema_img = pygame.transform.scale(gema, (40,40))

#Cria listas globais com as sprites
all_sprites = pygame.sprite.Group()

# Criando o jogador, inimigo e habilidade

player = jogador(jog_img)

destruidor = inimigo(inim_img)

hab = poder(gema_img)

#Adicionando sprites em uma variável global

all_sprites.add(player)
all_sprites.add(destruidor)

for i in range(5):
    hab = poder(gema_img)
    all_sprites.add(hab)

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while game:
    Tempo.tick(FPS)
    #t += 5

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

                player.image = pygame.image.load('img/kirby parado.png').convert_alpha()
                player.speedx = 0
            

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)
    # Desenhando o score
    text_surface = score_font.render("{​​​​:06d}​​​​".format(PONTOS), True, (255, 0, 200))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (90, 10)
    window.blit(text_surface, text_rect)

    # Desenhando as vidas

    text_surface = score_font.render(chr(9829) * VIDAS, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    window.blit(text_surface, text_rect)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
