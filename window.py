from tkinter import Tk ,Label, Button, Canvas, PhotoImage

class Window:
    def __init__(self, hi):
        self.Hi = hi

        self.w = Tk()     
        self.w.geometry('2400x1200')
        self.w.title('Space Invaders')
        
        self.canevas = Canvas(self.w, width = 1200, height = self.Hi,  bg ='white')  
        self.canevas.grid(row = 1, column = 0)
        self.photo = PhotoImage(file="jean-pierre.gif")
        self.item = self.canevas.create_image(600, 500, image = self.photo, tags = "D")
        self.canevas.tag_raise("A")     # Ces quatres lignes gèrent la position en profondeur des différents élèments du
        self.canevas.tag_raise("B")     # Canvas
        self.canevas.tag_raise("C")
        self.canevas.tag_lower("D")
              

        self.score = Label(self.w, text = 'score : 0', fg = 'black')
        self.score.grid(row = 0, column = 0, sticky = 'nw')
        self.score.configure(font = 20)

        self.labelLives = Label(self.w, text = "vie restantes : 3", fg = 'black')
        self.labelLives.grid(row = 0, column = 0, sticky = 'ne')
        self.labelLives.configure(font = 20)
        

        self.buttonLeave = Button(self.w, text = 'Quitter', command = self.w.destroy)
        self.buttonLeave.grid(row = 1, column = 1, sticky = 's')
        self.buttonLeave.configure(font = 20)

        self.buttonReload = Button(self.w, text = 'Nouvelle partie', command = '')
        self.buttonReload.grid(row = 1, column = 1)
        self.buttonReload.configure(font = 20)



    
    def Mainloop(self):
        self.w.mainloop()