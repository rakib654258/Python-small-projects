import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print('Server will start on host: ',host)
port = 8080
s.bind((host,port))
print('')
print('Server done binding to host and port successfully')
print('')
print('Server is waiting to incoming connections')
print('')
s.listen(1)
connection,address=s.accept()
print(address,'Has connected to the server and is now online..')
print('')
while True:
    message=input(str('>>'))
    message=message.encode()
    connection.send(message)
    print('sent')
    print('')
    incoming_message=connection.recv(1024)
    incoming_message=incoming_message.decode()
    print('Client: ',incoming_message)
    print('')
