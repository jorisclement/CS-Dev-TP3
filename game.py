#@Copyright: Joris CLEMENT, Corto Deschamps
#Header
"""
ce programme permet de jouer dans une interface graphique à space invader
vous avez 3 vies, le but et d'avoir de le meilleur score possible
Auteur: Joris CLEMENT Corto DESCHAMPS.
date de réalisation: 22/12/2020


Github:https://github.com/jorisclement/CS-Dev-TP3.git

"""
"""
TODO -Pouvoir relancer une partie (fonctionnelle) à n'importe quelle moment
     -Appliquer un effet a l'impacte tirs des aliens (pour aller plus loin)
     -Tableau des scores (pour aller plus loin)
"""

## Importation des bibliothéques ##
from move import Move
from draw import Draw
from random import randint
from tkinter import Label, Button, PhotoImage


## Classes ##
class Game(Move):    
    def __init__(self, hi, dx, dy, t):
        Move.__init__(self, hi, dx, dy, t)
        Move.moveAliens(self)
        Move.moveSpaceships(self)
        Move.moveBulet2(self)
        Move.moveBulet(self)
        Move.moveBuletAliens(self)
        self.lives = 3
        self.scoring = 0
        

    def hitBox(self):
        if self.cLoose == 1:
            self.Defeat()
            return -1
        
        else:
            if self.canevas.coords(self.bulletsShips[-1])[1] < 0:
                    self.canevas.delete(self.bulletsShips[-1])
                    self.bulletsShips.pop(-1)
            
            for line in self.Aliens:
                for alien in line:
                    if self.canevas.coords(self.bulletsShips[-1])[1] < self.canevas.coords(alien)[3]   and self.canevas.coords(self.bulletsShips[-1])[3] > self.canevas.coords(alien)[1]   and self.canevas.coords(self.bulletsShips[-1])[0] < self.canevas.coords(alien)[2]   and self.canevas.coords(self.bulletsShips[-1])[2] > self.canevas.coords(alien)[0]:
                        line.remove(alien)
                        if len(line) == 0:
                            del self.Aliens[self.Aliens.index(line)]
                            
                        self.Aliens2.remove(alien)
                        self.canevas.delete(alien)

                        self.scoring = self.scoring + 100
                        self.Scoring()
        
                        self.canevas.delete(self.bulletsShips[-1])
                        self.bulletsShips.pop(-1)

                        if len(self.Aliens2) == self.aliensNumber/2:
                            self.dx = 1.5*self.dx

                        if len(self.Aliens2) == 0:
                            self.Win()

            for bullet in self.bulletsAlien:
                if self.canevas.coords(bullet)[3] > self.canevas.coords(self.spaceships)[1]   and self.canevas.coords(bullet)[1] < self.canevas.coords(self.spaceships)[3]   and self.canevas.coords(bullet)[0] < self.canevas.coords(self.spaceships)[2]   and self.canevas.coords(bullet)[2] > self.canevas.coords(self.spaceships)[0]:
                    self.lives -= 1
                    self.printLives = "vie restantes: ", str(self.lives)
                    if self.lives == 0:
                        self.Scoring
                        self.Defeat()
                    
                    self.labelLives.configure (text = "".join(self.printLives))
                    
                    self.canevas.delete(self.bulletsAlien[-1])
                    self.bulletsAlien.pop(-1)

            if len(self.Barricades) != 0:
                for barricade in self.Barricades:
                    if self.canevas.coords(self.bulletsShips[-1])[1] < self.canevas.coords(barricade)[3]   and self.canevas.coords(self.bulletsShips[-1])[3] > self.canevas.coords(barricade)[1]   and self.canevas.coords(self.bulletsShips[-1])[0] < self.canevas.coords(barricade)[2]   and self.canevas.coords(self.bulletsShips[-1])[2] > self.canevas.coords(barricade)[0]:
                        if self.canevas.itemcget(barricade, "fill") == "red":
                            self.canevas.delete(barricade)
                            self.Barricades.remove(barricade)
                            
                            self.canevas.delete(self.bulletsShips[-1])
                            self.bulletsShips.pop(-1)
                            
                            break

                        self.canevas.itemconfigure(barricade, fill = "red")

                        self.canevas.delete(self.bulletsShips[-1])
                        self.bulletsShips.pop(-1)
                        

                    if self.canevas.coords(self.bulletsAlien[-1])[3] > self.canevas.coords(barricade)[1]   and self.canevas.coords(self.bulletsAlien[-1])[1] < self.canevas.coords(barricade)[3]   and self.canevas.coords(self.bulletsAlien[-1])[0] < self.canevas.coords(barricade)[2]   and self.canevas.coords(self.bulletsAlien[-1])[2] > self.canevas.coords(barricade)[0]:
                        self.canevas.delete(barricade)
                        self.Barricades.remove(barricade)

                        self.canevas.delete(self.bulletsAlien[-1])
                        self.bulletsAlien.pop(-1)
            
            self.w.after(self.t, self.hitBox)

    
    def Scoring(self):        
        self.printScore = "score :", str(self.scoring)
        self.score.configure(text = "".join(self.printScore))


    def Defeat(self):
        defeatTxt = "Oh niiooon, vous avez perdu. Votre score est de: ", str(self.scoring)

        self.dx = 0
        self.dy = 0
        self.canevas.delete(self.spaceships)
        
        self.labelDefeat = Label(self.w, text = "".join(defeatTxt), fg = 'black')
        self.labelDefeat.grid(row = 1, column = 0)
        self.labelDefeat.configure(font = 20)
        
        self.stop = 1
        self.cLoose = 1

        self.buttonReload["command"] = self.Reload


    def Win(self):
        winTxt = "Wouhouuu, vous avez obtenu le score maximal: ", str(self.scoring)

        self.labelWin = Label(self.w, text = "".join(winTxt), fg = 'black')
        self.labelWin.grid(row = 1, column = 0)
        self.labelWin.configure(font = 20)

        self.stop = 1
        
        self.buttonReload["command"] = self.Reload


    def Reload(self):
        self.canevas.delete(all)
        
        self.scoring = 0
        self.Scoring()
        
        self.lives = 3
        self.printLives = "vie restantes: ", str(self.lives)
        
        if self.cLoose == 1:
            self.labelDefeat.destroy()
        else:
            self.labelWin.destroy()

        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "D")

        self.labelHelp = Label(self.w, text = "Etes vous prêt à jouer?", fg = 'black')
        self.labelHelp.grid(row = 1, column = 0, sticky = "n")
        self.labelHelp.configure(font = 20)

        self.cLoose = 0
        self.stop = 0
        
        Draw.drawAliens(self)
        (self.Barricades1, self.Barricades2, self.Barricades3) = Draw.drawBarricades(self)
        self.Barricades = self.Barricades1 + self.Barricades2 + self.Barricades3
        Draw.drawSpaceships(self)

        self.buttonYes = Button(self.w, text = "oui", command = self.reMove)
        self.buttonYes.grid(row = 1, column = 0)
        self.buttonYes.configure(font = 20)

        
    def reMove(self):
        self.buttonYes.destroy()
        self.labelHelp.destroy()
        self.hitBox()

        Move.moveAliens(self)
        Move.moveSpaceships(self)
        Move.moveBulet2(self)
        Move.moveBulet(self)
        Move.moveBuletAliens(self)

        Draw.createBuletsAliens(self)

        

    
            
    
       

    
   

           

