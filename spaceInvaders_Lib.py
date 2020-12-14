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
    w.geometry('2400x700')
    w.title('Space Invaders')

    Canevas = Canvas(w, width = 1200, height = 650,  bg ='white')
    Canevas.grid(row = 1, column = 0)
    item = Canevas.create_image(120, 350,anchor="center",image = PhotoImage(file = "pitbull.gif") )
       


    score = Label(w, text = 'score :', fg = 'black')
    score.grid(row = 0, column = 0)
    score.configure(font = 20)

    labelLives = Label(w, text = 'Vie restantes: 3', fg = 'black')
    labelLives.grid(row = 0, column = 2)
    labelLives.configure(font = 20)

    buttonLeave = Button(w, text = 'Quitter', command = w.destroy)
    buttonLeave.grid(row = 2, column = 4)
    buttonLeave.configure(font = 20)

    buttonBegin = Button(w, text = 'Nouvelle partie', command = '')
    buttonBegin.grid(row = 1, column = 4)
    buttonBegin.configure(font = 20)
    
    w.mainloop()   