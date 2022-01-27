from socket import *
def start_server():
    s = socket()            # Skapa ett socket-objekt
    host = "10.32.47.8"     # ändra till din egen IP-adress eller till localhost
    port = 12345            # på port 12345.
    s.bind((host, port))    # Konfigurera socket-objektet.
    s.listen()              # Vänta på att klient ansluter.
    return s
s = start_server()
while True:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, addr = s.accept()     # När en klient ansluter
    print("En klient anslöt från adressen", addr)
    msg = "Servern säger hej till klienten! Hur mår du idag?"
    b = msg.encode("utf-16")    # Gör om meddelandet till bytekod
    conn.send(b)                # Skicka meddelandet till klienten
    print("Väntar på meddelande från klienten...")
    b = conn.recv(1024)         # Ta emot ett meddelande från klienten
    msg = b.decode("utf-16")    # Gör om från bytekod till vanlig text
    print(msg)
    conn.close()                # Stäng anslutningen till klienten
