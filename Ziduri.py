import pygame
from pygame.math import Vector2

class Ziduri:
    # Constructorul
    def __init__(self,cell_number,nivel=1):
        self.cell_number=cell_number
        self.nivel=nivel
        self.ziduri=self.genereaza_ziduri()

    # Functia care genereaza zidurile
    # In functie de valoarea variabilei nivel, se va genera un pattern distinct pentru ziduri
    def genereaza_ziduri(self):
        ziduri=[]

        if self.nivel==1:
            # Ziduri de-a lungul marginilor (lasă spațiu pentru intrare și ieșire)
            for x in range(self.cell_number):
                ziduri.append(Vector2(x,0))  # Sus
                ziduri.append(Vector2(x,self.cell_number-1))  # Jos
            for y in range(1,self.cell_number-1):
                ziduri.append(Vector2(0,y))  # Stânga
                ziduri.append(Vector2(self.cell_number-1,y))  # Dreapta
        elif self.nivel==2:
                # Model pereți sub forma literei "L" în fiecare colț
                for i in range(5):
                    # Colț stânga sus
                    ziduri.append(Vector2(i, 0))
                    ziduri.append(Vector2(0, i))
                    # Colț dreapta sus
                    ziduri.append(Vector2(self.cell_number-1-i,0))
                    ziduri.append(Vector2(self.cell_number-1,i))
                    # Colț stânga jos
                    ziduri.append(Vector2(i,self.cell_number-1))
                    ziduri.append(Vector2(0,self.cell_number-1-i))
                    # Colț dreapta jos
                    ziduri.append(Vector2(self.cell_number-1-i,self.cell_number-1))
                    ziduri.append(Vector2(self.cell_number-1,self.cell_number-1-i))
        elif self.nivel==3:
            # Ziduri în formă de labirint
            for x in range(2,self.cell_number-2):
                ziduri.append(Vector2(x,2))
                ziduri.append(Vector2(x,self.cell_number-3))
            for y in range(4,self.cell_number-4):
                ziduri.append(Vector2(2,y))
                ziduri.append(Vector2(self.cell_number-3,y))
        return ziduri

    def deseneaza_zidurile(self, cell_size, surface):
        culoare_zid=(93,93,93)
        for zid in self.ziduri:
            zid_rect=pygame.Rect(int(zid.x*cell_size),int(zid.y*cell_size),cell_size,cell_size)
            pygame.draw.rect(surface,culoare_zid,zid_rect)

    def este_zid(self,pozitie):
        return pozitie in self.ziduri
