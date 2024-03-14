import pygame
from sys import exit
from random import randint
# -*- coding: utf-8 -*-

def display_score():
    current_time = round((pygame.time.get_ticks() - start_time)/1000)
    score_surface = score_font.render(f'Score: {current_time}',False, (64,64,64))
    
    score_rect = score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)

    return current_time

    # global recorde
    # if (recorde <= current_time):
    #     recorde = current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(fly_surf,obstacle_rect)
                
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100 ]
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index
    # print(player_index)
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pula Filha!')
clock = pygame.time.Clock()

score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
title_font = pygame.font.Font('font/Pixeltype.ttf', 100)
menu_font = pygame.font.Font('font/Pixeltype.ttf', 70)
recorde_font = pygame.font.Font('font/Pixeltype.ttf', 40)

# guide_font = pygame.font.Font('font/Pixeltype.ttf', 25)
game_active = False
start_time = 0
recorde = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Snail
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index] 

# Fly
fly_frame_1  = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2  = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


# Player
# player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [ player_walk_1 , player_walk_2 ]
player_index = 0
player_jump  = pygame.image.load('graphics/player/jump.png').convert_alpha()


player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0

# intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#title
game_name = menu_font.render('Corre Filha!!',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,60))

game_message = recorde_font.render('Aperte espaco para correr',False,(111,196,169))
game_message_rect = game_message.get_rect(center=(400,340))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

# title_surface = title_font.render(f'Pula Filha', False, ('Green'))
# title_rect = title_surface.get_rect(center=(400,20))


# score_surface = score_font.render("My game", False, (64,64,64) )
# score_rect = score_surface.get_rect(center=(400,50))
# screen.fill('red')



while True:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(pygame.mouse.get_pos()):
                    if player_rect.bottom == 300:
                        player_gravity = -20
                # print(f"Voce clicou na posição :{pygame.mouse.get_pos()}")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
                # keys =  pygame.key.get_pressed()
                        
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),200)))
                else:
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

        
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks() 

        
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('mouse esta sob personagem')
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)

        recorde = display_score()
        # pygame.draw.line(screen,'Black',(0,0),pygame.mouse.get_pos(),10)
        # pygame.draw.ellipse(screen,'Brown',pygame.Rect(150,100,200,100))

        
        # Player
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions (player_rect,obstacle_rect_list)


        # screen.blit(snail_surface,snail_rect)
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # snail_rect.x -= 5 

        # if snail_rect.colliderect(player_rect)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity=0


        screen.blit(game_name,game_name_rect)
        if recorde == 0:
            screen.blit(game_message,game_message_rect)
        else:    
            recorde_message=recorde_font.render(f'Voce sobreviveu por {recorde} segundos!',False,(111,196,169))
            recorde_message_rect=recorde_message.get_rect(center=(400,330))
            screen.blit(recorde_message,recorde_message_rect)


        # display_init_page()
        
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

