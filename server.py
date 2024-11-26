import socket
import thread
from threading import Thread

print('Im server')
server = socket.socket()
server.bind(('localhost', 5004))
server.listen()




def on_new_client(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('message from client:'+str(data))
        status_send='OK 200'
        if str(data) == 'hi':
            status_send='Im good!'
        if str(data) == 'how are you?':
            status_send='Fine!'
        conn.send(status_send.encode())
    conn.close()



while True:
   conn, addr = server.accept()
   print('Clien on:'+str(addr))
   t=Thread(target=on_new_client, args=(conn, addr))
   t.start()
   #thread.start_new_thread(on_new_client,(conn,addr))
