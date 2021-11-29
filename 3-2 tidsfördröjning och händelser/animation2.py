from tkinter import *
from time import *
root = Tk()
canv = Canvas(root, height=250, width=300, bg="blue")
canv.pack()
def update_circle():
    x0 = 0
    rightwards = True
    for i in range(1000):
        if x0 > 300 or x0 < 0:
            rightwards = not rightwards # växlar mellan att förflytta sig åt höger och åt vänster
        # uppdatera cirkelns koordinater
        if rightwards:
            x0 = x0 + 10
        else:
            x0 = x0 - 10
        canv.delete("all")  # radera allt på canvas
        oval = canv.create_oval(x0, 100, x0+50, 150, fill="red")    # skapa en ny cirkel: x0 är positionen i x-led, 100 är position i y-led
        canv.update()       # rita om canvas
        root.after(100)     # vänta en tiondels sekund innan vi kör loopen igen
    root.destroy()          # stäng fönstet efter att loopen körts 1000 ggr, dvs. efter 100 sekunder
update_circle()
root.mainloop()
