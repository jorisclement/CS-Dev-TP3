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

#Fonctions:

def createWindow ():
    w=Tk()
    w.geometry('2400x1000')
    w.title('Space Invaders')

    Canevas = Canvas(w, width = 1200, height = 650,  bg ='white')
    Canevas.grid(row = 1, column = 0)
    item = Canevas.create_image(0, 0, anchor = 'nw', image = PhotoImage(file = "pitbull.gif"))

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