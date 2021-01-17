
## Importation des bibliothéques ##
from move import Move
from draw import Draw

from tkinter import Label, Button, PhotoImage


## Classes ##
class Game(Move):
    # Classe gérant tout ce qui concerne le jeu pure telle que les hitboxs, le score, les conditions de victoire et de 
    # défaite.
    # Cette classe comporte 7 méthodes, init comme dans toutes nos classes où l'on apelle les différentes méthodes des
    # classes précédentes dont nous avons besoin et où nous récupérons toues les variables nécessaire gâce aux propriétés
    # d'héridié des classes.
    # Les 6 autres méthodes sont décrites à l'aide d'un commentaire sous chacunes d'entre elles.

    def __init__(self, hi, dx, dy, t):
        Move.__init__(self, hi, dx, dy, t)
        Move.moveAliens(self)
        Move.moveSpaceships(self)
        Move.moveBulet2(self)
        Move.moveBulet(self)
        Move.moveBuletAliens(self)
        self.lives = 3
        self.scoring = 0
        

    def hitBox(self):
        # Cette méthode gère les collisions entre les différents éléments du Canvas.
        # Pour ce faire, elle vérifie que les coordonées des éléments censés intéragir entre concordent, si c'est le cas,
        # les deux éléments sont détruits sur le canvas et dans leurs listes respectives.
        # Afin de vérifier constemment si des éléments rentrenet en collisions, cette fonction s'apelle de maniére 
        # récursive grâce à la méthode tkinter .after() 
        # La méthode cesse sa récursivité lorsque le compteur self.cLoose passe à 1. Le compteur peut changer d'état lorsque
        # les aliens arrivent au niveau du vaisseau ou lorsque le nombre de vies tombe à 0.
    
        if self.cLoose == 1:
            self.Defeat()
            return -1
        
        else:
            if self.canevas.coords(self.bulletsShips[-1])[1] < 0:
                    self.canevas.delete(self.bulletsShips[-1])
                    self.bulletsShips.pop(-1)
            
            for line in self.Aliens:
                for alien in line:
                    if self.canevas.coords(self.bulletsShips[-1])[1] < self.canevas.coords(alien)[3]   and self.canevas.coords(self.bulletsShips[-1])[3] > self.canevas.coords(alien)[1]   and self.canevas.coords(self.bulletsShips[-1])[0] < self.canevas.coords(alien)[2]   and self.canevas.coords(self.bulletsShips[-1])[2] > self.canevas.coords(alien)[0]:
                        line.remove(alien)
                        if len(line) == 0:
                            del self.Aliens[self.Aliens.index(line)]
                            
                        self.Aliens2.remove(alien)
                        self.canevas.delete(alien)

                        self.scoring = self.scoring + 100
                        self.Scoring()
        
                        self.canevas.delete(self.bulletsShips[-1])
                        self.bulletsShips.pop(-1)

                        if len(self.Aliens2) == self.aliensNumber/2:
                            self.dx = 1.5*self.dx

                        if len(self.Aliens2) == 0:
                            self.Win()

            for bullet in self.bulletsAlien:
                if self.canevas.coords(bullet)[3] > self.canevas.coords(self.spaceships)[1]   and self.canevas.coords(bullet)[1] < self.canevas.coords(self.spaceships)[3]   and self.canevas.coords(bullet)[0] < self.canevas.coords(self.spaceships)[2]   and self.canevas.coords(bullet)[2] > self.canevas.coords(self.spaceships)[0]:
                    self.lives -= 1
                    self.printLives = "vie restantes: ", str(self.lives)
                    if self.lives == 0:
                        self.Scoring
                        self.Defeat()
                    
                    self.labelLives.configure (text = "".join(self.printLives))
                    
                    self.canevas.delete(self.bulletsAlien[-1])
                    self.bulletsAlien.pop(-1)

            if len(self.Barricades) != 0:
                for barricade in self.Barricades:
                    if self.canevas.coords(self.bulletsShips[-1])[1] < self.canevas.coords(barricade)[3]   and self.canevas.coords(self.bulletsShips[-1])[3] > self.canevas.coords(barricade)[1]   and self.canevas.coords(self.bulletsShips[-1])[0] < self.canevas.coords(barricade)[2]   and self.canevas.coords(self.bulletsShips[-1])[2] > self.canevas.coords(barricade)[0]:
                        if self.canevas.itemcget(barricade, "fill") == "red":
                            self.canevas.delete(barricade)
                            self.Barricades.remove(barricade)
                            
                            self.canevas.delete(self.bulletsShips[-1])
                            self.bulletsShips.pop(-1)
                            
                            break

                        self.canevas.itemconfigure(barricade, fill = "red")

                        self.canevas.delete(self.bulletsShips[-1])
                        self.bulletsShips.pop(-1)
                        

                    if self.canevas.coords(self.bulletsAlien[-1])[3] > self.canevas.coords(barricade)[1]   and self.canevas.coords(self.bulletsAlien[-1])[1] < self.canevas.coords(barricade)[3]   and self.canevas.coords(self.bulletsAlien[-1])[0] < self.canevas.coords(barricade)[2]   and self.canevas.coords(self.bulletsAlien[-1])[2] > self.canevas.coords(barricade)[0]:
                        self.canevas.delete(barricade)
                        self.Barricades.remove(barricade)

                        self.canevas.delete(self.bulletsAlien[-1])
                        self.bulletsAlien.pop(-1)
            
            self.w.after(self.t, self.hitBox)

    
    def Scoring(self):
        # Cette méthode sert à afficher le score en cours de partie.
        # Le score est stocké dans la variables self.scoring. Elle est initialisée à 0 dans l'init de la classe Game et
        # augmente de 100 à chaque fois qu'un alien est détruit.
        # La méthode est appelée à chaque fois qu'un alien est détruit (ligne 67), lorsque l'utilisateur tombe à court de 
        # vies (ligne 83) et lorsqu'on relance la partie(ligne 164).
           
        self.printScore = "score :", str(self.scoring)
        self.score.configure(text = "".join(self.printScore))


    def Defeat(self):
        # Cette méthode est utilisée pour afficher le texte en cas de défaites dans un Label créé au moment de l'appel de
        # la méthode et pour détruire le vaiseau et pour arrêter
        # le jeu. 
        # Pour ce faire on donne la valeure 1 au compteur self.stop, or lorsque ce compteur est 1, toutes les méthodes
        # qui faisaient bouger les différents éléments du jeu retourne -1 et donc arrêtent leur récursivité. 
        # Elle est appelée lorsque l'utilisateur tombe à court de vie (ligne 84) et lorsqu'un des aliens arrive à la même
        # ordonnée que le vaisseau(classe Move ligne 46 + classe Game ligne 56). 
        
        defeatTxt = "Oh niiooon, vous avez perdu. Votre score est de: ", str(self.scoring)

        self.canevas.delete(self.spaceships)      # Destruction du vaisseau
        
        self.labelDefeat = Label(self.w, text = "".join(defeatTxt), fg = 'black')
        self.labelDefeat.grid(row = 1, column = 0)
        self.labelDefeat.configure(font = 20)
        
        self.stop = 1
        self.cLoose = 1                           # Compteur utilisée dans la méthode reload afin de détruire le bon label en fonction de si le joueur a gagnè ou perdu.

        self.buttonReload["command"] = self.Reload


    def Win(self):
        # Tout comme la méthode defeat cette méthode arrête le jeu en donnant au compteur self.stop la valeure 1. À la 
        # différence de la méthode Defeat, la méthode Win affiche un texte de victoire au lieu d'un texte de défaite 
        # dans un Label créé au moment de l'appel de la méthode.
        # Cette méthode est appelée lorsque la longeur la liste contenant les aliens self.Aliens2 est nul (ligne 75).

        winTxt = "Wouhouuu, vous avez obtenu le score maximal: ", str(self.scoring)

        self.labelWin = Label(self.w, text = "".join(winTxt), fg = 'black')
        self.labelWin.grid(row = 1, column = 0)
        self.labelWin.configure(font = 20)

        self.stop = 1
        
        self.buttonReload["command"] = self.Reload


    def Reload(self):
        # Cette méthode n'est pas encore totalement fonctionnel, elle a pour but de préparer une nouvelle partie lorsque
        # l'utilisateur vient d'en terminer une (pas encore de système de niveaux) 
        # Pour ce faire elle nettoie le canvas puis recrée les différents éléments tel que les aliens ou les barricades.
        # Elle crée ensuite un  bouton qui lorsqu'on appuie dessus apelle la méthode reMove qui n'est pas non plus fini.
        # Cette méthode est appelé lorsque l'utilisateur appuie sur le boutton self.buttonReload.

        self.canevas.delete(all)
        
        self.scoring = 0
        self.Scoring()
        
        self.lives = 3
        self.printLives = "vie restantes: ", str(self.lives)
        
        if self.cLoose == 1:            # Conditions obligatoires pour pas que le programme cherche à détuire un Label innexistant
            self.labelDefeat.destroy()
        else:
            self.labelWin.destroy()

        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "D")

        self.labelHelp = Label(self.w, text = "Etes vous prêt à jouer?", fg = 'black')
        self.labelHelp.grid(row = 1, column = 0, sticky = "n")
        self.labelHelp.configure(font = 20)

        self.cLoose = 0
        self.stop = 0
        
        Draw.drawAliens(self)
        (self.Barricades1, self.Barricades2, self.Barricades3) = Draw.drawBarricades(self)
        self.Barricades = self.Barricades1 + self.Barricades2 + self.Barricades3
        Draw.drawSpaceships(self)

        self.buttonYes = Button(self.w, text = "oui", command = self.reMove)
        self.buttonYes.grid(row = 1, column = 0)
        self.buttonYes.configure(font = 20)

        
    def reMove(self):
        # Cette méthode est en court de finition.
        # Lorsqu'elle est appelée, elle détruit le boutton servant à confirmer que le joueur est prêt à commencer une
        # nouvelle partie et le Label self.LabelHelp
        # La méthode n'est cepandante pas fonctionnel car lors de son appel, les aliens ne ce déplacent pas et tirent
        # deux fois plus de balles que ce qu'ils devraient tirer normalement.

        self.buttonYes["command"] = ""
        self.buttonYes.destroy()
        self.labelHelp.destroy()
        self.hitBox()
        

        Move.moveAliens(self)
        Move.moveSpaceships(self)
        Move.moveBulet2(self)
        Move.moveBulet(self)
        Move.moveBuletAliens(self)

        Draw.createBuletsAliens(self)

        

    
            
    
       

    
   

           

