import pygame  

pygame.init()


largura = 500
altura = 600

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("destiny trivial")


game = True
# fonte = pygame.font.SysFont(None,24) 
# text = fonte.render("Ordem e Progresso", True,(255,255,255))
image = pygame.image.load("mario.jpg").convert()
image = pygame.transform.scale(image, (110,70))
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    tela.fill((0,0,0))
    tela.blit(image, (10,10))

    # tela.fill((0,255,0)) #tem que estar dentro do for para rodar 
    # cor = (255,255,0)
    # cor2 = (0,0,255)
    # vertices = [(250,0),(500,200),(250,400), (0,200)]
    # centro = (250,200)
    # raio = 100
    # pygame.draw.polygon(tela,cor,vertices)
    # pygame.draw.circle(tela,cor2,centro,raio)
    # tela.blit(text, (170,185))
    
    pygame.display.update()

pygame.quit()

