from celle import Celle
import random

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self.generasjon = 0
        self.brett = []
        self._generer()

    def tegnBrett(self):
        for linje in self.brett:
            for celle in linje:
                print(celle.tegnPresentasjon(), end="")
            print()
        antall_levende = self.finnAntallNaboer()
        print(f'Generasjon: {self.generasjon} - Antall levende celler: {antall_levende}')

    def _generer(self):
        for rader in range(self._rader):
            ny_rad = []
            for kolonne in range(self._kolonner):
                celle = Celle()
                if random.randint(1, 3) == 1:
                    celle.settLevende()
                ny_rad.append(celle)
            self.brett.append(ny_rad)
    
    def finnAntallNaboer(self):
        antall_levende = 0
        for linje in self.brett:
            for celle in linje:
                if celle.levende:
                    antall_levende += 1
        return antall_levende

    def finnNabo(self, rad, kolonne):
        nabo_liste = []
        if rad == 0:
            if kolonne == 0:
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                nabo_liste.append(ned_nabo)
                nedHøyre_nabo = self.brett[rad + 1][kolonne + 1]
                nabo_liste.append(nedHøyre_nabo)
            elif kolonne == self._kolonner - 1:
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                nedVenstre_nabo = self.brett[rad + 1][kolonne -1]
                nabo_liste.append(nedVenstre_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                nabo_liste.append(ned_nabo) 
            else:
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                nabo_liste.append(ned_nabo)
                nedVenstre_nabo = self.brett[rad + 1][kolonne -1]
                nabo_liste.append(nedVenstre_nabo)
                nedHøyre_nabo = self.brett[rad + 1][kolonne + 1]
                nabo_liste.append(nedHøyre_nabo)
        elif rad == self._rader - 1:
            if kolonne == 0:
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                topHøyre_nabo = self.brett[rad - 1][kolonne + 1]
                nabo_liste.append(topHøyre_nabo)
            elif kolonne == self._kolonner - 1:
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                topVenstre_nabo = self.brett[rad - 1][kolonne - 1]
                nabo_liste.append(topVenstre_nabo)
            else:
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                topVenstre_nabo = self.brett[rad - 1][kolonne - 1]
                nabo_liste.append(topVenstre_nabo)
                topHøyre_nabo = self.brett[rad - 1][kolonne + 1]
                nabo_liste.append(topHøyre_nabo)
        elif 1 <= rad <= self._rader - 2:
            if kolonne == 0:
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                nabo_liste.append(ned_nabo)
                nedHøyre_nabo = self.brett[rad + 1][kolonne + 1]
                nabo_liste.append(nedHøyre_nabo)
                topHøyre_nabo = self.brett[rad - 1][kolonne + 1]
                nabo_liste.append(topHøyre_nabo)
                
            elif kolonne == self._kolonner - 1:
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                topVenstre_nabo = self.brett[rad - 1][kolonne - 1]
                nabo_liste.append(topVenstre_nabo)
                nedVenstre_nabo = self.brett[rad + 1][kolonne -1]
                nabo_liste.append(nedVenstre_nabo)

            else:
                venstre_nabo = self.brett[rad][kolonne - 1]
                nabo_liste.append(venstre_nabo)
                høyre_nabo = self.brett[rad][kolonne + 1]
                nabo_liste.append(høyre_nabo)
                top_nabo = self.brett[rad - 1][kolonne]
                nabo_liste.append(top_nabo)
                ned_nabo = self.brett[rad + 1][kolonne]
                nabo_liste.append(ned_nabo)
                topVenstre_nabo = self.brett[rad - 1][kolonne - 1]
                nabo_liste.append(topVenstre_nabo)
                topHøyre_nabo = self.brett[rad - 1][kolonne + 1]
                nabo_liste.append(topHøyre_nabo)
                nedVenstre_nabo = self.brett[rad + 1][kolonne -1]
                nabo_liste.append(nedVenstre_nabo)
                nedHøyre_nabo = self.brett[rad + 1][kolonne + 1]
                nabo_liste.append(nedHøyre_nabo)

        return nabo_liste


    def oppdatering(self):
        bli_levende = []
        bli_død = []
        for rad_verdi, rad in enumerate(self.brett):
            for celle_verdi, celle in enumerate(rad):
                if celle.levende:
                    naboer = self.finnNabo(rad_verdi, celle_verdi)
                    i_live = 0
                    for nabo in naboer:
                        if nabo.levende:
                            i_live += 1
                    if i_live < 2:
                        bli_død.append(celle)
                    else:
                        bli_levende.append(celle)
                
                else:
                    naboer = self.finnNabo(rad_verdi, celle_verdi)
                    i_live = 0
                    for nabo in naboer:
                        if nabo.levende:
                            i_live += 1
                    if i_live == 3:
                        bli_levende.append(celle)
                    else:
                        bli_død.append(celle)

        
        for celle in bli_levende:
            celle.settLevende()
        print()
        for celle in bli_død:
            celle.settDoed()
        self.generasjon += 1


        
