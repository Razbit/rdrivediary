# -*- coding: UTF-8 -*-
#COPYRIGHT Toivo Koskinen 2015

def polaskin(hinta):
	while True:
		luke= raw_input("Poistuminen Q:lla, litrahintatiedot Enter >> ")
		if luke == 'Q' or luke == 'q':
			break	
		else:
			maarab=len(hinta)-1
			hjinta = 0
			for var in hinta:
				hjinta+= var
				
			keskihinta=float(hjinta)/float(maarab)
			print " "
			print "-----------------------------------------------"
			print "Polttoaineen keskimääräinen litrahinta: "
			print "%.3f" % (keskihinta) # Pyöristä 3 desimaaliin
	
