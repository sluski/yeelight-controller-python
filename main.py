import json
import socket

def search_for_new_devices():
    msg = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'HOST:239.255.255.250:1982\r\n' \
        'ST:wifi_bulb\r\n' \
        'MX:2\r\n' \
        'MAN:"ssdp:discover"\r\n' \
        '\r\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.sendto(msg.encode(), ('239.255.255.250', 1982))
    try:
        while True:
            data, addr = sock.recvfrom(65507)
            print(addr, data)
    except socket.timeout:
        pass



search_for_new_devices()
# bulbSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
# def connect(ip, port):
#     bulbSocket.connect((ip, port))
#     print("Connected to %s:%d" % (ip, port))
#
#
# def disconnect():
#     bulbSocket.close();
#     print("Disconnected");
#
#
# def send(data):
#     bulbSocket.sendall(data.encode())
#
#
# def change_color(red, green, blue):
#     data = json.dumps({
#         "id": 1,
#         "method": "set_rgb",
#         "params": [red*65536 + green*256 + blue, "smooth", 500]
#     }) + "\r\n"
#     send(data)
#
#
# connect("192.168.0.17", 55443)
#
# disconnect();
