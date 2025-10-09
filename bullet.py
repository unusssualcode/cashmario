from config import BULLET_SPEED


class Bullet:
    def __init__(self, rect):
        self.rect = rect
        self.speed = BULLET_SPEED
        
    def update(self):
        self.rect.x += self.speed
        
    def is_off_screen(self):
        return self.rect.x > 820
        
    def draw(self, screen, image):
        screen.blit(image, (self.rect.x, self.rect.y))

