class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist
    
    def spill(self):
        print(f'Spiller av {self._tittel} av {self._artist}')

    def sjekkArtist(self, navn):
        # return true hvis ett eller flere av navnene finnes i _artist
        funnet = False
        navn = navn.lower()
        artist = self._artist.lower()
        liste_av_navn = navn.split()
        liste_av_artist = artist.split()
        for ord in liste_av_navn:
            if ord in liste_av_artist:
                funnet = True
                break
        return funnet
 
    def sjekkTittel(self, tittel):
        # return true hvis tittel er lik sangtittel
        org_tittel = self._tittel.lower()
        ny_tittel = tittel.lower()
        if org_tittel == ny_tittel:
            return True
        else:
            return False
    
    def sjekkArtistogTittel(self, navn, tittel):
        # return true hvis både artist og tittel er lik
        if self.sjekkArtist(navn) and self.sjekkTittel(tittel):
            return True
        else:
            return False 

sang = Sang('work', 'Rihanna and the boys')




