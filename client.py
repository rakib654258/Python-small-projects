import socket
import sys
import time

s=socket.socket()
host=input(str('Please enter the hostname of the server: '))
port = 8080
s.connect((host,port))
print('Connected to the server')
while True:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print('Server/Host: ',incoming_message)
    print('')
    message=input(str('>>'))
    message=message.encode()
    s.send(message)
    print('sent')
    print('')
