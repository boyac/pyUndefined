# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-11 00:25:32
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-11 00:37:47
import socket

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket family, socket type
	s.bind((host, port)) # bind our socket to the port

	print 'Server Started.'
	while True:
		data, addr = s.recvfrom(1024) # buffer
		print 'message from: ' + str(addr)
		print 'from connect user: ' + str(data)
		data = str(data).upper()
		print 'sending: ' + str(data)
		s.sendto(data, addr)
	s.close()

if __name__ == '__main__':
	Main() # receiving data and sending data
