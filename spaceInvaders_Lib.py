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
TODO -
     -
     -
     -
"""

#Importation des bibliothéques
from tkinter import Tk ,Label,Button,Canvas,PhotoImage

#Classes:
class alien:
    def __init__(self,hp,position,canevas):
        self.hp=hp
        self.position=position
        self.canevas = canevas

    def affichageAlien (self):
        self.alien = self.canevas.create_rectangle(600,500,200,300)
        print("wow")



## Fonctions graphiques ##
def createWindow():
    w=Tk()
    w.geometry('2400x1000')
    w.title('Space Invaders')

    canevas = Canvas(w, width = 1200, height = 650,  bg ='white')
    canevas.grid(row = 1, column = 0)
    photo=PhotoImage(file="jean-pierre.gif")
    item = canevas.create_image(600, 500,image = photo)

    

    score = Label(w, text = 'score :', fg = 'black')
    score.grid(row = 0, column = 0, sticky = 'nw')
    score.configure(font = 20)

    labelLives = Label(w, text = 'Vie restantes: 3', fg = 'black')
    labelLives.grid(row = 0, column = 0, sticky = 'ne')
    labelLives.configure(font = 20)

    buttonLeave = Button(w, text = 'Quitter', command = w.destroy)
    buttonLeave.grid(row = 1, column = 1, sticky = 's')
    buttonLeave.configure(font = 20)

    buttonBegin = Button(w, text = 'Nouvelle partie', command = '')
    buttonBegin.grid(row = 1, column = 1)
    buttonBegin.configure(font = 20)
    
    w.mainloop()   
