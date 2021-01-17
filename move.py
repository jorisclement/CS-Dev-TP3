from draw import Draw


class Move(Draw):
    def __init__(self, hi, dx, dy, t):
        Draw.__init__(self, hi)
        Draw.drawAliens(self)
        self.aliensNumber = len(self.Aliens2)
        self.spaceships = Draw.drawSpaceships(self)
       
        Draw.createBuletsAliens(self)
        (self.Barricades1, self.Barricades2, self.Barricades3) = Draw.drawBarricades(self)
        self.Barricades = self.Barricades1 + self.Barricades2 + self.Barricades3
        
        self.dx = dx
        self.dy = dy
        self.t = t
        self.c = 0
        self.bounce = 0
        self.cLoose = 0
        

    def moveAliens(self):
        if self.stop == 1:
            return -1
        
        else:
            for line in self.Aliens:
                if self.canevas.coords(line[-1])[2] > 1200 and self.bounce == 0:     
                    self.dx = -self.dx
                    if self.dx < 0:
                        self.bounce = 1

                elif self.canevas.coords(line[0])[0] < 0 and self.bounce == 1:   
                    self.dx = -self.dx
                    self.c = 2     
                    if self.dx > 0:
                        self.bounce = 0

            if self.c == 2:
                self.canevas.move("B", 0, 50)
                self.c = 0

            for alien in self.Aliens2:
                if self.canevas.coords(alien)[3] >= self.canevas.coords(self.spaceships)[1]:
                   self.cLoose = 1

            self.canevas.move("B", self.dx, self.dy)        
            self.w.after(self.t, self.moveAliens)

    
    def right (self,event):
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[2] < 1200 : 
                self.canevas.move(self.spaceships,20,0)
            else :
                self.canevas.move(self.spaceships,0,0)
        
    
    def left (self,event):
        if self.stop == 1:
            return -1
        
        else:
            if self.canevas.coords(self.spaceships)[0] > 0:
                self.canevas.move(self.spaceships,-20,0)
            else :
                self.canevas.move(self.spaceships,0,0)


    def moveSpaceships(self):
        self.canevas.bind_all('<Right>', self.right)
        self.canevas.bind_all('<Left>', self.left)
        
        
    def moveBulet2(self):
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("C", 0, -20)
            self.w.after(self.t, self.moveBulet2)
            


    def moveBulet(self):
        self.canevas.bind_all('<space>', self.createBuletsShips)

    
    def moveBuletAliens(self):
        if self.stop == 1:
            return -1
        else:
            self.canevas.move("E", 0, 20)
            self.w.after(self.t, self.moveBuletAliens)