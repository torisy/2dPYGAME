import pygame

class Character:

    def __init__(self, x, y):
        self.x = 10
        self.y = 10
        self.speed = 2
        self.visible = True

    def move(self, keys):
        self.prev_x, self.prev_y = self.x, self.y
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))
