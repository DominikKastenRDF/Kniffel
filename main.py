import os,pygame,game,dice,scoresheed

#----------------------------------------------------------------------

# Konsole leeren
os.system("cls")

#----------------------------------------------------------------------

# Pygame initialisieren
pygame.init()

#----------------------------------------------------------------------

# Das Fenster und der Hintergrund werden aus game.py aufgerufen
game_window = game.create_window()
background = game.load_background()

#Dice wird initalisiert
dice_1 = dice.Dice(1000, 100)
dice_2 = dice.Dice(1000, 200)
dice_3 = dice.Dice(1000, 300)
dice_4 = dice.Dice(1000, 400)
dice_5 = dice.Dice(1000, 500)

#Button zum Würfeln wird initalisiert
dice_button = dice.Dicebutton(980, 600)

#Scoresheed wird initalisiert
scoresheed = scoresheed.Scoresheed(50, 50)

#----------------------------------------------------------------------

# Hier wird das Spiel als Loop ausgegeben
running = True
while running:

    #Hintergrundbild für Fenster
    game_window.blit(background, (0, 0))

    #Dices werden angezeigt
    dice_1.draw_dice(game_window)
    dice_2.draw_dice(game_window)
    dice_3.draw_dice(game_window)
    dice_4.draw_dice(game_window)
    dice_5.draw_dice(game_window)


    #Scoresheed wird angezeigt
    scoresheed.draw_scoresheed(game_window)
    
    #Dicebutton wird angezeigt
    dice_button.draw_dice_button(game_window)



    # Schließen des Fensters mit X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()

pygame.quit()
