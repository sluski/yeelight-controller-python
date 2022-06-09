import json
import random
import socket
import time


def calculate_color(red, green, blue):
    return red * 65536 + green * 256 + blue


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.0.14", 55432))
sock.listen()
print("Starting server")

conn, addr = sock.accept()
print(addr)

# while True:

    # data = json.dumps({
    #     "id": 1,
    #     "method": "set_rgb",
    #     "params": [calculate_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), "sudden", 30]
    # }) + "\r\n"
    # conn.sendall(data.encode())
    # time.sleep(0.3)




