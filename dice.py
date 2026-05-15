import pygame, random

class Dice:
    def __init__(self, x,y):
            self.x = x
            self.y = y
            self.rect = pygame.Rect(self.x, self.y, 80, 80)
            self.value = random.randint(1,6)

    def draw_dice(self, game_window):
        
        dice = pygame.draw.rect(game_window, "white", self.rect)
        return dice

class Dicebutton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 120, 60)

    
    def draw_dice_button(self, game_window):
         
        dice_button = pygame.draw.rect(game_window,"red",self.rect)
        return dice_button
    