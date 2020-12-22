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
from spaceInvaders_Lib import alien, createWindow
from tkinter import PhotoImage


## Variables globales ##


## Programme principal ##

# Affichage du jeu #
Window = createWindow()

photo = PhotoImage(file="jean-pierre.gif")
item = Window[1].create_image(600, 500, image = photo)

alien=alien(12, 78, Window[1])
alien.affichageAlien()

Window[0].mainloop()

