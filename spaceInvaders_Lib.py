#@Copyright: Joris CLEMENT, Corto Deschamps
#Header
"""
ce programme permet de jouer dans une interface graphique à space invader
vous avez 3 vie, le but et d'avoir de le meilleur score possible
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
from tkinter import Tk,Label,Button

#Fonctions:

def creatWindow ():
    w=Tk()
    w.geometry('2400x500')
    w.title('Space Invaders')

    

    score = Label(w, text = 'score :', fg = 'black')
    score.grid(row = 0, column = 0)
    score.configure(font = 20)

    buttonLeave = Button(w, text = 'Quitter', command = w.destroy)
    buttonLeave.grid(row = 0, column = 1)
    buttonLeave.configure(font = 20)
    
    w.mainloop()   