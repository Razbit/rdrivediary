# -*- coding: UTF-8 -*-
#Urpon ohjelma
#Alkaa varsinaisesti riviltä 176
#COPYRIGHT Toivo Koskinen 2015

import os
import time
from time import gmtime, strftime
os.system('clear') and os.system('cls') #Tyhjennetään komentorivi turhasta roinasta

def addp(x): # lisää tekstiä data.txt tiedostoon. Merkkijonon lopuksi rivinvaihto
	with open('data.txt',"a+") as output_file:
	        output_file.write(str(x)+'\n')
	output_file.close()

def add(x): #lisää tekstiä data.txt tiedostoon ilman rivinvaihtoa lopussa
	with open('data.txt',"a+") as output_file:
	        output_file.write(str(x)+' ')
	output_file.close()

def nimi(): # Kyselee käyttäjän tietoja, jos ei ole vielä tallessa
	ni='data.txt'
	nim= open(ni,'a')
	try: 
		nimi= "Päiväkirjan haltijan nimi: "+ raw_input("Anna nimesi, niin päästään alkuun: ")
	except:
		print " Virhe!"
	addp(nimi)
	ajokki= "Ajoneuvo: "+ raw_input("Mikä on kulkineesi? ")
	addp(ajokki)
	ajika= "Vuosimalli: "+raw_input("Vuosimalli? ")
	addp(ajika)
	viiva="------------------------------------------"
	addp(viiva)
	info= "1. Päivämäärä 2. kilometrit 3. ostetut litrat 4. litrahinta "
	addp(info)
	addp(viiva)
	print "Hieno homma! Nyt päästään jatkamaan!"
	nim.close()


def tankkaus(): #Tankkaustiedot
	print "Tankkaustietojen lisääminen päiväkirjaan: "
	kilo= 0.0
	poltto= 0.0
	hinta= 0.0
	while True: # Tarkastetaan oliko annettu tieto numeroina
		tmpkilo= raw_input("Anna mittarin kilometrit: ")
		try:
			kilo= float(tmpkilo)
		except Exception:
			print "Et antanut numeroita!!!!!!!!!!"
		else:
			break

	while True:	
		tmppoltto= raw_input("Ostetun polttoaineen määrä (litraa): ")
		try:
			poltto= float(tmppoltto)
		except Exception:
			print "Et antanut numeroita!!!!!!!!!!"
		else:
			break
	while True:	
		tmphinta= raw_input("Litrahinta: ")
		try:
			hinta= float(tmphinta)
		except Exception:
			print "Et antanut numeroita!!!!!!!!!!"
		else:
			break

	pvm= strftime("%d_%b_%Y")
	
	add(pvm+":")
	add(kilo)
	add(poltto)
	addp(hinta)
	

def inikilsa(): #Kilometritiedot lisätään päiväkirjaan
	print "Ensimmäisten kilometritietojen lisääminen päiväkirjaan: "
	kilo= raw_input("Anna mittarin nykyiset kilometrit: ")
	poltto= 0
	hinta= 0
	pvm= strftime("%d_%b_%Y")
	
	add(pvm+":")
	add(kilo)
	add(poltto)
	addp(hinta)
	

def historia(): # Lukee data.txt tiedoston ruudulle
	while True:
		luke= raw_input("Poistuminen Q:lla, historiatiedot Enter >> ")
		if luke == 'Q' or luke == 'q':
			break	
		else:
			os.system('clear') and os.system('cls')	
			print " "
			print "-----------------------------------------"
			print " "
			h='data.txt'	
			outp= open(h,'r')  #Avataan datatiedosto
			for rivi in outp:
				print rivi #Tulostetaan data.txt tiedoston sisältö
			outp.close()
		

def keski2(): #Antaa ulos kolmena listana bensiininkulutuksen, kilometrit ja litrahinnan
	pvm = []	
	km = []
	bensa = []
	hinta = []
	with open('data.txt', 'r') as f:
		lines_7_through_end = f.readlines()[6:]
		u = 1;
		i =1

		for line in lines_7_through_end: 
#Kerätään tiedot data.txt:stä riviltä 7 alkaen, ja lisätään listoihin"""
			print " Tankkaus %s: %s" % (u, line)
			tmp_pvm, tmp_km, tmp_bensa, tmp_hinta = line.split()
			pvm.append(str(tmp_pvm)) #Kilometrit merkkijonona listaan
			bensa.append(float(tmp_bensa)) #muuttaa liukuluvuksi ja lisää listaan bensa
			km.append(float(tmp_km)) #muutetaan liukuluvuksi ja lisätään listaan km
			hinta.append(float(tmp_hinta))  #muuttaa liukuluvuksi ja lisää listaan hinta
    			i = i+1
			u+=1
	return pvm, km, bensa, hinta # Palauttaa funktion arvona kolme listaa


def laskin(bensa, km): #Laskee erilaisia keskikulutuslukemia
	os.system('clear') and os.system('cls')	
	print " "
	print "------------------------------------------------"
	print " ~~Q poistuu laskimesta~~ "
	print "1. Edellisen tankkauksen keskikulutus"
	print "2. Kahden edellisen tankkauksen keskikulutus"
	print "3. Keskikulutus koko ajalta"
	print "------------------------------------------------"
	print " "
	
	
	while True:	
		try:
			kysy2= raw_input("Valitse mitä tehdään >> ")
		except Exception:
			print "Valitse yltä mitä tehdään"
		
		if kysy2 == 'Q' or kysy2 == 'q':
			break 		
	
		elif kysy2 == '1':
			try:			
				kulutus= float(bensa[-1])/(km[-1]-km[-2]) #Lasketaan listojen viimeisestä ja toiseksi viimeisestä indexistä polttoaineen keskikulutus
			except Exception: #Kaikki virheet ohitetaan yhdellä ohjeella
				print "Liian vähän polttoainetietoja tämän laskemiseen"			
			print " "
			print "Keskikulutus edelliseltä tankkauskerralta:"		
			print "   %.2f L/100km" % (kulutus*100) #%.2f: ota liukuluku sulkujen sisästä, pyöristä kahteen desimaaliin ja tunge tulostuksen joukkoon
			print "------------------------------------------"
			print " "
		
		elif kysy2 == '2':
			try:
				kulutus2= float((bensa[-1]+bensa[-2]))/float(((km[-1] - km[-2])+(km[-2] - km[-3])))
			except Exception:
				print "-Liian vähän polttoainetietoja tämän laskemiseen"
			else:
				
				print " "
				print "Keskikulutus kahdelta edelliseltä tankkauskerralta:"		
				print "   %.2f L/100km" % (kulutus2*100)	
			print "------------------------------------------"
			print " "

		elif kysy2 == '3': 
			pensa = 0
			for var in bensa:
				pensa+= var
			try:			
				kulutus3= pensa/float((km[-1] - km[0]))
			except Exception:
				print "-Liian vähän polttoainetietoja tämän laskemiseen"
			print " "
			print "Keskikulutus kaikilta merkityiltä tankkauksilta:"		
			print "   %.2f L/100km" % (kulutus3*100)
			print "------------------------------------------"
			print " "			
			
			
#Varsinainn ohjelma alkaa
print " "
print "------------------------------------------------------------------------------"
print "Tervetuloa ajopäiväkirjaan! "
print "Ajopäiväkirja 2015 Edition"
print "Copyright UrpoCloud Inc. "
print "Creator: Toivo Koskinen"
print "------------------------------------------------------------------------------"
print " "


print " "
print "Lisää tietoja päiväkirjaan: "
print "-----------------------------------------------------"
print " "
with open('data.txt') as data: #Tarkastaa oliko data.txt tiedostossa vielä tietoa
	data.seek(0)
	firstc = data.read(1)
	if not firstc:
		print "Nimeäsi ei ollut vielä talletetettu"
		nimi() #Nimifunktiolla lisätään nimitiedot tiedostoon
		print "Nyt voimme jatkaa"
		time.sleep(1)
		os.system('clear') and os.system('cls')	
		inikilsa()

	else:
		data.seek(0)
		print " "
		print "Tietosi löytyivät, jatkakaamme"
		print " "
		time.sleep(1)
		os.system('clear') and os.system('cls')	
		

print " "
print "----------------------------------------------"
print "AJOPÄIVÄKIRJA 2015 Edition"
print " "

while True: #Päävalikko
		
	try: 
		
		print "----------------------------------------------"
		print "Q poistuu ohjelmasta tai sen osiosta"
		print "1. Tarkastele historiatietoja"
		print "2. Laske keskikulutus"
		print "3. Keskimääräinen polttoaineen hinta"
		print "4. Tähän asti käytetty raha"
		print "5. Lisää tankkaustietoja"
		print "Tankkaustietoja tarvitsee väh. 2kpl, että laskin toimii"
		print "-----------------------------------------------"
		print " "		
		tieto= raw_input("Mitä haluat tehdä? ^^ ")
		print " "
		print "-----------------------------------------------"
		print " "
	except:
		print "Valitse ylläolevista numeroista"
	
	if tieto == 'Q' or tieto == 'q': # Q:lla voidaan poistua while-rakenteesta
		break	
	
	elif tieto == '1':
		os.system('clear') and os.system('cls')
		historia()
	
	elif tieto == '2':
		os.system('clear') and os.system('cls')
		pvm, km, bensa, hinta = keski2() #Hakee keski2() funktion tekemät listat käyttöönsä
		laskin(bensa, km) #Lähettää nämä argumentit laskin-funktiolle
	elif tieto == '3':
		os.system('clear') and os.system('cls')
		import polttoaine
		pvm, km, bensa, hinta = keski2()
		polttoaine.polaskin(hinta)
	elif tieto == '4':
		os.system('clear') and os.system('cls')
		pvm, km, bensa, hinta = keski2() 
		import raha
		raha.rahalaskin(bensa,hinta)
	elif tieto == '5':
		os.system('clear') and os.system('cls')
		tankkaus()
	else:
		print "Numerolla ei toimintoa"
