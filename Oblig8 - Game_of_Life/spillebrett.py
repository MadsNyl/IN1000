from celle import Celle
import random

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self.generasjon = 0
        self.brett = []
    
    def tegnBrett(self):
        for rader in range(self._rader):
            ny_rad = []
            for kolonne in range(self._kolonner):
                celle = Celle()
                ny_rad.append(celle.tegnPresentasjon())
            self.brett.append(ny_rad)
        for linje in self.brett:
            print(linje)

    def _generer(self):
        for rader in range(self._rader):
            ny_rad = []
            for kolonne in range(self._kolonner):
                celle = Celle()
                if random.randint(1, 3) == 1:
                    celle.settLevende()
                ny_rad.append(celle.tegnPresentasjon())
            self.brett.append(ny_rad)
        for linje in self.brett:
            print(linje)

    def finnNabo(self, rad, kolonne):
        pass
