class Superclass:
    def hej(self):
        print("Hej från Super!")
class Subclass(Superclass):
    def hej(self, x):
        print("Hej från Sub!")
        print("input:", x)
sup = Superclass()
sup.hej()   # Hej från Super!
sub = Subclass()
sub.hej(2)   # Hej från Sub! \\ input: 2
sub.hej()   # FEL!

# Ett sidospår: statiska funktioner, som inte ingår i en klass, behöver inte argumentet "self"
def funktion():
    print("Det går!")
funktion()
