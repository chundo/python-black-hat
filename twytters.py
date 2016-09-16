#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TwitterAPI import TwitterAPI

	
def main():
	#SEARCH_TERM = 'sr_espana, @sr_espana'
	#buscar = raw_input('Ingrese busqueda: ')
	CONSUMER_KEY = 'tu-KEY'
	CONSUMER_SECRET = 'tu-SECRET'
	ACCESS_TOKEN_KEY = 'tu-TOKEN_KEY'
	ACCESS_TOKEN_SECRET = 'tu-TOKEN_SECRET'
	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

	print '# Cupones'
	print ' ___sr_espana_________'
	print '< pecademy >'
	print ' ------------'
	print '       \   ,__,'
	print '        \  (oo)____'
	print '           (__)    )\ '
	print '              ||--|| *'
	print '1 buscar, 2 filtrar'
	opcion = raw_input('Ingrese opcion: ')
	if opcion == '1':
		buscar()
	elif opcion == '2':
		filtrar()
	else:
		main()

def buscar():
	CONSUMER_KEY = 'tu'
	CONSUMER_SECRET = 'tu'
	ACCESS_TOKEN_KEY = 'tu-tu'
	ACCESS_TOKEN_SECRET = 'tu'
	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
	buscar = raw_input('Ingrese busqueda: ')	
	r = api.request('search/tweets', {'q':buscar})
	for item in r:
	    print(item['text'])
	    print('------------------------------------------------------------------------')

def filtrar():
	CONSUMER_KEY = 'tu'
	CONSUMER_SECRET = 'tu'
	ACCESS_TOKEN_KEY = '297410594-tu'
	ACCESS_TOKEN_SECRET = 'tu'
	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
	buscar = raw_input('Ingrese filtro: ')
	r = api.request('statuses/filter', {'locations':buscar})
	for item in r:
	    print(item)
	    print('------------------------------------------------------------------------')

main()



print                     	  ########                  #
print                      #################            #
print                   ######################         #
print                  #########################      #
print                ############################
print               ##############################
print               ###############################
print              ###############################
print              ##############################
print                              #    ########   #
print                 ##        ###        ####   ##
print                                      ###   ###
print                                    ####   ###
print               ####          ##########   ####
print               #######################   ####
print                 ####################   ####
print                  ##################  ####
print                    ############      ##
print                      ########        ###
print                      #########        #####
print                    ############      ######
print                   ########      #########
print                     #####       ########
print                       ###       #########
print                     ######    ############
print                     #######################
print                     #   #   ###  #   #   ##
print                     ########################
print                      ##     ##   ##     ##
print #                     http://metasploit.com


