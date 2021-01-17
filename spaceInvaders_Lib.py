#@Copyright: Joris CLEMENT, Corto Deschamps
#Header
"""
ce programme permet de jouer dans une interface graphique à space invader
vous avez 3 vies, le but et d'avoir de le meilleur score possible
Auteur: Joris CLEMENT.
date de réalisation: 22/12/2020


Github:https://github.com/jorisclement/CS-Dev-TP3.git

"""
"""
TODO -Pouvoir relancer une partie (fonctionnelle) à n'importe quelle moment
     -Appliquer un effet a l'impacte tirs des aliens (pour aller plus loin)
     -Tableau des scores (pour aller plus loin)
"""

## Importation des bibliothéques ##
from tkinter import Tk ,Label, Button, Canvas, PhotoImage
from random import randint

## Classes ##
class Window:
    def __init__(self, hi):
        self.Hi = hi

        self.w = Tk()     
        self.w.geometry('2400x1200')
        self.w.title('Space Invaders')
        
        self.canevas = Canvas(self.w, width = 1200, height = self.Hi,  bg ='white')  
        self.canevas.grid(row = 1, column = 0)
        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "D")
        self.canevas.tag_raise("A")     # Ces quatres lignes gèrent la position en profondeur des différents élèments du
        self.canevas.tag_raise("B")     # Canvas
        self.canevas.tag_raise("C")
        self.canevas.tag_lower("D")
              

        self.score = Label(self.w, text = 'score : 0', fg = 'black')
        self.score.grid(row = 0, column = 0, sticky = 'nw')
        self.score.configure(font = 20)

        self.labelLives = Label(self.w, text = "vie restantes : 3", fg = 'black')
        self.labelLives.grid(row = 0, column = 0, sticky = 'ne')
        self.labelLives.configure(font = 20)
        

        self.buttonLeave = Button(self.w, text = 'Quitter', command = self.w.destroy)
        self.buttonLeave.grid(row = 1, column = 1, sticky = 's')
        self.buttonLeave.configure(font = 20)

        self.buttonReload = Button(self.w, text = 'Nouvelle partie', command = '')
        self.buttonReload.grid(row = 1, column = 1)
        self.buttonReload.configure(font = 20)



    
    def Mainloop(self):
        self.w.mainloop()



class Draw(Window):
    def __init__(self, hi):
        Window.__init__(self, hi)
        
        self.stop = 0
        self.bulletsShips = [self.canevas.create_line(1249, 649, 1250, 650)]
        self.bulletsAlien = [self.canevas.create_line(1249, 649, 1250, 650)]
    
    def drawAliens(self):
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

        self.Aliens = [line1 ,line2 ,line3 ,line4 ,line5]
        self.Aliens2 = line1 + line2 + line3 + line4 +line5
    
    def drawSpaceships(self):
        self.spaceships = self.canevas.create_rectangle(561, self.Hi-70, 641, self.Hi, fill = "green", tags = "A")

        return self.spaceships


    def createBuletsShips(self, event):
        if len(self.bulletsShips) > 1:
            self.bulletsShips = self.bulletsShips
            
        else:
            bullet = self.canevas.create_line((self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1], (self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1] + 40, fill = "green", width = 10,tags = "C")
            self.bulletsShips.append(bullet)


    def createBuletsAliens(self):
        if self.stop == 1:
            return -1
        
        else:
            r = randint(0, len(self.Aliens2) - 1)

            self.bulletAlien = self.canevas.create_line((self.canevas.coords(self.Aliens2[r])[0] + self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3], (self.canevas.coords(self.Aliens2[r])[0]+self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3] + 40, fill = "black", tags = "E", width = 10)
            self.bulletsAlien.append(self.bulletAlien)
            self.w.after(2500, self.createBuletsAliens)
        

    def drawBarricades(self):
        Barricade1 = []
        Barricade2 = []
        Barricade3 = []

        for line in range(2):
            for col in range(6):
                Barricade1.append(self.canevas.create_rectangle(50 + col*50, self.Hi - 200  + line*50, 100 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade2.append(self.canevas.create_rectangle(450 + col*50, self.Hi - 200  + line*50, 500 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade3.append(self.canevas.create_rectangle(850 + col*50, self.Hi - 200  + line*50, 900 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))

        return Barricade1, Barricade2, Barricade3

class Move(Draw):
    def __init__(self, hi, dx, dy, t):
        Draw.__init__(self, hi)
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
        print(self.stop)
        if self.stop == 1:
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
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[2] < 1200 : 
                self.canevas.move(self.spaceships,20,0)
            else :
                self.canevas.move(self.spaceships,0,0)
        
    
    def left (self,event):
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[0] > 0:
                self.canevas.move(self.spaceships,-20,0)
            else :
                self.canevas.move(self.spaceships,0,0)


    def moveSpaceships(self):
        self.canevas.bind_all('<Right>', self.right)
        self.canevas.bind_all('<Left>', self.left)
        
        
    def moveBulet2(self):
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("C", 0, -20)
            self.w.after(self.t, self.moveBulet2)
            


    def moveBulet(self):
        self.canevas.bind_all('<space>', self.createBuletsShips)

    
    def moveBuletAliens(self):
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("E", 0, 20)
            self.w.after(self.t, self.moveBuletAliens)
    


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

        

    
            
    
       

    
   

           

