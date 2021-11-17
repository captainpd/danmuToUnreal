import socket


class Sender():

    def __init__(self, host, port):
        self.ip_port = (host, port)
        self.sk = socket.socket()
        self.sk.bind((host, port))
        self.sk.listen(5)

        print('-----准备建立与UE4的连接-----')
        self.conn, self.address = self.sk.accept()
        print('-----连接成功: ' + str(self.ip_port) + '-----')

    def send_danmu(self, msg):
        self.conn.send(msg.encode())

    def send_admin(self, _msg):
        self.conn.send(_msg.encode())

    def send_json(self, _msg):
        self.conn.send(_msg.encode())

    def if_connected(self):
        ue_msg = self.conn.recv(1024)
        if ue_msg.decode() == 'exit':
            print('DISCONNECTED')
            return False
        else:
            return True
