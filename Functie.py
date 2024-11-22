import pygame
import sys
from Fruct import Fruct
from Sarpe import Sarpe
from Main import Main
from pygame.math import Vector2

# Adauga aceasta conditie la sunet pentru a avea o experienta mai buna
pygame.mixer.pre_init(44100,-16,2,512)

# Initializarea jocului
pygame.init()

# Vom schimba numele ferestrei de joc din 'pygame window' in 'Snake Game'
pygame.display.set_caption('Snake Game')

# Vom schimba iconita default cu o imagine cu un serpis or
Iconita=pygame.image.load('Imagini/Snake.png');
pygame.display.set_icon(Iconita);

# Se vor declara variabile care retin dimensiunea unei celule si numarul de celule din canvas
cell_size=40;
cell_number=20;

# Crearea ferestrei in care ne vom juca
# In paranteza, primul parametru reprezita latimea, iar cel de-al doilea inaltimea
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))

# Vom aplica grafica fructului
Mar=pygame.image.load('Imagini/apple.png').convert_alpha()
Mar=pygame.transform.scale(Mar,(cell_size,cell_size))

# Este initializat un ceas care ajuta sa controlam ceasul in Python
clock=pygame.time.Clock()

# Vom crea un font
font=pygame.font.Font('Font/PoetsenOne-Regular.ttf',50)

# Se va crea un eveniment pentru a capta un eveniment provocat de user
SCREEN_UPDATE=pygame.USEREVENT

# Se va crea un timer pentru receptarea evenimentului
pygame.time.set_timer(SCREEN_UPDATE,150)

# Se va crea un obiect de tipul Main
jocul=Main(cell_number)

# Acest while va merge la infinit daca nu se da o conditie de oprire din interior
while True:

    # In acest for vom cauta ce evenimente apar pe parcursul jocului
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  # Spre exemplu, daca apare evenimentul pygame.QUIT
            pygame.quit() # Vom inchide jocul
            sys.exit() # Inchidere suplimentara de la system
        if event.type==SCREEN_UPDATE: # Daca are loc un eveniment de la user
            jocul.update(cell_number) # Muta sarpele
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if jocul.sarpe.directie.y!=1:
                    jocul.sarpe.directie=Vector2(0,-1)
            if event.key==pygame.K_DOWN:
                if jocul.sarpe.directie.y!=-1:
                    jocul.sarpe.directie=Vector2(0,1);
            if event.key==pygame.K_LEFT:
                if jocul.sarpe.directie.x!=1:
                    jocul.sarpe.directie=Vector2(-1,0);
            if event.key == pygame.K_RIGHT:
                if jocul.sarpe.directie.x!=-1:
                    jocul.sarpe.directie=Vector2(1,0);

    # Vom colara ecranul folosind functia fill, care primeste ca parametru un tuplu RGB
    screen.fill((176,215,70))

    # Vom desena elementele pe canvas cu noua functie din main
    jocul.deseneaza_elementele(cell_number,cell_size,screen,Mar,font)

    # Prin această comandă se va afișa pe ecran orice modificare în cadrul jocului
    pygame.display.update()

    # Prin acestă comandă setăm cu cate frame-uri pe secunda sa se dezfasoare jocul
    clock.tick(100)