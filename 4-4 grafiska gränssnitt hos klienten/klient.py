# Börja med att ansluta och ta emot välkomstmeddelandet från servern
from socket import *
def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
conn = connect_to_server()
b = conn.recv(1024)
msg = b.decode('utf-16')
print(msg)

# Bygg sedan ett grafiskt gränssnitt med ett textinmatningsfält och en knapp som skickar meddelande till servern
from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
lbl = Label(root)
lbl.pack()
b = Button(root, text ="Skicka")
def click_handler(self):
    msg = e.get()
    b = msg.encode("utf-16")
    conn.send(b)
b.bind("<Button-1>", click_handler)
b.pack()

# Definiera sedan trådens funktion och starta tråden och det grafiska gränssnittet.
def receiver_thread():
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        lbl["text"] = msg
from _thread import *
start_new_thread(receiver_thread, ())
root.mainloop()

'''
Fortsättning:
- Se till att alla meddelanden (inte bara det senaste) syns i fönstret
- Låt användare ange sina namn och meddela vem som skriver till alla klienter
'''