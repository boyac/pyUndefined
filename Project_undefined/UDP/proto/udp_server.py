import socket

host = '127.0.0.1'
port = 15515
clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsock.bind((host, port))
print "wait..."
while True:
  recv_msg, addr = clientsock.recvfrom(1024)
  print "Received ->", recv_msg
  break
