# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-05-11 00:25:24
# @Last Modified by:   boyac
# @Last Modified time: 2016-05-11 00:37:23
import socket

def Main():
	host = '127.0.0.1'
	port = 5001 # a port different from our server

	server = ('127.0.0.1', 5000) # server of data we are sending to

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	message = raw_input('-> ')
	while message != 'q':
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print 'Recieved from server: ' + str(data)
		message = raw_input('-> ')
	s.close()

if __name__ == '__main__':
	Main()
