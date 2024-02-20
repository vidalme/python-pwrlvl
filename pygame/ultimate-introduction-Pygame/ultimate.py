import pygame
from sys import exit
# -*- coding: utf-8 -*-

def display_score():
    current_time = round((pygame.time.get_ticks() - start_time)/1000)
    score_surface = score_font.render(f'Score: {current_time}',False, (64,64,64))
    
    score_rect = score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)

    global recorde
    if (recorde <= current_time):
        recorde = current_time


def display_init_page():
    title_surface = title_font.render(f'Pula Filha!', False, (111,196,169))
    title_rect = title_surface.get_rect(center=(400,70))
    global recorde
    recorde_surface  = recorde_font.render(f'melhor score [ {recorde} ]',False,(55,77,96))
    recorde_rect = recorde_surface.get_rect(center=(400, 300))

    menu_surface = menu_font.render(f'[ espaco ] inicia jogo      [ S ] sai do jogo',False,'Black')
    menu_rect = menu_surface.get_rect(center=(400,355))

    guide_surface = guide_font.render(f'Aperte espaco ou clique com o mouse no personagem para pular e desviar dos inimigos.', False, (55,77,96))
    guide_rect = guide_surface.get_rect(center=(400,380))

    screen.blit(title_surface, title_rect)
    screen.blit(recorde_surface,recorde_rect)
    screen.blit(guide_surface, guide_rect)
    screen.blit(menu_surface, menu_rect)
    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pula Filha!')
clock = pygame.time.Clock()

score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
title_font = pygame.font.Font('font/Pixeltype.ttf', 100)
recorde_font = pygame.font.Font('font/Pixeltype.ttf', 50)
menu_font = pygame.font.Font('font/Pixeltype.ttf', 35)
guide_font = pygame.font.Font('font/Pixeltype.ttf', 25)

game_active = False
start_time = 0
recorde = 0


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_y_pos = 300
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos,snail_y_pos))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#title 
title_surface = title_font.render(f'Runner', False, ('Green'))
title_rect = title_surface.get_rect(center=(400,20))


# score_surface = score_font.render("My game", False, (64,64,64) )
# score_rect = score_surface.get_rect(center=(400,50))
#screen.fill('red')



while True:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Voce clicou na posição :{pygame.mouse.get_pos()}")
                if player_rect.collidepoint(pygame.mouse.get_pos()):
                    if player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                keys =  pygame.key.get_pressed()
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.x = 600
                    start_time = pygame.time.get_ticks() 

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('mouse esta sob personagem')
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)

        display_score()

        # pygame.draw.line(screen,'Black',(0,0),pygame.mouse.get_pos(),10)
        # pygame.draw.ellipse(screen,'Brown',pygame.Rect(150,100,200,100))

        screen.blit(snail_surface,snail_rect)
        
        # Player
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface,player_rect)


        if snail_rect.right <= 0:
            snail_rect.left = 800
        snail_rect.x -= 4 

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        display_init_page()
        
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # elif keys[pygame.K_a]:
    #     print('go left')
    # elif keys[pygame.K_d]:
    #     print('go right')

    # print(f'esta a {player_rect.left} da esquerda')
    # print(f'esta a {player_rect.right} da direita')
    # player_rect.right +=1

    # if player_rect.colliderect(snail_rec):
    #    print('tocou')
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)

