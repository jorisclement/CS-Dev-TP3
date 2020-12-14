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
    w.geometry('2400x500')
    w.title('Space Invaders')

    Canevas = Canvas(w, width = 2200, height = 450,  bg ='white')
    Canevas.grid(row = 0, column = 3)
    item = Canevas.create_image(2200, 450,anchor="center",image = PhotoImage(file = "pitbull.jpg") )
       


    score = Label(w, text = 'score :', fg = 'black')
    score.grid(row = 0, column = 0)
    score.configure(font = 20)

    buttonLeave = Button(w, text = 'Quitter', command = w.destroy)
    buttonLeave.grid(row = 0, column = 1)
    buttonLeave.configure(font = 20)
    
    w.mainloop()   