import pygame
veld_grootte = 20
kleur_slang = (0,255,0)
class Snake:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.lijst_slang = [[startx, starty]]
        self.lengte_slang = 1  # len(self.lijst_slang)
        self.x_verandering = 0
        self.y_verandering =  0

    def beweeg(self):
        self.x += self.x_verandering
        self.y += self.y_verandering
        slang_kop = [self.x, self.y]
        self.lijst_slang.append(slang_kop)
        if len(self.lijst_slang) > self.lengte_slang:
            del self.lijst_slang[0]
    def teken(self, venster):
        for segment in self.lijst_slang:
            pygame.draw.rect(venster, kleur_slang, pygame.Rect(
                segment[0], segment[1], veld_grootte, veld_grootte
            ))
    def is_buiten_veld(self, breedte, hoogte):

    def raakt_zichzelf(self):