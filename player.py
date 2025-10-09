import pygame
from config import PLAYER_SPEED, PLAYER_START_X, PLAYER_START_Y


class Player:
    def __init__(self, assets):
        self.assets = assets
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.speed = PLAYER_SPEED
        self.anim_count = 0
        self.is_jumping = False
        self.jump_count = 10
        
    def reset(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.is_jumping = False
        self.jump_count = 10
        
    def get_rect(self):
        return self.assets.walk_left[0].get_rect(topleft=(self.x, self.y))
        
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.x > 50:
            self.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.x < 150:
            self.x += self.speed
            
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                if self.jump_count > 0:
                    self.y -= (self.jump_count**2) / 2
                else:
                    self.y += (self.jump_count**2) / 2
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10
                
    def update_animation(self):
        if self.anim_count == 3:
            self.anim_count = 0
        else:
            self.anim_count += 1
            
    def draw(self, screen, keys):
        if keys[pygame.K_LEFT]:
            screen.blit(self.assets.walk_left[self.anim_count], (self.x, self.y))
        else:
            screen.blit(self.assets.walk_right[self.anim_count], (self.x, self.y))

