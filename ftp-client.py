import socket
import os

HOST = 'localhost'
PORT = 6666

while True:
    try:
        request = input('>')
        if request == "":
            request = "pwd"
    except:
        break
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
    except:
        break   
    sock.send(request.encode())
    try:
        response = sock.recv(1024).decode()
    except:
        break
    if response == 'exit' or response == 'cstop':
        break
    print(response)
    
    sock.close()
