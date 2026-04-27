import pygame


#Spielfenster wird festgelegt
def create_window():
    window = pygame.display.set_mode((1100, 650))
    pygame.display.set_caption("AMIGO-FLUSH")
    window.fill((100,100,200))
    return window

