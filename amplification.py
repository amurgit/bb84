# -*- coding: utf-8 -*-
from random import randrange
import math

# given
# a list l of n integers consisting of integers between 0 and 1.
# result
# a list p of n integers consisting of integers between 0 and 1.
# where the mixture is reproducible

def amplification_Clef(l):
	p=[]
	while l:
		x=len(l)
		f=randrange(0,2)
		if f==0:i=f1(x)
		if f==1:i=f2(x)
		p.append(l[i])
		l.pop(i)
	for i in range(0,int(len(p)/2)):
		p.pop()

	return p

 		
# given
# x is a whole number

# result
# i a whole number in the image of f1

def f1(x):
	i=int(x*x*math.pi)%x
	return i
	
# given
# x is a whole number

# result
# i a whole number in the image of f1

def f2(x):
	i=int(x*x*x*math.pi)%x
	return i

