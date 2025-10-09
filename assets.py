import pygame


class Assets:
    def __init__(self):
        self.bg = pygame.image.load("images/bg.png").convert()
        self.icon = pygame.image.load("images/icon.png").convert_alpha()
        
        self.walk_right = [
            pygame.image.load("images/player_right/right1.png").convert_alpha(),
            pygame.image.load("images/player_right/right2.png").convert_alpha(),
            pygame.image.load("images/player_right/right3.png").convert_alpha(),
            pygame.image.load("images/player_right/right4.png").convert_alpha(),
        ]
        
        self.walk_left = [
            pygame.image.load("images/player_left/left1.png").convert_alpha(),
            pygame.image.load("images/player_left/left2.png").convert_alpha(),
            pygame.image.load("images/player_left/left3.png").convert_alpha(),
            pygame.image.load("images/player_left/left4.png").convert_alpha(),
        ]
        
        self.mushroom = pygame.image.load("images/enemy/mushroom.png")
        self.bullet = pygame.image.load("images/bullet.png").convert_alpha()
        
        self.font = pygame.font.Font("fonts/Mont-Bold.ttf", 40)
        self.lose_label = self.font.render("You lost", False, (193, 196, 199))
        self.restart_label = self.font.render("Start new game", False, (0, 255, 0))

