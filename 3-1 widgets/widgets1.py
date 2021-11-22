'''
from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Hej världen!\nHur är läget?")
label.pack()
root.mainloop()
'''

from tkinter import *   # importera alla metoder i Pythons inbyggda GUI-ramverk Tkinter
root = Tk()             # skapa ett rot-objekt
# här behandlas fönstret som ska visas
img = PhotoImage(file='./3-1 widgets/bild.gif')
label = Label(image=img)
label.pack()
# visa fönstret och håll programmet vid liv tills man stänger fönstret
root.mainloop()
