import pygame;
import random;
from pygame.math import Vector2

class Sarpe:
    # Constructorul pentru clasa Sarpe
    # Initial, sarpele va fi compus din 3 elemente unul langa celalalt
    def __init__(self,):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.directie=Vector2(0,0)
        self.new_block=False

        # Grafica pentru capul sarpelui
        self.head_up=pygame.image.load('Imagini/head_up.png').convert_alpha()
        self.head_down=pygame.image.load('Imagini/head_down.png').convert_alpha()
        self.head_right=pygame.image.load('Imagini/head_right.png').convert_alpha()
        self.head_left=pygame.image.load('Imagini/head_left.png').convert_alpha()

        # Grafica pentru coada sarpelui
        self.tail_up=pygame.image.load('Imagini/tail_up.png').convert_alpha()
        self.tail_down=pygame.image.load('Imagini/tail_down.png').convert_alpha()
        self.tail_right=pygame.image.load('Imagini/tail_right.png').convert_alpha()
        self.tail_left=pygame.image.load('Imagini/tail_left.png').convert_alpha()

        # Grafica pentru pozitia corpului sarpelui (vertical sau orizontal)
        self.body_vertical=pygame.image.load('Imagini/body_vertical.png').convert_alpha()
        self.body_horizontal=pygame.image.load('Imagini/body_horizontal.png').convert_alpha()

        # Grafica pentru pozitiile unde corpul sarpelui este curbat
        self.body_tr=pygame.image.load('Imagini/body_tr.png').convert_alpha()
        self.body_tl=pygame.image.load('Imagini/body_tl.png').convert_alpha()
        self.body_br=pygame.image.load('Imagini/body_br.png').convert_alpha()
        self.body_bl=pygame.image.load('Imagini/body_bl.png').convert_alpha()

        # Adaugam un sunet pentru momentul in care sarpele mananca un fruct
        self.sunet_mancat=pygame.mixer.Sound('Sunete/crunch.wav')

    # Functia care va afisa sarpele pe canvas
    def deseneaza_sarpele(self,cell_size,canvas):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos=int(block.x*cell_size)
            y_pos=int(block.y*cell_size)
            block_rect=pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index==0:
                canvas.blit(self.head,block_rect)
            elif index==len(self.body)-1:
                canvas.blit(self.tail,block_rect)
            else:
                previous_block=self.body[index+1]-block
                next_block=self.body[index-1]-block
                if previous_block.x==next_block.x:
                    canvas.blit(self.body_vertical,block_rect)
                elif previous_block.y==next_block.y:
                    canvas.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                        canvas.blit(self.body_tl,block_rect)
                    elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                        canvas.blit(self.body_bl,block_rect)
                    elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                        canvas.blit(self.body_tr,block_rect)
                    elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                        canvas.blit(self.body_br,block_rect)

    # Functia care actualizeaza pozitia capului
    # Se va face difernta dintre primele doua blocuri care alcatuiesc sarpele
    # In functie de valoarea Vector2 a diferentei, putem spune in ce directie este capul:
    # 1. Vector2(1,0) -> stanga
    # 2. Vector2(-1,0) -> dreapta
    # 3. Vector2(0,1) -> sus
    # 4. Vector2(0,-1) -> jos
    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):
            self.head=self.head_left
        elif head_relation==Vector2(-1,0):
            self.head=self.head_right
        elif head_relation==Vector2(0,1):
            self.head=self.head_up
        elif head_relation==Vector2(0,-1):
            self.head=self.head_down

    # Functia care actualizeaza pozitia cozii
    # Se va face difernta dintre ultimele doua blocuri care alcatuiesc sarpele
    # In functie de valoarea Vector2 a diferentei, putem spune in ce directie este cozii:
    # 1. Vector2(1,0) -> stanga
    # 2. Vector2(-1,0) -> dreapta
    # 3. Vector2(0,1) -> sus
    # 4. Vector2(0,-1) -> jos
    def update_tail_graphics(self):
        tail_relation=self.body[-2]-self.body[-1]
        if tail_relation==Vector2(1,0):
            self.tail=self.tail_left
        elif tail_relation==Vector2(-1,0):
            self.tail=self.tail_right
        elif tail_relation==Vector2(0,1):
            self.tail=self.tail_up
        elif tail_relation==Vector2(0,-1):
            self.tail=self.tail_down

    # Functia care muta sarpele
    # Ideea de baza este ca renuntam la ultimul element din lista body
    # La head o sa adaugam directia pe care user-ul o da ca input
    def muta_sarpele(self):
        if self.new_block==True:
            body_copie = self.body[:]
            body_copie.insert(0, body_copie[0] + self.directie);
            self.body = body_copie[:]
            self.new_block=False;
        else:
            body_copie = self.body[:-1]
            body_copie.insert(0, body_copie[0] + self.directie);
            self.body = body_copie[:]

    # Functia care schimba starea de adaugare bloc nou din False in True
    def adauga_block(self):
        self.new_block=True;

    # Functia care adauga un sunet atunci cand fructul este mancat de catre sarpe
    def adauga_sunetul(self):
       self.sunet_mancat.play()

    # Metoda prin care atunci cand jucatorul pierde, sa punem sarpele intr-o pozitie default
    def resetare(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.directie = Vector2(0,0)

