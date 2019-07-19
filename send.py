import socket

UDP_IP = "10.1.1.128"
UDP_PORT = 5005
MESSAGE = "test"

print ("UDP target IP:"), UDP_IP
print ("UDP target port:"), UDP_PORT
print ("message:"), MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(str.encode(MESSAGE), (UDP_IP, UDP_PORT))