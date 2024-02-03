import pygame


class Paddle:
    VEL = 4
    WIDTH = 20
    HEIGHT = 100
    color = (255, 255, 0)

    def __init__(self, x, y, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
