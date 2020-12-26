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
TODO -Gérer la sortie d'écran
     -Rajouter le vaisseau 
     -
     -
"""

## Importation des bibliothéques ##
from tkinter import Tk ,Label, Button, Canvas, PhotoImage


## Classes ##
class Window:
    def __init__(self):
        self.w = Tk()     
        self.w.geometry('2400x1000')
        self.w.title('Space Invaders')
        
        self.canevas = Canvas(self.w, width = 1200, height = 650,  bg ='white')  
        self.canevas.grid(row = 1, column = 0)
        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "B")
        self.canevas.tag_raise("A")     # Ces deux lignes gèrent la position en profondeur des différents élèments du
        self.canevas.tag_lower("B")     # Canvas  

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
        
    
    def drawAlien(self):
        self.alien1 = self.canevas.create_rectangle(30, 10, 120, 80, fill = "red", tags = "A")
        
        return self.alien1


class Move(Draw):
    def __init__(self, dx, dy, t):
        Draw.__init__(self)
        self.alien1 = Draw.drawAlien(self)
        self.dx = dx
        self.dy = dy
        self.t = t

    def moveAlien(self):
        self.canevas.move(self.alien1, self.dx, self.dy)        
        self.w.after(self.t, self.moveAlien)
    
    def Mainloop(self):
        self.w.mainloop()
    