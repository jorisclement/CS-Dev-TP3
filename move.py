#------------------------------------------------- Importation des bibliothéques----------------------------------------------------------#

from draw import Draw

class Move(Draw):
    # Cette classe permet de déplacer les objet créés dans la draw
    def __init__(self, hi, dx, dy, t):
        Draw.__init__(self, hi) # Héritage de la fonction Draw
        Draw.drawAliens(self)
        self.aliensNumber = len(self.Aliens2)
        self.spaceships = Draw.drawSpaceships(self)
       
        Draw.createBuletsAliens(self)
        (self.Barricades1, self.Barricades2, self.Barricades3) = Draw.drawBarricades(self)
        self.Barricades = self.Barricades1 + self.Barricades2 + self.Barricades3
        
        self.dx = dx
        self.dy = dy
        self.t = t
        self.c = 0
        self.bounce = 0
        self.cLoose = 0
        
    def moveAliens(self):
        # Création du déplacement des aliens

        if self.stop == 1: # Condition verifiée lorsqu'on arrête le programme (empêche la méthode de boucler indéfiniment)
            return -1
        
        else:
            for line in self.Aliens:
                if self.canevas.coords(line[-1])[2] > 1200 and self.bounce == 0:     
                    self.dx = -self.dx
                    if self.dx < 0:
                        self.bounce = 1

                elif self.canevas.coords(line[0])[0] < 0 and self.bounce == 1:   
                    self.dx = -self.dx
                    self.c = 2     
                    if self.dx > 0:
                        self.bounce = 0

            if self.c == 2:
                self.canevas.move("B", 0, 50)
                self.c = 0

            for alien in self.Aliens2:
                if self.canevas.coords(alien)[3] >= self.canevas.coords(self.spaceships)[1]:
                   self.cLoose = 1

            self.canevas.move("B", self.dx, self.dy)        
            self.w.after(self.t, self.moveAliens)

    def right (self,event):
        # Evenement qui permet d'aller à droite
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[2] < 1200 : # Condition qui empéche le vaisseau de sortir du canvas par la droite
                self.canevas.move(self.spaceships,20,0)
            else :
                self.canevas.move(self.spaceships,0,0) 
        
    def left (self,event):
        # Evenement qui permet de déplacer le vaisseau à gauche
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[0] > 0: # Condition qui empéche le vaisseau de sortir du canvas par la gauche
                self.canevas.move(self.spaceships,-20,0)
            else :
                self.canevas.move(self.spaceships,0,0)

    def moveSpaceships(self):
        # Permet d'associer une touches aux événements précedents
        self.canevas.bind_all('<Right>', self.right) # Appel l'événement right lorsqu'on appui sur la touche droite
        self.canevas.bind_all('<Left>', self.left)
        
        
    def moveBulet2(self):
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("C", 0, -20) # Permet de déplacer les balles du vaisseau (tag C) de 20 pixels vers le haut
            self.w.after(self.t, self.moveBulet2) # Le déplacement se répéte toute les t secondes
            
    def moveBulet(self):
        #Permet de créer un balle lorsqu'on appuie sur la barre espace
        self.canevas.bind_all('<space>', self.createBuletsShips)

    def moveBuletAliens(self):
        # Permet de faire bouger les balles aliens précédemment créées
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("E", 0, 20) # Permet de déplacer les balles aliens (tag E) de 20 pixels vers le bas
            self.w.after(self.t, self.moveBuletAliens) # Le déplacement se répéte toute les t secondes