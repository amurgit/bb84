import tkinter
#! /usr/bin/env python3.1
# -*- coding: utf-8 -*-
#auteur:Yves Mercadier Daniel Veissi

import sys
import tkinter

from action import *
from amplification import *
from codage import *
from generateur import *
from graphisme import *
from reconciliation import *

list_action=[ "Alice generates a key","Alice generates a filter.","Alice sends photons.", "Bob measure. ","Bob bed.","Bob announces the chosen base. ","Bob and alice are comparing their base. ", "Alice and Bob to analyze the data. "," Secret key reconciled. "," Secret key amplified. "]
etape=0
erreur=False
nombre_photon=500
bruit=0.5
perte=2

 	
# given
# a list l of integers between -1 and 4

# result
# shows a step of the protocol, BB85

def affiche_Etape(l,la,etape):
	if etape==0:
		print()
		print()
		print("Début du protocole de communication.")
		
		print()
		print()
		print(la[etape],affiche_Liste_Clef(l))

		
	if etape==1:
		print(la[etape],affiche_Liste_Filtre(l))

	if etape==2:
		print(la[etape],affiche_Liste_Photon(l))

	if etape==3:
		print(la[etape],affiche_Liste_Filtre(l))
		
	if etape==4:
		print(la[etape],affiche_Liste_Photon(l))

	if etape==5:
		print(la[etape],affiche_Liste_Filtre(l))

	if etape==6:
		print(la[etape],affiche_Liste_Filtre(l))

	if etape==7:
		print(la[etape],affiche_Liste_Clef(l))

	if etape==8:
		print(la[etape],affiche_Liste_Clef(l))

	if etape==9:
		ligne()		
		print(la[etape],affiche_Liste_Clef(l))
		print()
		print("Fin du protocole de communication.")
		print()
		print()


		
# given
# a list l of integers between 1 and 4

# result
# displays the representation of a photon

def affiche_Liste_Photon(l):
	ch=""
	for i in range(0,len(l)):
		if l[i]==-1:
			ch=ch+" "
		elif l[i]==1:
			ch=ch+"|"
		
		elif l[i]==2:
			ch=ch+"-"
		elif l[i]==3:
			ch=ch+"/"
		elif l[i]==4:
			ch=ch+"\\"
	return(ch)
		
# given
# a list l of integers between 0 and 1

# result
# displays the representation of a filter

def affiche_Liste_Filtre(l):
	ch=""
	for i in range(0,len(l)):
		if l[i]==1:
			ch=ch+"+"
		elif l[i]==0:
			ch=ch+"X"
	return(ch)
		
 		
# given
# a list l of integers between 0 and 1

# result
# displays the representation of a sequence of binary
		
def affiche_Liste_Clef(l):
	ch=""
	for i in range(0,len(l)):
		if l[i]==0:
			ch=ch+"0"
		elif l[i]==1:
			ch=ch+"1"
	return(ch)

 	
# procedure that draws a line
def ligne():
	ligne=""                          
	for i in range(0,60+nb):        
		ligne=ligne+'='           
	print(ligne) 		


 	
# given

# result
# displays the presence of a pirate on the line

def affiche_Piratage():	
	ligne()
	print(" ")
	print(" Piracy detected.")
	print(" ")
	print(" ")
	print(" End of the communication.")
	print(" ")

	
		
#========================================================================================================================================================================
#========================================================================================================================================================================
#========================================================================================================================================================================

print()
print(" The beginning of the program")
print()
nombre_photon=int(input(' Give the number of photon transmitted :'))
pirate=int(input("Without spy(0) ; spy(1):"))
print()
print()

clef_alice=generation_Clef(nombre_photon)
l=clef_alice
affiche_Etape(l,list_action,etape)
etape=etape+1
	
filtre_alice=generation_Filtre(len(clef_alice))
l=filtre_alice
affiche_Etape(l,list_action,etape)
etape=etape+1

photon_alice=generation_Photon_Alice(filtre_alice,clef_alice) 
l=photon_alice
affiche_Etape(l,list_action,etape)
etape=etape+1

filtre_bob=generation_Filtre(len(clef_alice))
l=filtre_bob
affiche_Etape(l,list_action,etape)
etape=etape+1
		
nb_bruit=int(nombre_photon*(bruit/100))
nb_perte=int(nombre_photon*(perte/100))
photon_bob=photon_Transmission(photon_alice,nb_bruit,nb_perte,filtre_alice,filtre_bob)	
l=photon_bob
affiche_Etape(l,list_action,etape)
etape=etape+1
	
photon_alice,photon_bob,filtre_alice,filtre_bob=photon_Manquant(photon_alice,photon_bob,filtre_alice,filtre_bob)
l=filtre_bob
affiche_Etape(l,list_action,etape)
etape=etape+1

photon_alice,photon_bob,filtre_alice,filtre_bob=filtre_Comparaison(photon_alice,photon_bob,filtre_alice,filtre_bob)
l=filtre_bob
affiche_Etape(l,list_action,etape)
etape=etape+1

if pirate==1:
	photon_bob=piratage(photon_bob,int(nombre_photon*0.1))
clef_bob=qu_Bit(photon_bob)
clef_alice=qu_Bit(photon_alice)
bloc_connu_alice=bloc_Connu(clef_alice)
bloc_connu_bob=bloc_Connu(clef_bob)
l=bloc_connu_bob
affiche_Etape(l,list_action,etape)
etape=etape+1

clef_alice=sup_Bloc_Connu(clef_alice)
clef_bob=sup_Bloc_Connu(clef_bob)
		
nb=int(2.5/100*nombre_photon*10/100)
bloc_connu_alice_photon=bloc_Connu(photon_alice)
bloc_connu_bob_photon=bloc_Connu(photon_bob)
if detection_Pirate(bloc_connu_alice_photon,bloc_connu_bob_photon,nb):
				affiche_Piratage()
				etape=10
						
clef_bob=reconciliation_Parite_Simple(clef_alice,clef_bob)

l=clef_bob
affiche_Etape(l,list_action,etape)
etape=etape+1

clef_amplifie=amplification_Clef(clef_bob)
l=clef_amplifie
affiche_Etape(l,list_action,etape)
r=taux_De_Transfert(len(clef_amplifie),nombre_photon)
print()
print("Fin du programme")
