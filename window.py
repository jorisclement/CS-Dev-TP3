#------------------------------------------------- Importation des bibliothéques----------------------------------------------------------#

from tkinter import Tk ,Label, Button, Canvas, PhotoImage




class Window:
    # cette classe permet de créer notre interface graphique, notamment la fenêtre dans laquelle on trouve le canvas, 2 boutons,
    # l'affichage du score et du nombre de vie.
    def __init__(self, hi):
        self.Hi = hi # Valeur de la hauteur du canvas

        self.w = Tk() # Création de la fenêtre 
        self.w.geometry('2400x1000') # Dimension de la fenêtre
        self.w.title('Space Invaders')
        
        self.canevas = Canvas(self.w, width = 1200, height = self.Hi,  bg ='white')  # Dimension du canvas
        self.canevas.grid(row = 1, column = 0)
        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "D")

        # Ces quatres lignes gèrent la position en profondeur des différents élèments du canvas
        self.canevas.tag_raise("A")     # niveau du vaisseau
        self.canevas.tag_raise("B")     # niveau des aliens 
        self.canevas.tag_raise("C")     # niveau des balles
        self.canevas.tag_lower("D")     # niveau profondeur le plus haut, definit le niveau du fond du canvas (photo)
              
        #Affichage du score
        self.score = Label(self.w, text = 'score : 0', fg = 'black')
        self.score.grid(row = 0, column = 0, sticky = 'nw')
        self.score.configure(font = 20)

        #Affichage des vies
        self.labelLives = Label(self.w, text = "vie restantes : 3", fg = 'black')
        self.labelLives.grid(row = 0, column = 0, sticky = 'ne')
        self.labelLives.configure(font = 20)
        
        #Création du bouton "Quitter"
        self.buttonLeave = Button(self.w, text = 'Quitter', command = self.w.destroy)
        self.buttonLeave.grid(row = 1, column = 1, sticky = 's')
        self.buttonLeave.configure(font = 20)

        #Création du bouton "Nouvelle partie"
        self.buttonReload = Button(self.w, text = 'Nouvelle partie', command = '')
        self.buttonReload.grid(row = 1, column = 1)
        self.buttonReload.configure(font = 20)



    
    def Mainloop(self):
        self.w.mainloop()