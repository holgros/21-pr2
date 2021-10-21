# DEMO ÄRVA METODER FRÅN FLERA SUPERKLASSER
class Motorfordon:  # superklass
    def starta(self):
        print("Vroom!")
class Fyrhjuling:   # också superklass
    def rulla(self):
        print("Rullar!")
class Bil(Motorfordon, Fyrhjuling): # subklassy, som ärver från båda superklasserna
    pass
b = Bil()   
b.starta()  # Vroom!
b.rulla()   # Rullar!
print(isinstance(b, Bil) and isinstance(b, Motorfordon))	# True
