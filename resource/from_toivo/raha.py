# -*- coding: UTF-8 -*-
#COPYRIGHT Toivo Koskinen 2015

import os
def rahalaskin(bensa, hinta): #Lasketaan kaikki tähän mennessä käytetty raha
	os.system('clear') and os.system('cls') #Tyhjennetään komentorivi turhasta
	maarab=len(hinta)-1
	rahe= sum(bensa)*(sum(hinta)/float(maarab))
	print "------------------------------------------------"
	print " "
	print "Kuluttamasi raha polttoaineeseen tähän mennessä: %.2f rahea" % (rahe) #%.2f huomioi pyöristyksen
	print " "
