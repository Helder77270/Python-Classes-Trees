class ArbreBinaire:
    value = 0
    noeudGauche = 0
    noeudDroit = 0
    def __init__(self):
        self.value = 0

    def getValue(self):
        return self.value
        
    def setValue(self,val):
        self.value = val

bernard = ArbreBinaire()
bernard.setValue(1)

print(bernard.getValue())