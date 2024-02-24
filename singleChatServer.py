import socket
import os
from _thread import *
import threading

class chatServer():
    def __init__(self):
        self.ServerSocket = socket.socket()
        self.host = '127.0.0.1'
        self.port = 8000
        self.ThreadCount = 0
        self.connect()

    def connect(self):
        try:
            self.ServerSocket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        print('Waitiing for a Connection..')
        self.ServerSocket.listen(5)
        self.clients = []
        self.index = 0
        threading._start_new_thread(self.new_clients, (self.ServerSocket, " "))

    def new_clients(self,server,y):
        while True:
            c,a = server.accept()
            self.clients.append(c)
            if len(self.clients) >2:
                c.send(b'The Space is Not for u')
                break
            else:
                threading._start_new_thread(self.threaded, (c, a))
            
    def threaded(self,con,ad):
        con.send(b'go ahead')
        while True:
            data = con.recv(4096)
            if not data: break
            if data == "exit": break

            client_msg = data.decode('utf-8')

            idx = self.get_index(con)

            index = 0
            for c in self.clients:
                index += 1
                if c != con:
                    mes =  "User" + str(index)+ " SAYS: " + client_msg + "\n"
                    c.send(str.encode(mes))


    # find the client index then remove from both lists(client name list and connection list)
        idx = self.get_index(con)
        del self.clients[idx]
        con.close()

    def get_index(self,sample):
        i = 0
        for c in self.clients:
            if c == sample:
                break
            i += 1
        return i
            

#    def run(self):
#        while True:
 #           cl,ad = self.ServerSocket.accept()
  #          start_new_thread(self.threaded, (cl,ad ))
   #         self.ThreadCount += 1
    #    self.ServerSocket.close()

if __name__ == "__main__":
    main = chatServer()
