from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
    
    def lesFraFil(self, filnavn):
        with open(filnavn, 'r') as f:
            for linje in f:
                linje = linje.strip().split(';')
                sang = Sang(linje[0], linje[1])
                self._sanger.append(sang)
        
    
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)
    
    def spillSang(self, sang):
        if sang in self._sanger:
            print(f'Spiller av {sang}')
        else:
            print('Kunne ikke finne sangen i listen')
    
    def spillAlle(self):
        for sang in self._sanger:
            self.spillSang(sang)
    
    def finnSang(self, tittel):
        if tittel in self._sanger:
            return tittel
    
    def hentArtistUtvalg(self, artistnavn):
        pass

spilleliste = Spilleliste('hey')

musikkFil = 'Oblig7 - sang/musikk.txt'

spilleliste.leggTilSang('work')
spilleliste.leggTilSang('jude')
spilleliste.leggTilSang('work')

print(spilleliste.finnSang('jude'))




