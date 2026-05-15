import pygame

class Dice:
    def __init__(self, x,y):
            self.x = x
            self.y = y
            self.rect = pygame.Rect(self.x, self.y, 80, 80)

    def draw_dice(self, game_window):
        
        dice = pygame.draw.rect(game_window, "white", self.rect)
        return dice

