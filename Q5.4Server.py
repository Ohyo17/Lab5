import socket
import tqdm
import os
import json
s = socket.socket()
print("Socket successfully created")

port = 8080

s.bind(('', port))
print("socket binded to " + str(port))

s.listen(5)
print("socket is listening")

BUFFER_SIZE = 4096

SEPERATOR = "<SEPERATOR>"

c, addr = s.accept()

receive = c.recv(BUFFER_SIZE).decode()
file, filesize = receive.split(SEPERATOR)

file = os.path.basename(file)

filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {file}", unit="B", unit_scale=True, unit_divisor=1024)

with open(file,"wb") as f:
	while True:
		bytes_read = c.recv(BUFFER_SIZE)
		if not bytes_read:
			break
		f.write(bytes_read)
		progress.update(len(bytes_read))

c.close()
s.close()
