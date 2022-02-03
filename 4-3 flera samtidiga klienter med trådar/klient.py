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
while True:
    msg = input("Skriv något meddelande till servern eller 'q' för att avbryta: ")
    if msg == "q":
        conn.close()
        break
    b = msg.encode("utf-16")
    conn.send(b)
    b = conn.recv(1024)
    msg = b.decode("utf-16")
    print(msg)
