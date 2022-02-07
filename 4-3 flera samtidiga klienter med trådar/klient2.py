# uppgradering av tidigare exempel - klient med trådar
from socket import *
def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
# funktion som körs i separat tråd för att lyssna på meddelanden från servern och skriva ut på konsolen
def listener_thread(conn):
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        print("\n"+msg)
conn = connect_to_server()
from _thread import *
start_new_thread(listener_thread, (conn, )) # startar en ny tråd som kör funktionen listener_thread
# samma som tidigare, men utan att input blockerar utskrift av meddelanden från servern
while True: # input skrivs och meddelanden skickas i huvudtråden
    msg = input("Skriv något meddelande till servern eller 'q' för att avbryta: ")
    if msg == "q":
        conn.close()
        break
    b = msg.encode("utf-16")
    conn.send(b)