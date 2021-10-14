class Superclass:
    def hej(self):
        print("Hej från Super!")    # superklassen har en metod som heter "hej"
class Subclass(Superclass):
    def hej(self):  # metoden "hej" överskuggas ("overridas") i subklassen
        print("Hej från Sub!")
sup = Superclass()
sup.hej()   # Hej från Super!
sub = Subclass()
sub.hej()   # Hej från Sub!
