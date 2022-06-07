import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_TTL, 20)
# sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_LOOP, 1)

sock.bind(('', 5004))

print("Listening: ");
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message: %s" % data)