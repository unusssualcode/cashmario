import sys
import random
import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, FPS,
    BG_SCROLL_SPEED, BG_WIDTH,
    BULLET_START_COUNT, ENEMY_Y_POSITION,
    MUSHROOM_SPAWN_MIN, MUSHROOM_SPAWN_MAX
)
from assets import Assets
from player import Player
from enemy import Enemy
from bullet import Bullet


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        
        self.assets = Assets()
        pygame.display.set_icon(self.assets.icon)
        
        self.player = Player(self.assets)
        self.enemies = []
        self.bullets = []
        self.bullets_left = BULLET_START_COUNT
        
        self.bg_x = 0
        self.gameplay = True
        self.running = True
        
        self.mushroom_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mushroom_timer, random.randint(MUSHROOM_SPAWN_MIN, MUSHROOM_SPAWN_MAX))
        
        self.restart_label_rect = self.assets.restart_label.get_rect(topleft=(180, 200))
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            if event.type == self.mushroom_timer:
                enemy_rect = self.assets.mushroom.get_rect(topleft=(800, ENEMY_Y_POSITION))
                self.enemies.append(Enemy(enemy_rect))
                
            if (
                self.gameplay
                and event.type == pygame.KEYUP
                and event.key == pygame.K_b
                and self.bullets_left > 0
            ):
                bullet_rect = self.assets.bullet.get_rect(topleft=(self.player.x + 100, self.player.y + 50))
                self.bullets.append(Bullet(bullet_rect))
                self.bullets_left -= 1
                
    def update_gameplay(self):
        keys = pygame.key.get_pressed()
        
        self.player.handle_input(keys)
        self.player.update_animation()
        
        player_rect = self.player.get_rect()
        
        for i in range(len(self.enemies) - 1, -1, -1):
            enemy = self.enemies[i]
            enemy.update()
            
            if enemy.is_off_screen():
                self.enemies.pop(i)
            elif player_rect.colliderect(enemy.rect):
                self.gameplay = False
                
        for i in range(len(self.bullets) - 1, -1, -1):
            bullet = self.bullets[i]
            bullet.update()
            
            if bullet.is_off_screen():
                self.bullets.pop(i)
            else:
                for j in range(len(self.enemies) - 1, -1, -1):
                    if bullet.rect.colliderect(self.enemies[j].rect):
                        self.enemies.pop(j)
                        self.bullets.pop(i)
                        break
                        
        self.bg_x -= BG_SCROLL_SPEED
        if self.bg_x == -BG_WIDTH:
            self.bg_x = 0
            
    def draw_gameplay(self):
        self.screen.blit(self.assets.bg, (self.bg_x, 0))
        self.screen.blit(self.assets.bg, (self.bg_x + BG_WIDTH, 0))
        
        for enemy in self.enemies:
            enemy.draw(self.screen, self.assets.mushroom)
            
        keys = pygame.key.get_pressed()
        self.player.draw(self.screen, keys)
        
        for bullet in self.bullets:
            bullet.draw(self.screen, self.assets.bullet)
            
    def draw_game_over(self):
        self.screen.fill((87, 87, 87))
        self.screen.blit(self.assets.lose_label, (180, 100))
        self.screen.blit(self.assets.restart_label, self.restart_label_rect)
        
        mouse = pygame.mouse.get_pos()
        if self.restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            self.restart_game()
            
    def restart_game(self):
        self.gameplay = True
        self.player.reset()
        self.enemies.clear()
        self.bullets.clear()
        self.bullets_left = BULLET_START_COUNT
        
    def run(self):
        while self.running:
            if self.gameplay:
                self.update_gameplay()
                self.draw_gameplay()
            else:
                self.draw_game_over()
                
            pygame.display.update()
            self.handle_events()
            self.clock.tick(FPS)

