import pygame


class Player_List:
    # Liste mit Spielern
    def player_list():
        players = []


# Spielfenster wird festgelegt
def create_window():
    window = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("AMIGO-FLUSH")  
    return window


# Hintergrundbild laden
def load_background():
    return pygame.transform.scale(pygame.image.load("wood.png"), (1200, 700))
