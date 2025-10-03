from re import A
import sys
import random
import pygame


clock = pygame.time.Clock()

pygame.init()

"""
Screen size init
"""
screen = pygame.display.set_mode((800, 600)) #flags=pygame.NOFRAME
pygame.display.set_caption("CASHMARIO") #game name
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)


bg = pygame.image.load('images/bg.png').convert()


walk_right = [
    pygame.image.load('images/player_right/right1.png').convert_alpha(),
    pygame.image.load('images/player_right/right2.png').convert_alpha(),
    pygame.image.load('images/player_right/right3.png').convert_alpha(),
    pygame.image.load('images/player_right/right4.png').convert_alpha()
]

walk_left = [
    pygame.image.load('images/player_left/left1.png').convert_alpha(),
    pygame.image.load('images/player_left/left2.png').convert_alpha(),
    pygame.image.load('images/player_left/left3.png').convert_alpha(),
    pygame.image.load('images/player_left/left4.png').convert_alpha()
]

mushroom = pygame.image.load('images/enemy/mushroom.png')
mushroom_list_in_game = []

player_anim_count = 0
bg_x = 0


player_speed = 5
player_x = 150
player_y = 320

is_jumping = False
jump_count = 10

mushroom_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(mushroom_timer, 1000)
pygame.time.set_timer(mushroom_timer, random.randint(1000, 5000))

label = pygame.font.Font("fonts/Mont-Bold.ttf", 40)
lose_label = label.render("You lost", False, (193, 196, 199))
restart_label = label.render("Start new game", False, (0, 255, 0))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

gameplay = True

"""
Screen show game
"""
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        # mushroom_rect = mushroom.get_rect(topleft=(mushroom_x, 320))
        
        if mushroom_list_in_game:
            for (i,el) in enumerate(mushroom_list_in_game):
                screen.blit(mushroom, el)
                el.x -= 10
                
                if el.x < -10:
                    mushroom_list_in_game.pop(i)
        
                if player_rect.colliderect(el):
                    gameplay = False
        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        
        
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 150:
            player_x += player_speed
            
            
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
                
            else:
                is_jumping = False
                jump_count = 10

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -800:
            bg_x = 0
    else:
        screen.fill((87, 87, 87))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay=True
            player_x = 150
            mushroom_list_in_game.clear()
    
    pygame.display.update()
    """
    Correct finishing project
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        if event.type == mushroom_timer:
            mushroom_list_in_game.append(mushroom.get_rect(topleft=(800, 350)))
            

    clock.tick(10)