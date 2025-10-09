from config import ENEMY_SPEED


class Enemy:
    def __init__(self, rect):
        self.rect = rect
        self.speed = ENEMY_SPEED
        
    def update(self):
        self.rect.x -= self.speed
        
    def is_off_screen(self):
        return self.rect.x < -10
        
    def draw(self, screen, image):
        screen.blit(image, self.rect)

