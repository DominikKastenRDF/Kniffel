import pygame

#----------------------------------------------------------------------

#Klasse für den Spielzettel
class Scoresheed:
    def __init__(self, x,y):
            self.x = x
            self.y = y
            self.rect = pygame.Rect(self.x, self.y, 420, 620)

    def draw_scoresheed(self, game_window):
        
        #Weißes Feld für das Scoresheed wird erstellt
        scoresheed_background = pygame.draw.rect(game_window, "white", self.rect)

        #Listen für das Scoresheed
        oberer_teil = ["Eins","Zwei","Drei","Vier","Fünf","Sex","Oberer-Teil ohne Bonus","Bonus","Oberer-Teil mit Bonus"]
        unterer_teil = ["Dreierpasch","Viererpasch","Full House","Kleine Straße","Große Straße","Kniffel","Chance","Unterer-Teil","Gesamtpunkte"]

        #
        #
        #

        return scoresheed_background, oberer_teil, unterer_teil
    
