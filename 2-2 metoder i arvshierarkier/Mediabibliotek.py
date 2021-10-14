class Media:
    def __init__(self, titel):
        self.__titel = titel
    def getTitel(self):
        return self.__titel
class Bok(Media):
    def __init__(self, titel, antalSidor):
        super().__init__(titel)
        self.__antalSidor = antalSidor
    def getAntalSidor(self):
        return self.__antalSidor
class Ljudspår(Media):
    def __init__(self, titel, speltid):
        super().__init__(titel)
        self.__speltid = speltid
    def getSpeltid(self):
        return self.__speltid
class Film(Ljudspår):
    def __init__(self, titel, speltid, upplösning):
        super().__init__(titel, speltid)
        self.__upplösning = upplösning
    def getUpplösning(self):
        return self.__upplösning
b = Bok("Bröderna Karamazov", 840)
print(b.getTitel())      # Bröderna Karamazov
print(b.getAntalSidor()) # 840
f = Film("De sju samurajerna", "3:27:02", "1080")
print(f.getTitel())      # De sju samurajerna
print(f.getSpeltid())    # 3:27:02
print(f.getUpplösning()) # 1080