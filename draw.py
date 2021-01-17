from window import Window
from random import randint

class Draw(Window):
    def __init__(self, hi):
        Window.__init__(self, hi)
        self.stop = 0
        self.bulletsShips = [self.canevas.create_line(1249, 649, 1250, 650)]
        self.bulletsAlien = [self.canevas.create_line(1249, 649, 1250, 650)]
    
    def drawAliens(self):
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        line5 = []

        for i in range(8):
            line1.append(self.canevas.create_rectangle(120*i+50, 10, 120*i+120, 40, fill = "red", tags = "B"))
            line2.append(self.canevas.create_oval(120*i+50, 50, 120*i+120, 80, fill = "yellow", tags = "B"))
            line3.append(self.canevas.create_oval(120*i+50, 90, 120*i+120, 120, fill = "blue", tags = "B"))
            line4.append(self.canevas.create_rectangle(120*i+50, 130, 120*i+120, 160, fill = "magenta", tags = "B"))
            line5.append(self.canevas.create_oval(120*i+50, 170, 120*i+120, 200, fill = "black", tags = "B"))

        self.Aliens = [line1 ,line2 ,line3 ,line4 ,line5]
        self.Aliens2 = line1 + line2 + line3 + line4 +line5
    
    def drawSpaceships(self):
        self.spaceships = self.canevas.create_rectangle(561, 930, 641, 1000, fill = "green", tags = "A")

        return self.spaceships


    def createBuletsShips(self, event):
        if len(self.bulletsShips) > 1:
            self.bulletsShips = self.bulletsShips
            
        else:
            bullet = self.canevas.create_line((self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1], (self.canevas.coords(self.spaceships)[0]+self.canevas.coords(self.spaceships)[2])/2, self.canevas.coords(self.spaceships)[1] + 40, fill = "green", width = 10,tags = "C")
            self.bulletsShips.append(bullet)


    def createBuletsAliens(self):
        if self.stop == 1:
            return -1
        
        else:
            r = randint(0, len(self.Aliens2) - 1)

            self.bulletAlien = self.canevas.create_line((self.canevas.coords(self.Aliens2[r])[0] + self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3], (self.canevas.coords(self.Aliens2[r])[0]+self.canevas.coords(self.Aliens2[r])[2])/2, self.canevas.coords(self.Aliens2[r])[3] + 40, fill = "black", tags = "E", width = 10)
            self.bulletsAlien.append(self.bulletAlien)
            self.w.after(2500, self.createBuletsAliens)
        

    def drawBarricades(self):
        Barricade1 = []
        Barricade2 = []
        Barricade3 = []

        for line in range(2):
            for col in range(6):
                Barricade1.append(self.canevas.create_rectangle(50 + col*50, self.Hi - 200  + line*50, 100 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade2.append(self.canevas.create_rectangle(450 + col*50, self.Hi - 200  + line*50, 500 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))
                Barricade3.append(self.canevas.create_rectangle(850 + col*50, self.Hi - 200  + line*50, 900 + col*50, self.Hi - 150 + line*50, fill = "grey", outline = "black"))

        return Barricade1, Barricade2, Barricade3