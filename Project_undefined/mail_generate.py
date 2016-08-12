# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-08-11 22:50:43
# @Last Modified by:   boyac
# @Last Modified time: 2016-08-11 23:53:18

# using decorators to add tags inside mails

def tagit(tag='p'):
	def deco(func):
		def new_func(title,txt):
			print '<'+tag+'>' + txt + '</'+tag+'>'
			print '#' + ' ' + title 
			print '-' + ' ' + txt
		return new_func
	return deco


def mail(tag='p'):
	def deco_(func):
		def new_func_(client_title, client, my_name, my_firm, suggest_stock, goal):
			print 'Hi {} {}, this is {} from {} calling.'.format(client_title, client, my_name, my_firm)
			print 'It is important, can we talk?'
			print 'I just got this report from our research team,'
			print 'they have initiated a buy on ''<'+tag+'>' + suggest_stock + '</'+tag+'>'
			print 'I remember that you were trying to save for {},'.format(goal)
			print 'and this struck me as a good fit for you.'


			print '''
			Hi {} {}, this is {} from {} calling.
			It is important, can we talk?
			I just got this report from our research team,'
			they have initiated a buy on <'+tag+'>' + suggest_stock + '</'+tag+'>
			I remember that you were trying to save for {},'
			and this struck me as a good fit for you.'''.format(client_title, client, my_name, my_firm, goal)

		return new_func_
	return deco_


@tagit(tag='h1')
def printer(title,txt):
	print txt


@mail(tag='b')
def mailer(client_title, client, my_name, my_firm, suggest_stock, goal):
	print client



if __name__ == '__main__':
	#print printer('pydata','use python 2.7')
	print mailer('Mr.','Couvreur', 'Boya Chiou', '<Company_NAME>', 'BuyMe.Inc', '$1 billion for retirement')
	
# Output	
'''
Hi Mr. Couvreur, this is Boya Chiou from <Company_NAME> calling.
It is important, can we talk?
I just got this report from our research team,
they have initiated a buy on <b>BuyMe.Inc</b>
I remember that you were trying to save for $1 billion for retirement,
and this struck me as a good fit for you.

			Hi Mr. Couvreur, this is Boya Chiou from <Company_NAME> calling.
			It is important, can we talk?
			I just got this report from our research team,'
			they have initiated a buy on <'+tag+'>' + suggest_stock + '</'+tag+'>
			I remember that you were trying to save for $1 billion for retirement,'
			and this struck me as a good fit for you.
	'''
