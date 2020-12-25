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
TODO -Faire bouger "l'alien"
     -Tout le reste
     -
     -
"""

## Importation des bibliothéques ##
from tkinter import Tk ,Label, Button, Canvas, PhotoImage


## Classes ##
class alien:
    def __init__(self, dx, dy, t):
        self.dx = dx
        self.dy = dy
        self.t = t

        self.w = Tk()
        self.canevas = Canvas(self.w, width = 1200, height = 650,  bg ='white')
        self.alien1 = self.canevas.create_rectangle(30, 10, 120, 80, fill = "red", tags = "A")


    def moveAlien(self):
        self.canevas.move(self.alien1, self.dx, self.dy)        
        self.w.after(self.t, self.moveAlien)


    def createWindow(self):       
        self.w.geometry('2400x1000')
        self.w.title('Space Invaders')
       
        self.canevas.grid(row = 1, column = 0)
        photo = PhotoImage(file="jean-pierre.gif")
        item = self.canevas.create_image(600, 500, image = photo, tags = "B")
        self.canevas.tag_raise("A")     # Ces deux lignes gèrent la position en profondeur des différents élèments du
        self.canevas.tag_lower("B")     # Canvas  

        score = Label(self.w, text = 'score :', fg = 'black')
        score.grid(row = 0, column = 0, sticky = 'nw')
        score.configure(font = 20)

        labelLives = Label(self.w, text = 'Vie restantes: 3', fg = 'black')
        labelLives.grid(row = 0, column = 0, sticky = 'ne')
        labelLives.configure(font = 20)

        buttonLeave = Button(self.w, text = 'Quitter', command = self.w.destroy)
        buttonLeave.grid(row = 1, column = 1, sticky = 's')
        buttonLeave.configure(font = 20)

        buttonBegin = Button(self.w, text = 'Nouvelle partie', command = '')
        buttonBegin.grid(row = 1, column = 1)
        buttonBegin.configure(font = 20)

        self.w.mainloop()


