import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is our message. It will be sent all at once'

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()