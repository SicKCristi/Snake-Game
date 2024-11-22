from Fruct import Fruct
from Sarpe import Sarpe
import pygame
import sys

class Main:
    # Constructorul
    def __init__(self,cell_number):
        self.sarpe=Sarpe()
        self.fruct=Fruct(cell_number)
        self.scor=0

    # Conditia de mutare a sarpelui se muta aici
    def update(self,cell_number):
        self.sarpe.muta_sarpele()
        self.a_ajuns_sarpele_la_fruct(cell_number)
        self.final(cell_number)

    # Elementele desenate initial in main se vor desena aici
    def deseneaza_elementele(self,cell_number,cell_size,canvas,Mar,font):
        self.deseneaza_gazonul(canvas,cell_number,cell_size)
        self.fruct.deseneaza_fructul(cell_size,canvas,Mar)
        self.sarpe.deseneaza_sarpele(cell_size,canvas)
        self.deseneaza_scorul(font,canvas,cell_number,cell_size,Mar)

    # Functie care verifica daca capul sarpelui este identic cu pozitia fructului
    # Daca sarpele a ajuns la fruct, acesta trebuie sa dispara din prima locatie si sa se repozitioneze
    # Si de asemenea, la sarpe se mai adauga un bloc la final
    def a_ajuns_sarpele_la_fruct(self,cell_number):
        if self.fruct.pos==self.sarpe.body[0]:
            self.fruct.randomizare(cell_number)
            self.sarpe.adauga_block()
            self.scor+=1
            self.sarpe.adauga_sunetul()

        # In cazul in care un fruct se genereaza intr-o celula cu corpul sarpelui sa se genereze din nou
        for block in self.sarpe.body[1:]:
            if block==self.fruct.pos:
                self.fruct.randomizare()

    # Verifica daca s-a indeplinit una dintre conditiile de oprire
    # 1. Sarpele s-a lovit de el insusi
    # 2. Sarpele s-a lovit de un perete al jocului
    def final(self,cell_number):
        for block in self.sarpe.body[1:]:
            if(self.sarpe.body[0]==block):
                self.game_over()
        if not 0<=self.sarpe.body[0].x<cell_number or not 0<=self.sarpe.body[0].y<cell_number:
            self.game_over()

    # Cand se apeleaza aceasta functie, jocul s-a sfarsit
    def game_over(self):
        self.sarpe.resetare()

    # Metoda prin care vom desena un "pattern" pentru gazon
    def deseneaza_gazonul(self,canvas,cell_number,cell_size):
        culoare_iarba=(167,209,61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row+col)%2:
                    rectangle_iarba=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                    pygame.draw.rect(canvas,culoare_iarba,rectangle_iarba)

    # Functia care va desena scorul in fereastra de joc
    def deseneaza_scorul(self,font,screen,cell_number,cell_size,Mar):
        text_pt_scor=str(len(self.sarpe.body)-3)
        suprafata_scor=font.render(text_pt_scor,True,(56,74,12))
        scor_x=int(cell_size*cell_number-60)
        scor_y=int(cell_size*cell_number-40)
        rectagle_pt_scor=suprafata_scor.get_rect(center=(scor_x,scor_y))
        Mar_rectangle=Mar.get_rect(midright=(rectagle_pt_scor.left,rectagle_pt_scor.centery))
        bg_rectangle=pygame.Rect(Mar_rectangle.left,Mar_rectangle.top,Mar_rectangle.width+rectagle_pt_scor.width+7,Mar_rectangle.height)

        pygame.draw.rect(screen,(167,209,61),bg_rectangle)
        screen.blit(suprafata_scor,rectagle_pt_scor)
        screen.blit(Mar,Mar_rectangle)
        pygame.draw.rect(screen, (56,74,12), bg_rectangle,2)





