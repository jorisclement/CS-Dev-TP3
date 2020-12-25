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
class Window:
    def createWindow(self):
        self.w = Tk()       
        self.w.geometry('2400x1000')
        self.w.title('Space Invaders')
       
        self.canevas = Canvas(self.w, width = 1200, height = 650,  bg ='white')
        self.canevas.grid(row = 1, column = 0)
        self.canevas = Canvas(self.w, width = 1200, height = 650,  bg ='white')
        self.photo = PhotoImage(file = "jean-pierre.gif")
        self.canevas.create_image(600, 500, image = self.photo)
            

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

        self.w.mainloop()


