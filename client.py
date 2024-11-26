import socket
import time

print('Im client')
client = socket.socket()
client.connect(('localhost', 5004))
message = input('Imput the message:')
while message !='exit':

    #time.sleep(2)
    client.send(message.encode())
    resp = client.recv(1024).decode()
    print('Response from server:'+resp)
    message = input('Imput the message:')

client.close()


