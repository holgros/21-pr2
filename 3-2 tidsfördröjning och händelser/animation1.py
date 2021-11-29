from tkinter import *
from time import *
root = Tk()
canv = Canvas(root, bg="blue", height=250, width=300)
canv.pack()
def update_arc():
    open = False
    for i in range(10):
        canv.delete("all")  # radera allt från canvasen
        if (open):
            arc = canv.create_arc(10, 10, 140, 210, start=10, extent=340, fill="yellow")    # skapa en cirkelbåge 340 grader
        else:
            arc = canv.create_arc(10, 10, 140, 210, start=30, extent=300, fill="yellow")    # liknande som ovan, men med 300 graders cirkelbåge
        canv.update()   # ritar canvas igen
        open = not open # växla mellan öppen och stängd mun
        root.after(500) # vänta en halv sekund, dvs. 500 millisekunder
    root.destroy()      # stäng ner fönstret efter loopen körts 10 gånger
update_arc()
root.mainloop()
