import pygame
import random
#import Kirbys   ##Possibilidade de kerbys extras

pygame.init()
pygame.mixer.init()   ##MUSICA

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Falling-Sky')


# ----- Inicia assets
##Os nomes das variáveis está em uma mistura de português e inglês##
#assets jogador
JOG_WIDTH = 90
JOG_HEIGHT = 70
jog_img = pygame.image.load('img/kirby parado.png').convert_alpha()
jog_img = pygame.transform.scale(jog_img, (JOG_WIDTH, JOG_HEIGHT))
#assets inimigo
inim_img = pygame.image.load('img/roda da morte.png').convert_alpha()
inim_img = pygame.transform.scale(inim_img, (70, 70))
#assets gemas
gemab_img = pygame.image.load('img/gemas/hab b.png').convert_alpha()
gemay_img = pygame.image.load('img/gemas/hab y.png').convert_alpha()
gemag_img = pygame.image.load('img/gemas/hab g.png').convert_alpha()
t_gemas = [gemab_img, gemay_img, gemag_img]
#assets meteoros
chao_img = pygame.image.load("img/plataforma.png").convert_alpha()
chao_img = pygame.transform.scale(chao_img, (710, 200))
#assets meteoro
meteoro_img = pygame.image.load('img/meteorodragon.png').convert_alpha()
meteoro_img = pygame.transform.scale(meteoro_img, (80, 80))
#assets background
background = pygame.image.load('img/Fundo.png').convert()
background = pygame.transform.scale(background, (700, 620))
background_rect = background.get_rect()
#assets fonte de texto
score_font = pygame.font.Font('font/PressStart2P.ttf', 28)

# Carrega os sons do jogo
musica   = pygame.mixer.music.load('snd/Musica de fundo.mp3')
#item_som = pygame.mixer.Sound('snd/item.flac')
#dano_som = pygame.mixer.Sound('snd/dano.flac')
#pulo_som = pygame.mixer.Sound('snd/pulo.flac')
#pygame.mixer.music.set_volume(0.2)

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1

# Define valores iniciais
GRAVITY = 6
PONTOS = 0
VIDAS = 3

class jogador(pygame.sprite.Sprite):
    def __init__(self, jog_img, VIDAS):
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
        self.lifes = VIDAS
    
    def update(self):

        #Movimentação em y

        self.speedy += GRAVITY
        #Atualiza a posição y
        self.rect.y += self.speedy
        #Atualiza a posição x
        self.rect.x += self.speedx

        ## Mudança de sprite para cada situação que estiver ##
        #Se estiver no ar: kirby no ar
        if self.rect.bottom < HEIGHT-10:
            self.image = pygame.image.load('img/kirby saltando.png').convert_alpha()
            #pulo_som.play()  ###AUDIO DE PULO
        #Se estiver parado: kirby parado
        if self.rect.bottom > HEIGHT-9 and self.speedx==0:
            self.image = pygame.image.load('img/kirby parado.png').convert_alpha()
        #Se estiver correndo para a direita: kirby direita
        if self.speedx > 0:
            self.image = pygame.image.load('img/kirby correndo d.png').convert_alpha()
        #Se estiver correndo para a esquerda: kirby esquerda
        if self.speedx < 0:
            self.image = pygame.image.load('img/kirby correndo e.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (JOG_WIDTH, JOG_HEIGHT))

        #Se jogador colidiu com algum inimigo
        collisions = pygame.sprite.spritecollide(self, collide_destruidor, False)
        collisions2 = pygame.sprite.spritecollide(self, collide_meteoros, False)
        #Perde uma vida
        for collision in collisions:
            self.lifes -= 1
        for collision in collisions2:
            self.lifes -= 1
        
        #Corrige a posição para não sair da janela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 4
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            self.state = STILL

    #Método que faz o personagem pular
    def jump(self):
        #Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 50
            self.state = JUMPING       

class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = WIDTH - 120
        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        self.rect.x += 4
        if self.rect.left > WIDTH:
            self.rect.right = -100

class poder(pygame.sprite.Sprite):
    def __init__(self, gema_img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = gema_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(30,670)
        self.rect.centery = random.randint (WIDTH-300,WIDTH-200)
        self.speedx = 0 
        self.speedy = 0   

class Plataforma (pygame.sprite.Sprite):
    def __init__(self,chao_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = chao_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = HEIGHT-10

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,meteoro_img):

        pygame.sprite.Sprite.__init__(self)

        self.image = meteoro_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-50)
        self.rect.y = random.randint(-100,-38)
        self.velocidadex = random.randint(-3,3)
        self.velocidadey = random.randint(2,3)
    
    def update(self):
        #atualizando a posicao do meteoro
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0,WIDTH-50)
            self.rect.y = random.randint(-100,-38)
            self.velocidadex = random.randint(-3,3)
            self.velocidadey = random.randint(2,3)

game = True
#Cria um relógio que conta o tempo em jogo
tempo = pygame.time.Clock()
FPS = 30
gema = random.choice(t_gemas)
gema_img = pygame.transform.scale(gema, (40,40))

#Gemas aleatórias que aparecem
gema = random.choice(t_gemas)
gema_img = pygame.transform.scale(gema, (40,40))

#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
collide_destruidor = pygame.sprite.Group()
collide_gema = pygame.sprite.Group()
collide_meteoros = pygame.sprite.Group()
# Criando o jogador, inimigo e gemas
player = jogador(jog_img, VIDAS)
destruidor = inimigo(inim_img)
gema_ponto = poder(gema_img)
chao = Plataforma(chao_img)
#Adicionando sprites em uma variável global
all_sprites.add(player)
all_sprites.add(destruidor)
all_sprites.add(chao)
collide_destruidor.add(destruidor)
for i in range(5):
    gema_ponto = poder(gema_img)
    all_sprites.add(gema_ponto)
    collide_gema.add(gema_ponto)
for i in range(5):
    meteoro = Meteoro(meteoro_img)
    all_sprites.add(meteoro)
    collide_meteoros.add(meteoro)


# ===== Loop principal =====
pygame.mixer.music.play(loops=-1) ##MUSICA
while game:
    if VIDAS > 0:
        tempo.tick(FPS)
        
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
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.image = pygame.image.load('img/kirby parado.png').convert_alpha()
                    player.speedx = 0
        
        hits = pygame.sprite.spritecollide(player, collide_destruidor, True, pygame.sprite.collide_mask)
        hits2 = pygame.sprite.spritecollide(player, collide_meteoros, True, pygame.sprite.collide_mask)
        if len(hits) > 0 or len(hits2)>0:
            VIDAS -= 1
            destruidor.rect.x = -200
            all_sprites.add(destruidor)
            all_sprites.add(meteoro)
            collide_destruidor.add(destruidor)
            collide_meteoros.add(meteoro)
        contato = pygame.sprite.spritecollide(player, collide_gema, True)
        
        #Pontos 
        if len(contato)>0:
            if gema == gemay_img or gema == gemag_img:
                PONTOS += 10
            elif gema == gemab_img:
                PONTOS += 15
        
        for gema in contato:
            gema = random.choice(t_gemas)
            gema_img = pygame.transform.scale(gema, (40,40))
            gema_ponto = poder(gema_img)
            all_sprites.add(gema_ponto)
            collide_gema.add(gema_ponto)

        if PONTOS % 100 == 0 and VIDAS<3:
            VIDAS += 1
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()
        collide_destruidor.update()
        collide_gema.update()
        collide_meteoros.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background, (0, 0))
        # Desenhando as sprites
        all_sprites.draw(window)
        
        # Desenhando o score
        text_surface = score_font.render("{:06d}".format(PONTOS), True, (255, 0, 200))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (90,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = score_font.render(chr(9829) * VIDAS, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)


    
    else:
        window.fill((0, 0, 0))
        text_surface = score_font.render("Que pena vc perdeu", True, (255, 0, 0))
        text_surface2 = score_font.render("Você tem {0} pontos".format(PONTOS), True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text2_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH/2, (HEIGHT/2)-100)
        text2_rect.midtop = (WIDTH/2, (HEIGHT/2)+50)
        window.blit(text_surface, text_rect)
        window.blit(text_surface2, text2_rect)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                game = False
    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados