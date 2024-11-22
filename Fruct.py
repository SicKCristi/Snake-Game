import pygame
import random
from pygame.math import Vector2

class Fruct:
    # Constructorul pentru clasa Fruct
    def __init__(self,cell_number):
        self.randomizare(cell_number)

    # Functia prin care desenam pe o suprafata data fructul
    # Trebuie sa inmultim si cu cell_size pentru a obtine adevarata pozitie pe tabla
    # Pentru ca folosim Vector2, ele sunt by default float, asa ca trebuie sa le convertim explicit la int
    def deseneaza_fructul(self, cell_size, surface,Mar):
        fruct_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size), cell_size, cell_size)
        # Nu mai desenam un rectagle, desenam portocala data ca parametru
        # pygame.draw.rect(surface, (126, 166, 144), fruct_rect)
        surface.blit(Mar,fruct_rect)

    # Initial acesta a fost constructorul, dar acum codul este in aceasta functie
    # Poate fi folosita apoi si in constructor pentru a genera pozitii random pentru fruct
    def randomizare(self,cell_number):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
