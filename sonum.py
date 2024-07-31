import os
import random
import time

# written in Nano on Hyprland in Arch Linux. Windows is ewwww...
# sloppy code pls fix 2.0.0 :3
# work on the security of passwords, implement basic encryption into .deer files

os.system('cls' if os.name == 'nt' else 'clear') 

out=""
inp=""

print("""\033[1;31;40m .d8888b.                                           
d88P  Y88b                                      
Y88b.                                               
 "Y888b.    .d88b.  88888b.  888  888 88888b.d88b.  
    "Y88b. d88""88b 888 "88b 888  888 888 "888 "88b 
      "888 888  888 888  888 888  888 888  888  888 
Y88b  d88P Y88..88P 888  888 Y88b 888 888  888  888\033[1;37;40m  7/30/2024
\033[1;31;40m "Y8888P"   "Y88P"  888  888  "Y88888 888  888  888.\033[1;37;40m Version 1.1.0

 """)

## DEFAULT SONUM PASSKEY IS 'SECRET'.

## SONUM
prg=input("Select a tool.\n1. | Password Creator\n2. | Sonum Password Manager (best tool so far)\n3. | Sonum Earth (not very good yet)\n4. | Exit\n$ ")
## PROGRAMS
if prg=="1":
	os.system('cls' if os.name == 'nt' else 'clear')
	a=1
	dict="ABCD_-+()!@#$%^*&*(<>' EFGHIJKLMNOPQRSTUVWXYZ1234567890-+=~`;The cake is a lie.,?*abcdefgh{} security :)  ijklmnopqrstuvwxyz"
	inp=input("Length of the password? (64 recommended)  > ")
	for i in range(int(inp)):
		out+=dict[random.randint(1,len(dict)-1)]
if prg == "2":
	os.system('cls' if os.name == 'nt' else 'clear')
	g=open("password.deer","r")
	g=g.readlines()
	g=g[0]
	if g != " ":
		print("Please input your Password Manager Sonum passkey. (default is 'secret')\n")
		inp=input("$ ")
	if g == inp or g == " ":
		print("Password Manager Sonum.          v1.1.0\n1. | Add Password\n2. | Get Password\n3. | Remove Password\n4. | List Password(s)\n5. | Add a passkey for your passkeys!")
		inp=input("Action? $ ")
		f = open("passkeys.deer", "a")
		phi = open("passkeys.deer","r")
		phi=phi.readlines()
		phi=phi[0]
		if inp == "1":
			os.system('cls' if os.name == 'nt' else 'clear')
			inp=input("Title? > ")
			f.write(inp+"|")
			inp=input("Password? > ")
			f.write(inp+"~")
		if inp == "2":
			os.system('cls' if os.name == 'nt' else 'clear')
			b=""
			inp=input("Name of the password? > ")
			c=(phi.find(inp))+len(inp)+1
			if phi[c-1] == "|":
				for x in range(1024):
					if phi[c] != "~":
						b+=phi[c]
						c+=1
					if phi[c] == "~":
						break
			print(b)
		if inp == "3":
			inp=input("Which password do you wanna delete\033[1;31;40m permanently\033[1;37;40m?   $ ")
			# Finish this is 1.2.0, okay me?
		if inp == "4":
			o=0
			ability=1
			n=[""]
			for i in range(len(phi)):
				
				if phi[i]=="|":
					ability=0
					while True:
						i+=1
						if phi[i]=="~":
							ability=1
							i+=1
							o+=1
							n.append("")
							break
				elif i < len(phi)-1 and ability == 1:
					n[o]+=phi[i]
			del n[1::2]
			print(". ")
			for v in range(len(n)):
				print(n[v])
			

		if inp == "5":
			os.system('cls' if os.name == 'nt' else 'clear')
			os.remove("password.deer")
			inp=input("What password would you like to secure your manager with? (leaving this blank will get rid of the passkey thing)  > ")
			if inp == "":
				inp+=" "
			p = open("password.deer","a")
			p.write(inp)
if prg == "3":
	#SONUM EARTH
	US = ["Washington D.C (capital)","N/A","United States",333320000,"The United States of America is a country with deep history and has many diplomatic ties with other countries. The United States has many official names, but there are three common ways to say 'United States': 'US', 'USA' and 'United States of America'. The country was founded in the late 1700's and declared independence from the British Empire (commonwealth)."]
	Atlanta = ["Atlanta","GA","United States",499127,"Atlanta is the capital city of the US state Georgia. It is very economically beneficial to the US Government. It has rich history."] # CITY, STATE, COUNTRY, POPULATION, DESCRIPTION
	Berlin = ["Berlin","Berlin (state)","Federal Republic of Germany",3878100,"Berlin is a city in the European continent (central) that was sieged several times throughout history and dispite the horrors commited in it's turf it still remains mostly united. Berlin used to be split up from 1961-1990 during the Cold War. The United States tore down the Berlin Wall using diplomacy in the Reagan administration (Ronald Reagan) just before the U.S.S.R collapsed."]
	print("Sonum Earth v1.0.0\n\nUS, Atlanta, Berlin")
	inp=input("Type the location you wanna see (capitalization and spelling) $ ")
	print("\n\n"+eval(inp)[0]+", "+eval(inp)[1]+", "+eval(inp)[2]+"\n"+str(eval(inp)[3])+" population\n\n"+eval(inp)[4])
print(out)
print("\nSafe travels.")
