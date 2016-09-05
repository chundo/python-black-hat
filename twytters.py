#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TwitterAPI import TwitterAPI

	
def main():
	#SEARCH_TERM = 'sr_espana, @sr_espana'
	#buscar = raw_input('Ingrese busqueda: ')
	CONSUMER_KEY = '4knMbkyE8UPg9BRYGeQgcuJyt'
	CONSUMER_SECRET = 'isolgwWnQBH3FFwfJ2EkrF8KkEZ9m8OPiH5CywSFzhKzoSL5Jc'
	ACCESS_TOKEN_KEY = '297410594-Wdpr9p6lOJgGQJDOZegYL4bgvLONtWMV2JmtYTkm'
	ACCESS_TOKEN_SECRET = 'IXVzUOmyw7oYzFSvXc9hiyCMNkp7TZf6zAb7u4R3BGjkk'
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
	CONSUMER_KEY = '4knMbkyE8UPg9BRYGeQgcuJyt'
	CONSUMER_SECRET = 'isolgwWnQBH3FFwfJ2EkrF8KkEZ9m8OPiH5CywSFzhKzoSL5Jc'
	ACCESS_TOKEN_KEY = '297410594-Wdpr9p6lOJgGQJDOZegYL4bgvLONtWMV2JmtYTkm'
	ACCESS_TOKEN_SECRET = 'IXVzUOmyw7oYzFSvXc9hiyCMNkp7TZf6zAb7u4R3BGjkk'
	api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
	buscar = raw_input('Ingrese busqueda: ')	
	r = api.request('search/tweets', {'q':buscar})
	for item in r:
	    print(item['text'])
	    print('------------------------------------------------------------------------')

def filtrar():
	CONSUMER_KEY = '4knMbkyE8UPg9BRYGeQgcuJyt'
	CONSUMER_SECRET = 'isolgwWnQBH3FFwfJ2EkrF8KkEZ9m8OPiH5CywSFzhKzoSL5Jc'
	ACCESS_TOKEN_KEY = '297410594-Wdpr9p6lOJgGQJDOZegYL4bgvLONtWMV2JmtYTkm'
	ACCESS_TOKEN_SECRET = 'IXVzUOmyw7oYzFSvXc9hiyCMNkp7TZf6zAb7u4R3BGjkk'
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


