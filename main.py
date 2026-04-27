import os, pygame, game

#Konsole leeren
os.system("cls")


#Aufruf Window aus game.py
game_window = game.create_window()


#Hier wird das Spiel als Loop ausgegeben
running = True
while running:

    #Schließen mit dem Fenster X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    #Updatet das Window
    pygame.display.update()


pygame.quit()
