#@Copyright: Joris CLEMENT, Corto Deschamps
#Header
"""
ce programme permet de jouer dans une interface graphique à space invader
vous avez 3 vies, le but et d'avoir de le meilleur score possible
Auteur: Joris CLEMENT Corto DESCHAMPS.
date de réalisation: 22/12/2020


Github:https://github.com/jorisclement/CS-Dev-TP3.git

"""
"""
TODO -
     -
     -
"""


#------------------------------------------------- Importation des bibliothéques----------------------------------------------------------#
from game import Game



# -----------------------------------------------------Variables globales---------------------------------------------------------------- #
Hi = 1000  # Hauteur en pixels du canevas 
dx = 3    # Nombre de pixels dont on déplacera les aliens toutes les t ms sur l'axe des X
dy = 0    # Nombre de pixels dont on déplacera les aliens toutes les t ms sur l'axe des Y
t = 20    


#------------------------------------------------------- Programme principal---------------------------------------------------------------#



# Affichage du jeu #
game = Game(Hi, dx, dy, t)
game.hitBox()
game.Mainloop()





