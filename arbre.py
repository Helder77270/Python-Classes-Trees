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

    def prefixe(self):
        if self.value == 0:
            return False
        else:
            print(self.value)

        
bernard = TestArbreBinaire()
bernard.setValue(1)
bernard.str()
bernard.prefixe()
