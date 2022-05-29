import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption('Clicker Game')
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
Bg_surf = pygame.image.load('Images/SpaceBackground.png').convert()
Earth_surf = pygame.image.load('Images/Earth.png').convert()
Earth_surf_rect = Earth_surf.get_rect(center = (250,150))

Cps_Surf = pygame.image.load('Images/Cps.png').convert()
Cps_Surf_rect = Cps_Surf.get_rect(center = (370,350))

game_name = test_font.render('Clicker',False,(255,255,255))
game_name_rect = game_name.get_rect(center = (250,50))

score = 0
Cps = 0
SecondTick = 0

def ScoreFunc():
    global score_text
    global score_text_rect
    score_text = test_font.render(f'Score: {score}',False,(255,255,255))
    score_text_rect = score_text.get_rect(center = (250,250))

def CpsFunc():
    global Cps_text
    global Cps_text_rect
    Cps_text = test_font.render(f'Cps: {Cps}',False,(255,255,255))
    Cps_text_rect = Cps_text.get_rect(topleft = (20,20))


        


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if  Earth_surf_rect.collidepoint(event.pos):
              score += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if  Cps_Surf_rect.collidepoint(event.pos):
              if score >= 50:
                  Cps += 1
                  score = score -  50
              

    screen.blit(Bg_surf,(0,0))
    screen.blit(Earth_surf,Earth_surf_rect)

    screen.blit(game_name,game_name_rect)

    ScoreFunc()
    CpsFunc()

    SecondTick = SecondTick + 1
    if SecondTick >= 60:
        score = score + Cps
        SecondTick = 0

    screen.blit(score_text,score_text_rect)
    screen.blit(Cps_Surf,Cps_Surf_rect)
    screen.blit(Cps_text,Cps_text_rect)

    pygame.display.update()
    clock.tick(60)