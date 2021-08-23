class Hund:
    def __init__(self, alder, vekt):
        self.alder = alder
        self.vekt = vekt
        self.metthet = 10
    
    def skrivUt(self):
        print(self.alder)
        print(self.vekt)
    
    def spring(self):
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1
    
    def spis(self, mat):
        self.metthet += int(mat)
        if self.metthet > 7:
            self.vekt += 1