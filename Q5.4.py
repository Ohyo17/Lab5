import socket
import tqdm
import sys
import os
import json
SEPERATOR = "<SEPERATOR>"
BUFFER_SIZE = 4096

s=socket.socket()
host = '192.168.56.103'
port = 8080

print(f"[+] Connected to {host}:{port}")
s.connect((host,port))
print("[+]Connected")

filename = input("Enter filename:")
print("Filename:",filename)

filesize = os.path.getsize(filename)

s.send(f"{filename}{SEPERATOR}{filesize}".encode())

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename,"rb") as f:
	while True:
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break
		s.sendall(bytes_read)
		progress.update(len(bytes_read))

s.close()
