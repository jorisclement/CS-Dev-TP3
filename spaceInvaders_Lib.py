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
TODO -mettre un cool down sur les tirs (on peut trop spammer je pense)
     -faire le score
     -tir des aliens
     -gèrer les vies
     -delay entre les balles
"""

## Importation des bibliothéques ##
from tkinter import Tk ,Label, Button, Canvas, PhotoImage
#import time 

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

        self.score = Label(self.w, text = 'score :', fg = 'black')
        self.score.grid(row = 0, column = 0, sticky = 'nw')
        self.score.configure(font = 20)

        self.labelLives = Label(self.w, text = 'Vie restantes: 3', fg = 'black')
        self.labelLives.grid(row = 0, column = 0, sticky = 'ne')
        self.labelLives.configure(font = 20)

        self.buttonLeave = Button(self.w, text = 'Quitter', command = self.w.destroy)
        self.buttonLeave.grid(row = 1, column = 1, sticky = 's')
        self.buttonLeave.configure(font = 20)

        self.buttonBegin = Button(self.w, text = 'Nouvelle partie', command = '')
        self.buttonBegin.grid(row = 1, column = 1)
        self.buttonBegin.configure(font = 20)



class Draw(Window):
    def __init__(self):
        Window.__init__(self)
        
    
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

        return line1, line2, line3, line4, line5

    
        

    def drawSpaceships(self):
        self.spaceships = self.canevas.create_rectangle(560, 580, 640, 650, fill = "green", tags = "A")

        return self.spaceships


    def createBulet(self, event):
        self.canevas.create_line((self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, 580, (self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, 620, fill = "green", width = 10,tags = "C")
        #time.sleep(0.1)
    

class Move(Draw):
    def __init__(self, dx, dy, t):
        Draw.__init__(self)
        self.line5 = Draw.drawAliens(self)[4]
        self.spaceships = Draw.drawSpaceships(self)
        self.bullets = []
        self.dx = dx
        self.dy = dy
        self.t = t
        self.c = 0


    def moveAliens(self):
        if self.canevas.coords(self.line5[-1])[2] > 1200 or self.canevas.coords(self.line5[0])[0] < 0:
            self.dx = -self.dx
            self.c += 1

        elif self.c == 2:
            self.canevas.move("B", 0, 50)
            self.c = 0

        elif self.canevas.coords(self.line5[1])[3] > 580:
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
        self.canevas.bind_all('<space>', self.createBulet) 
        
        
    
    def Mainloop(self):
        self.w.mainloop()
    
    