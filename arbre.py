class TestArbreBinaire:
    value = 0
    noeudGauche = 0
    noeudDroit = 0
    def __init__(self):
        self.value = 0

    def getValue(self):
        return self.value
        
    def setValue(self,val):
        self.value = val

    def str(self):
        print("Noeud = " + str(self.value) + " noeud gauche = " + str(self.noeudGauche) + " noeud droit = " + str(self.noeudDroit))

bernard = TestArbreBinaire()
bernard.setValue(1)
bernard.str()
