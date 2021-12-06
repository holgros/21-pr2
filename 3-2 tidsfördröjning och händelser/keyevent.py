from tkinter import *
def keyup(e):
    print('knappsläppning:', e.char)
def keydown(e):
    print('knapptryckning:', e.char)
root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()
