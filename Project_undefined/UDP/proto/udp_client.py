import socket

host = '127.0.0.1'
port = 15515
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Type message...'
send_msg = raw_input()
serversock.sendto(send_msg, (host, port))
