import json
import random
import socket


class Bulb:

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        self.connection.connect(self.ip, self.port)
        print("connected to %:%" % (self.ip, self.port))

    def set_music(self, ip, port):
        data = json.dumps({
            "id": random.randint(0, 1000),
            "method": "set_music",
            "params": [1, ip, port]
        }) + "\r\n"
        self.connection.sendall(data.encode())
