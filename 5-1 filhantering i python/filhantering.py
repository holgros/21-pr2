# skriv tre rader i en fil
f = open("exempel.txt", "a")    # "a" står för "append", dvs. skriva utan att radera befintlig text
for i in range(3):
    text = "Skriver siffran " + str(i) + "\n"   # "\n" står för ny rad
    f.write(text)

# öppna och läs fil
f = open("exempel.txt", "r")    # "r" står för read, dvs. läsa
print(f.read())

# stäng fil - görs automatiskt när programmet avslutas, men bra att göra så att det inte blir konflikter under programmets gång
f.close()

# skriv över filens innehåll
f = open("exempel.txt", "w")    # "w" står för "write", dvs. skriv över allt innehåll
f.write("Skriver över all text!")
# läs filen igen och kolla att innehållet skrivits över
f = open("exempel.txt", "r")
print(f.read())
f.close()

# hantera modulen os, som bl.a. kan skapa och radera mappar
import os
try:
    os.mkdir("undermapp")
except: # blir fel ifall t.ex. mappen redan finns
    pass
# öppna fil i undermapp
f = open("undermapp/annat_exempel.txt", "a")
f.write("Skriver till textfil i undermapp")
f.close()   # OBS - måste stänga innan den raderas
os.remove("undermapp/annat_exempel.txt")    # ta bort fil
os.rmdir("undermapp")