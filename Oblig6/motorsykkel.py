class Motorsykkel:
    def __init__(self, merke, regnr, km):
        self.merke = merke
        self.regnr = regnr
        self.km = km
    
    def kjor(self, km):
        self.km += km
    
    def hentKilometerStand(self):
        self.kjor()
        self.totalKm = self.km 
    
    def skrivUt(self):
        print(self.merke)
        print(self.regnr)
        print(self.km)
