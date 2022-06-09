import socket
import json
import random
# def search_for_new_devices():
#     msg = \
#         'M-SEARCH * HTTP/1.1\r\n' \
#         'HOST:239.255.255.250:1982\r\n' \
#         'ST:wifi_bulb\r\n' \
#         'MX:2\r\n' \
#         'MAN:"ssdp:discover"\r\n' \
#         '\r\n'
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
#     sock.sendto(msg.encode(), ('239.255.255.250', 1982))
#     print("data sent");
#     try:
#         while True:
#             print("true")
#             data, addr = sock.recvfrom(65507)
#             print(addr, data)
#     except socket.timeout:
#         pass

# search_for_new_devices()
msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:239.255.255.250:1982\r\n' \
        'ST:wifi_bulb\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n' \
        '\r\n'

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
# sock.sendto(msg.encode(), ('239.255.255.250', 1982))
#
# while True:
#     print(sock.recv(1024))

#
def set_music(conn, ip, port):
    data = json.dumps({
        "id": random.randint(0, 1000),
        "method": "set_music",
        "params": [1, ip, port]
    }) + "\r\n"
    conn.sendall(data.encode())


connection1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection1.connect(("192.168.0.17", 55443))
connection2.connect(("192.168.0.22", 55443))

# set_music(connection1, "192.168.0.14", 55432)
# set_music(connection2, "192.168.0.14", 55432)
# def connect(ip, port):
#     connection.connect(ip, port)
#     print("connected to %:%" % (ip, port))

