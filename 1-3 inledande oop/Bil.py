class Bil:      # implementera klassen bil, dvs. en "form" som alla enskilda bilar skapas av
    def __init__(self, speed, brand):   # bilens konstruktor
        self.speed = speed
        self.brand = brand
    def honk(self):                     # en Bil-metod
        print("TUUT!!")
    def drive(self):                    # en till Bil-metod
        print("Bilen körs i", self.speed, "kilometer i timmen.")
bil1 = Bil(50, "Volvo")
bil1.honk()
bil1.drive()
bil2 = bil1             # variabeln bil2 "pekar" på samma objekt som bil1 - vi har alltså inte skapat något nytt objekt
bil2.speed = 70         # ändrar både bil1 och bil2
print(bil1.speed)       # 70