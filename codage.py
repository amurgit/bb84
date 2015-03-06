# -*- coding: utf-8 -*-

 	
# given
# a list p of n integers consisting of integers between 1 and 4
# result
# a list qb of n integers equal to 0 if p equal to 2 or 4 and equal to 1 if p equals 1 or 4.

def qu_Bit(p):
	qb=[]
	for i in range(0,len(p)):
		if p[i]==1:qb.append(1)
		if p[i]==2:qb.append(0)
		if p[i]==3:qb.append(0)
		if p[i]==4:qb.append(1)
	return qb



