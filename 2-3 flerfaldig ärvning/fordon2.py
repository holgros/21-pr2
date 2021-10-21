# DEMO ÄRVA ATTRIBUT FRÅN FLERA SUPERKLASSER
class Motorfordon:  # superklass med konstruktor
    def __init__(self, max_speed):
        self.max_speed = max_speed
class Fyrhjuling:   # superklass med konstruktor
    def __init__(self, wheel_radius):
        self.wheel_radius = wheel_radius
class Bil(Motorfordon, Fyrhjuling): # subklass med konstruktor
    def __init__(self, max_speed, wheel_radius):    # behöver båda attributvärdena som inparametrar
        Motorfordon.__init__(self, max_speed)       # anropa ena superklassens konstruktor
        Fyrhjuling.__init__(self, wheel_radius)     # anropa andra superklassens konstruktor
b = Bil(120, 15)    # skapa en bil med max_speed=120 och wheel_radius=15
print(b.max_speed)      # 120
print(b.wheel_radius)   # 15
