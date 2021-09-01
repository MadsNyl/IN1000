class Celle:
    def __init__(self):
        self.levende = False
    
    def settDoed(self):
        self.levende = False
    
    def settLevende(self):
        self.levende = True
    
    def erLevende(self):
        if self.levende:
            return True
        else:
            return False
    
    def tegnPresentasjon(self):
        if self.levende:
            return 'o'
        else:
            return '.'