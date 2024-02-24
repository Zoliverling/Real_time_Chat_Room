import socket
from ChatServer import chatServer
from singleChatServer import chatServer as singleChat


class serverStarter():
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 8000
        self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_server.bind((self.host, self.port))
        self.sock_server.listen(5)
        print("Connection Started")
        conn, addr = self.sock_server.accept()
        self.data = conn.recv(2048)
        conn.close()
        self.sock_server.close()

    def initialServer(self):
        if self.data == "single":
            singleChat()
        elif self.data == "group":
            chatServer()


while 1:
    serverStarter()