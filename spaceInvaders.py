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
"""


## Importation des bibliothéques ##
from spaceInvaders_Lib import alien
from tkinter import PhotoImage


## Variables globales ##
t = 20
dx = 0
dy = 5   # Nombre de pixels dont on déplacera les aliens toutes les t ms

## Programme principal ##

# Affichage du jeu #
alien = alien(dx, dy, t)
alien.moveAlien()
alien.createWindow()




