import os, pygame, game


# Konsole leeren
os.system("cls")


# Pygame initialisieren
pygame.init()


# Das Fenster und der Hintergrund werden aus game.py aufgerufen
game_window = game.create_window()
background = game.load_background()


# Hier wird das Spiel als Loop ausgegeben
running = True
while running:

    game_window.blit(background, (0, 0))

    # Schließen des Fensters mit X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
