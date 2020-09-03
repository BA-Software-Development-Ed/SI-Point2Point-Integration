import socket
import sys

try:
    message = sys.argv[1]
except:
    message = 'default message'

bytesToSend = str.encode(message)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
response = msgFromServer[0].decode('utf-8')

print(response)
