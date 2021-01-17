#------------------------------------------------- Importation des bibliothéques----------------------------------------------------------#

from window import Window
from random import randint


class Draw(Window):
    # Cette classe permet de créer les differentes formes necessaires au programme,(aliens,spaceships,balles,barricades).

    def __init__(self, hi):
        Window.__init__(self, hi) # Héritage de la fonction window
        self.stop = 0  # Valeur utilisée pour arreter le programme quand elle passera à 1
        self.bulletsShips = [self.canevas.create_line(1249, 649, 1250, 650)] # Création d'une liste de balles pour le vaisseau (avec 1 element pour qu'elle ne soit jamais vide)
        self.bulletsAlien = [self.canevas.create_line(1249, 649, 1250, 650)] # Création d'une liste de balles pour les aliens (avec 1 element pour qu'elle ne soit jamais vide)
    
    def drawAliens(self):
        # Fonction qui permet de créer les aliens par ligne de 8 aliens
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        line5 = []

        for i in range(8):
            line1.append(self.canevas.create_rectangle(120*i+50, 10, 120*i+120, 40, fill = "red", tags = "B"))
            line2.append(self.canevas.create_oval(120*i+50, 50, 120*i+120, 80, fill = "yellow", tags = "B"))
            line3.append(self.canevas.create_oval(120*i+50, 90, 120*i+120, 120, fill = "blue", tags = "B"))
            line4.append(self.canevas.create_rectangle(120*i+50, 130, 120*i+120, 160, fill = "magenta", tags = "B"))
            line5.append(self.canevas.create_oval(120*i+50, 170, 120*i+120, 200, fill = "black", tags = "B"))

        self.Aliens = [line1 ,line2 ,line3 ,line4 ,line5] # Liste de listes contenant tous les aliens
        self.Aliens2 = line1 + line2 + line3 + line4 + line5 # Liste contenant tous les aliens (pratique dans certain cas)
    
   
    def drawSpaceships(self):
        # Création du vaisseau sous forme d'un carré vert
        self.spaceships = self.canevas.create_rectangle(561, 930, 641, 1000, fill = "green", tags = "A")

        return self.spaceships


    def createBuletsShips(self, event):
        # Création des balles du vaisseau, ne pouvant etre tirées que une par une (régle du jeu Space Invader de base)
        if len(self.bulletsShips) > 1: # Condition pour empécher le joueur de tirer plusieur fois
            self.bulletsShips = self.bulletsShips
            
        else:
            bullet = self.canevas.create_line((self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1], (self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1] + 40, fill = "green", width = 10,tags = "C")
            self.bulletsShips.append(bullet)


    def createBuletsAliens(self):
        # Création des balles aliens qui s'ajoutent dans la liste créé précédemment et qui s'affiche sur le canvas

        if self.stop == 1: # Condition verifiée lorsqu'on arrête le programme (empêche la méthode de boucler indéfiniment)
            return -1
        
        else:              # Condition verifiée quand le programme est actif
            r = randint(0, len(self.Aliens2) - 1)

            # Création d'un balle dans le canvas au niveau d'un alien aléatoire
            self.bulletAlien = self.canevas.create_line((self.canevas.coords(self.Aliens2[r])[0] + self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3], (self.canevas.coords(self.Aliens2[r])[0]+self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3] + 40, fill = "black", tags = "E", width = 10)
            self.bulletsAlien.append(self.bulletAlien)
            self.w.after(2500, self.createBuletsAliens)
        

    def drawBarricades(self):
        # Création des barricades par ligne
        Barricade1 = []
        Barricade2 = []
        Barricade3 = []

        for line in range(2):
            for col in range(6):
                Barricade1.append(self.canevas.create_rectangle(50 + col*50, self.Hi - 200  + line*50, 100 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade2.append(self.canevas.create_rectangle(450 + col*50, self.Hi - 200  + line*50, 500 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade3.append(self.canevas.create_rectangle(850 + col*50, self.Hi - 200  + line*50, 900 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))

        return Barricade1, Barricade2, Barricade3