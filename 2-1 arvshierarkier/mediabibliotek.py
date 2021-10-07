# implementera en arvshierarki
class Media:
    def __init__(self, titel):
        self.titel = titel
class Bok(Media):
    def __init__(self, titel, antalSidor):
        super().__init__(titel)
        self.antalSidor = antalSidor
class Ljudspår(Media):
    def __init__(self, titel, speltid):
        super().__init__(titel)
        self.speltid = speltid
class Film(Ljudspår):
    def __init__(self, titel, speltid, upplösning):
        super().__init__(titel, speltid)
        self.upplösning = upplösning

# testa implementationen
b = Bok("Bröderna Karamazov", 840)
print(b.titel)      # Bröderna Karamazov
print(b.antalSidor) # 840
if isinstance(b, Media) and isinstance(b, Bok): # True
    print("b är samtidigt av typen Media och Bok")
f = Film("De sju samurajerna", "3:27:02", "1080")
print(f.titel)      # De sju samurajerna
print(f.speltid)    # 3:27:02
print(f.upplösning) # 1080
if isinstance(f, Media) and isinstance(f, Ljudspår) and isinstance(f, Film):    # True
    print("f är samtidigt av typen Media, Ljudspår och Film")
