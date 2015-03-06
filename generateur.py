# -*- coding: utf-8 -*-
from random import randrange


		
#Function that allows you to simulate the generation of bits.
# given
# an integer n>0
# result
# a list of ca n integers of value 0 or 1

def generation_Clef(n):
       ca=[]
       for i in range(0,n):
                 ca.append(randrange(0,2))          
       return ca
       
#Function that allows you to simulate the generation of the series of photons emitted.
#Returns a list of symbols indicating the polarization :

# given
# an integer n>0
#a list f of n integers of value 0 or 1

# result
# a list of n integers consisting of integers between 1 and 4

def generation_Photon(n,fa):
       photon=[]
       
       for i in range(0,n):
                 photon.append(randrange(1,5))          
       return photon
       	
#Returns a list of symbols indicating the polarization :
# given
# a list fa integer of value from 0 to 1
# list ca integer of value from 0 to 1

# result
# a list photon consisting of integers between 1 and 4 respecting the polarization filters
def generation_Photon_Alice(fa,ca):
	photon=[]
	for i in range(0,len(ca)):
		if fa[i]==1:
			if ca[i]==0:photon.append(1) 
			if ca[i]==1:photon.append(2) 
		if fa[i]==0:
			if ca[i]==0:photon.append(3) 
			if ca[i]==1:photon.append(4)         
	return photon

 	
# given
# an integer f>0

# result
# a filter list containing f values binary random

def generation_Filtre(f):
	filtre=[]
	for i in range(0,f):
          filtre.append(randrange(0,2))   
	return filtre


