import socket

s = socket.socket()

port = 8889

s.connect(('192.168.56.103', port))

data = s.recv(2048)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
