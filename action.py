# -*- coding: utf-8 -*-
from random import randrange
import math

 	
# given
# a list l of n entierss consisting of integers between 1 and 4
# x being an integer between 0 and n
# result
# a list l of n integers consisting of integers between 1 and 4, and x integers values varied between 1 and 4.

def bruit_Photon(l,x):
	for i in range(0,x):
		l[randrange(0,len(l))]=randrange(1,5)
	return l


		
# given
# a list l of n integers consisting of integers between 1 and 4
# x being an integer between 0 and 100

# result
# a list l of n integers consisting of integers between 1 and 4, and x integers equal to -1.

def perte_Photon(l,x):
	i=0
	while i<x:
		rang=randrange(0,len(l))
		while l[rang]==-1:
			rang=randrange(0,len(l))
		l[rang]=-1
		i=i+1
	return l

# given
# a list pb of n integers consisting of integers between 1 and 4
# a list f of n integers consisting of integers between 1 and 0
# a list of fb n integers consisting of integers between 1 and 0

# result
# a list pb n integers between 1 and 4, and x integers equal to -1 when different pa pb.

def perte_Photon_Lecture(pb,fa,fb):
	for i in range(0,len(pb)):
		if fa[i]!=fb[i]:pb[i]=-1
	return pb

	
# given
# a list pa n integers consisting of integers between -1 and 4
# a list pb of n integers consisting of integers between -1 and 4
# a list f of n integers consisting of integers between -1 and 0
# a list of fb n integers consisting of integers between -1 and 0

# result
# a list pa n integers consisting of integers between 1 and 4
# a list pb of n integers consisting of integers between 1 and 4
# a list f of n integers consisting of integers between 1 and 0
# a list of fb n integers consisting of integers between 1 and 0
#cells of rank or pb equal to -1 are removed
	


def photon_Manquant(pa,pb,fa,fb):
	a=[]
	b=[]
	c=[]
	d=[]
	while pa:
		x = pa.pop()
		y = pb.pop()
		z = fa.pop()
		w = fb.pop()
		if y!=-1:
			a.append(x)
			b.append(y)
			c.append(z)
			d.append(w)
	a.reverse() #necessary if we want to preserve the original order of the elements
	b.reverse() 
	c.reverse()
	d.reverse() 
	pa = a
	pb = b
	fa = c
	fb = d
	return  pa,pb,fa,fb
	
# given
# a list pa n integers consisting of integers between 1 and 4
# nb is an integer between 0 and 100
# np an integer between 0 and 100
# a list f of n integers consisting of integers between 1 and 0
# a list of fb n integers consisting of integers between 1 and 0

# result
# a list of pb of integers consisting of integers between 1 and 4 having undergone the functions bruit_Photon, perte_Photon and perte_Photon_Lecture.	
def photon_Transmission(pa,nb,np,fa,fb):
	pb=[]
	for i in range(0,len(pa)):
		pb.append(pa[i])
	pb=bruit_Photon(pb,nb)
	pb=perte_Photon(pb,np)
	pb=perte_Photon_Lecture(pb,fa,fb)

	return pb

# given
# a list pa n integers consisting of integers between 1 and 4
# a list pb of n integers consisting of integers between 1 and 4
# a list f of n integers consisting of integers between 1 and 0
# a list of fb n integers consisting of integers between 1 and 0

# result
# a list pa n integers consisting of integers between 1 and 4
# a list pb of n integers consisting of integers between 1 and 4
# a list f of n integers consisting of integers between 1 and 0
# a list of fb n integers consisting of integers between 1 and 0
#cells rank or fa is equal to fb are kept, the others are deleted
	
def filtre_Comparaison(pa,pb,fa,fb):
	a=[]
	b=[]
	c=[]
	d=[]
	while pa:
		x = pa.pop()
		y = pb.pop()
		z = fa.pop()
		w = fb.pop()
		if w==z:
			a.append(x)
			b.append(y)
			c.append(z)
			d.append(w)
	a.reverse() #necessary if we want to preserve the original order of the elements
	b.reverse() 
	c.reverse()
	d.reverse() 
	pa = a
	pb = b
	fa = c
	fb = d
	return pa,pb,fa,fb
	



# given
# a list pa n integers consisting of integers between 1 and 4
# a list pb of n integers consisting of integers between 1 and 4

# result
# a list of integers consisting of the common values of pb and pa.

def comparaison_Photon(pb,pa):
	p=[]
	for i in range(0,len(pb)):
		if pb[i]==pa[i] and pb[i]!=0:p.append(pb[i])
	return p
	
 	
# given
#a list of integers containing the values (1,2,3,4)
#a list lb of integers containing the values (1,2,3,4)
#na integer number of photons of different acceptable

# result
# returns true if the number of differences between la and lb is superior to na

def detection_Pirate(la,lb,na):
	e=0
	for i in range(0,len(la)):
		if la[i]!=lb[i]:
			e=e+1		
	if e>na:
		d=True	
	else: 
		d=False

	return d
	
# given
#a list l of integers containing the values (1,2,3,4)

# result
#a list l of integers containing the values (1,2,3,4) having the function bruit_Photon
def piratage(l,x):
	l=bruit_Photon(l,x)
	return l

# given
#a list of ca of integers containing the values 0 or 1
#a list cb of integers containing the values 0 or 1
#an integer b

# result
#a boolean true if there is at least one difference between ca and cb, and false otherwise

def comparaison_Clef_Finale(ca,cb):
	erreur=False
	i=0
	while i<len(cb) and erreur==False:
		if ca[i]!=cb[i]:erreur=True
		i=i+1
	return erreur
	


		
# given
#a whole
#an integer b
# result
#a real result of a/b

def taux_De_Transfert(a,b):
	r=a/b
	return r


