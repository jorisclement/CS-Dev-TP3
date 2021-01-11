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
TODO -faire les barricades
     -faire le score
     -appliquer un effet aux tirs des aliens
     -gèrer les vies
     -delay entre les balles
"""

## Importation des bibliothéques ##
from tkinter import Tk ,Label, Button, Canvas, PhotoImage
from random import randint

## Classes ##
class Window:
    def __init__(self):
        self.w = Tk()     
        self.w.geometry('2400x1000')
        self.w.title('Space Invaders')
        
        self.canevas = Canvas(self.w, width = 1200, height = 650,  bg ='white')  
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

        self.buttonBegin = Button(self.w, text = 'Nouvelle partie', command = '')
        self.buttonBegin.grid(row = 1, column = 1)
        self.buttonBegin.configure(font = 20)

    
    def Mainloop(self):
        self.w.mainloop()



class Draw(Window):
    def __init__(self):
        Window.__init__(self)
        self.compteur_edf = 0
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

        return line1, line2, line3, line4, line5

    
    def drawSpaceships(self):
        self.spaceships = self.canevas.create_rectangle(560, 580, 640, 650, fill = "green", tags = "A")

        return self.spaceships


    def createBuletsShips(self, event):
        if len(self.bulletsShips) > 1:
            self.bulletsShips = self.bulletsShips
            
        else:
            bullet = self.canevas.create_line((self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, 580, (self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, 620, fill = "green", width = 10,tags = "C")
            self.bulletsShips.append(bullet)


    def createBuletsAliens(self):
        r = randint(0, len(self.Aliens2) - 1)
        if self.compteur_edf == 1:
            return -1
        else:    
            self.bulletAlien = self.canevas.create_line((self.canevas.coords(self.Aliens2[r])[0] + self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3], (self.canevas.coords(self.Aliens2[r])[0]+self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3] + 40, fill = "black", tags = "E", width = 10)
            self.bulletsAlien.append(self.bulletAlien)
            self.w.after(4000, self.createBuletsAliens)
        


class Move(Draw):
    def __init__(self, dx, dy, t):
        Draw.__init__(self)
        (self.line1, self.line2, self.line3, self.line4, self.line5) = Draw.drawAliens(self)
        self.spaceships = Draw.drawSpaceships(self)
        Draw.createBuletsAliens(self)
        
        self.dx = dx
        self.dy = dy
        self.t = t
        self.c = 0
        self.bounce = 0
        

    def moveAliens(self):
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
            if self.canevas.coords(alien)[3] > 580:
                self.canevas.delete(self.spaceships)
                self.dx = 0
                self.dy = 0

        
        self.canevas.move("B", self.dx, self.dy)        
        self.w.after(self.t, self.moveAliens)

    
    def right (self,event):
        if self.canevas.coords(self.spaceships)[2] < 1200 : 
            self.canevas.move(self.spaceships,20,0)
        else :
            self.canevas.move(self.spaceships,0,0)
        
    
    def left (self,event):
        if self.canevas.coords(self.spaceships)[0] > 0:
            self.canevas.move(self.spaceships,-20,0)
        else :
            self.canevas.move(self.spaceships,0,0)


    def moveSpaceships(self):
        self.canevas.bind_all('<Right>', self.right)
        self.canevas.bind_all('<Left>', self.left)
        
        
    def moveBulet2(self):
        self.canevas.move("C", 0, -20)
        self.w.after(self.t, self.moveBulet2)
        


    def moveBulet(self):
        self.canevas.bind_all('<space>', self.createBuletsShips)

    
    def moveBuletAliens(self):
        self.canevas.move("E", 0, 6)
        self.w.after(self.t, self.moveBuletAliens)
    


class Game(Move):    
    def __init__(self, dx, dy, t):
        Move.__init__(self, dx, dy, t)
        Move.moveAliens(self)
        Move.moveSpaceships(self)
        Move.moveBulet2(self)
        Move.moveBulet(self)
        Move.moveBuletAliens(self)
        self.lives = [3]
        self.scoring = 0
 

    def hitBox(self):

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
    
                    self.canevas.delete(self.bulletsShips[-1])
                    self.bulletsShips.pop(-1)
        #def scoring (self):            
        self.printScore = "score :",self.scoring
        self.score.configure( text = self.printScore)



        for bullet in self.bulletsAlien:
            
            if self.canevas.coords(bullet)[3] > self.canevas.coords(self.spaceships)[1]   and self.canevas.coords(bullet)[1] < self.canevas.coords(self.spaceships)[3]   and self.canevas.coords(bullet)[0] < self.canevas.coords(self.spaceships)[2]   and self.canevas.coords(bullet)[2] > self.canevas.coords(self.spaceships)[0]:
                self.lives.append( self.lives[-1] - 1)
                self.printLives = "vie restantes: ",self.lives[-1]
                self.labelLives.configure (text = self.printLives)
                self.canevas.delete(self.bulletsAlien[-1])
                self.bulletsAlien.pop(-1)

    #def defeat(self)
        if self.lives[-1] == 0:
            self.dx = 0
            self.dy = 0
            self.canevas.delete(self.spaceships)
            self.compteur_edf = 1

        
        self.w.after(self.t, self.hitBox)

       

    
   

           

