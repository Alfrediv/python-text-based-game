import random
import winsound
import time
import os
#playsound('annoying sound.wav')

PlayerHealth = 100
armour = 100
speed = 0 
strength = 0 
damage = 15
Points=100
canleave=False
ammo = 180
boxspawn=True
PlayerStats = [PlayerHealth, armour, speed, ammo, Points]
boxchance = 1
wonderweapon=False
wonderweapon =("ray gun" or "shatterstar")
FinalBossHealth=1,000
SoldierHealth=100
OfficerHealth=150
AvagadroHealth=200



#killing hostiles

#acl art 
print('------------+-------------')
print('      ___ /^^[___              _')
print('     /|^+----+   |#___________//')
print('   ( -+ |____|    ______-----+/')
print('     ==_________--')            
print('       ~_|___|__')
#--------------------------------------------------------------------------------------------------------------------------
room = 1
choice = "potatoes"
inventory = ["medkit", "rations ", "ammo ", " ", " ", " ", " "]
print("your inventory:", inventory)
#Name
print ("Welcome to Redacted ops, 1945!")
#Pause feature

def sound():
    winsound.Beep(480,200)

    winsound.Beep(1568,200)

    winsound.Beep(1568,200)

    winsound.Beep(1568,200)



    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)


    winsound.Beep(370,200)

    winsound.Beep(392,200)

    winsound.Beep(370,200)

    winsound.Beep(392,200)

    winsound.Beep(392,400)

    winsound.Beep(196,400)



    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(84,200)

    winsound.Beep(880,200)

    winsound.Beep(831,200)

    winsound.Beep(880,200)

    winsound.Beep(988,400)


    winsound.Beep(880,200)

    winsound.Beep(784,200)

    winsound.Beep(699,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(880,200)

    winsound.Beep(830,200)

    winsound.Beep(880,200)

    winsound.Beep(988,400)

    time.sleep(200/1000)

    winsound.Beep(1108,10)
    winsound.Beep(1174,200)
    winsound.Beep(1480,10)
    winsound.Beep(1568,200)


    time.sleep(200/1000)
    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(784,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(880,200)

    winsound.Beep(830,200)

    winsound.Beep(880,200)

    winsound.Beep(988,400)


    winsound.Beep(880,200)

    winsound.Beep(784,200)

    winsound.Beep(699,200)


    winsound.Beep(659,200)

    winsound.Beep(699,200)

    winsound.Beep(784,200)

    winsound.Beep(880,400)

    winsound.Beep(784,200)

    winsound.Beep(699,200)

    winsound.Beep(659,200)



    winsound.Beep(587,200)

    winsound.Beep(659,200)

    winsound.Beep(699,200)

    winsound.Beep(784,400)

    winsound.Beep(699,200)

    winsound.Beep(659,200)

    winsound.Beep(587,200)



    winsound.Beep(523,200)

    winsound.Beep(587,200)

    winsound.Beep(659,200)

    winsound.Beep(699,400)

    winsound.Beep(659,200)

    winsound.Beep(587,200)

    winsound.Beep(494,200)

    winsound.Beep(523,200)


    time.sleep(400/1000)

    winsound.Beep(349,400)

    winsound.Beep(392,200)

    winsound.Beep(330,200)

    winsound.Beep(523,200)

    winsound.Beep(494,200)

    winsound.Beep(466,200)



    winsound.Beep(440,200)

    winsound.Beep(494,200)

    winsound.Beep(523,200)

    winsound.Beep(880,200)

    winsound.Beep(494,200)

    winsound.Beep(880,200)

    winsound.Beep(1760,200)

    winsound.Beep(440,200)



    winsound.Beep(392,200)

    winsound.Beep(440,200)

    winsound.Beep(494,200)

    winsound.Beep(784,200)

    winsound.Beep(440, 200)

    winsound.Beep(784,200)

    winsound.Beep(1568,200)

    winsound.Beep(392,200)



    winsound.Beep(349,200)

    winsound.Beep(392,200)

    winsound.Beep(440,200)

    winsound.Beep(699,200)

    winsound.Beep(415,200)

    winsound.Beep(699,200)

    winsound.Beep(1397,200)

    winsound.Beep(349,200)



    winsound.Beep(330,200)

    winsound.Beep(311,200)

    winsound.Beep(330,200)

    winsound.Beep(659,200)

    winsound.Beep(699,400)

    winsound.Beep(784,400)



    winsound.Beep(440,200)

    winsound.Beep(494,200)

    winsound.Beep(523,200)

    winsound.Beep(880,200)

    winsound.Beep(494,200)

    winsound.Beep(880,200)

    winsound.Beep(1760,200)

    winsound.Beep(440,200)



    winsound.Beep(392,200)

    winsound.Beep(440,200)

    winsound.Beep(494,200)

    winsound.Beep(784,200)

    winsound.Beep(440,200)

    winsound.Beep(784,200)

    winsound.Beep(1568,200)

    winsound.Beep(392,200)



    winsound.Beep(349,200)

    winsound.Beep(392,200)

    winsound.Beep(440,200)

    winsound.Beep(699,200)

    winsound.Beep(659,200)

    winsound.Beep(699,200)

    winsound.Beep(740,200)

    winsound.Beep(784,200)

    winsound.Beep(392,200)

    winsound.Beep(392,200)

    winsound.Beep(392,200)

    winsound.Beep(392,200)

    winsound.Beep(196,200)

    winsound.Beep(196,200)

    winsound.Beep(196,200)



    winsound.Beep(185,200)

    winsound.Beep(196,200)

    winsound.Beep(185,200)

    winsound.Beep(196,200)

    winsound.Beep(208,200)

    winsound.Beep(220,200)

    winsound.Beep(233,200)

    winsound.Beep(247,200)

def pause():
	programPause = input("Press the ENTER key to continue ...........")
#final boss 
def Finalboss ():
	if inventory == ("captured scientist" and room == 10 and inventory == "wonderweapon" ):
		FinalBoss=True
		playsound('Finalbossmusic.mp3')
		print("The Booty Warrior has arrived! Prepare for battle!")
		print("We can do this the easy way, or the hard way. The choice is yours. The creature says")
		programPause=input("Press the enter key to continue")
		print(" This is dispach, I recommend using that wonderweapon you have ")
		print (inventory)
		while FinalBossHealth>0 or PlayerHealth >0:
			PlayeHealth2 -= 40
		print(" The enemy hits you for" , attack, "damage!")
		PlayerHealth -= attack
		if search_item(inventory, "Ray gun"):
			attack = 150
		elif search_item(inventory, "Shatter star"):
			attack = 250
		elif search_item(inventory, "pistol"):
			attack = 15
			ammo-=1
			print(ammo)
		elif search_item(inventory, "smg"):
			attack = 30
			ammo-=5
			print(ammo)
		elif search_item(inventory, "knife"):
			attack = 100
			ammo+=1
		
		else:
			attack+=0 (FinalBossHealth)
		if FinalBossHealth>=500 or PlayerHealth>=50:
			print("I see you picked the hard way!")

		if FinalBossHealth<=0:
			print(" You defeated the final boss ")
#Battle function 
def Battle(MonsterHealth,monsmin, monsmax,Points,PlayerHealth):

	print("-------------A foe Approaches!------------------")
	input("Press any key to begin battle!")
	while MonsterHealth > 0 or PlayerHealth > 0 or SoldierHealth>0 or OfficerHealth>0 or AvagadroHealth>0:
		#monster turn 
		Monsterattack = random.randrange(monsmin,monsmax)
		print(" The enemy hits you for" , Monsterattack, "damage!")
		PlayerHealth -= Monsterattack
		PlayerStats[1]-=20
		print(PlayerHealth)

		if SoldierHealth<=0:
			print("You defeated a hostile soldier")
			Points+=25

		if OfficerHealth<=0:
			print("You defeated an officer")
			Points+=50

		if AvagadroHealth<=0:
			print("You somehow defeated an Avagadro")
			Points+=100

		if PlayerHealth<=0:
			print("Misson failed, we'll get em next time! ")
		#players turn 
		print("selcet the weapon you would like to use for this fight")
		print(inventory)
		choice=input()
		if choice==("pistol"):
			attack=15
			speed+=10
			MonsterHealth-=15
			SoldierHealth-=15
			OfficerHealth-=15
			AvagadroHealth-=15

		elif choice==("smg"):
			attack=30
			speed+=6
			MonsterHealth-=30
			SoldierHealth-=30
			OfficerHealth-=30
			AvagadroHealth-=30

		elif choice==("knife"):
			attack=100
			MonsterHealth-=100
			PlayerStats[1]+=30
			SoldierHealth-=100
			OfficerHealth-=100
			AvagadroHealth-=100

		elif choice==("ray gun"):
			attack=150
			speed+=10
			MonsterHealth-=150
			SoldierHealth-=150
			OfficerHealth-=150
			AvagadroHealth-=150

		elif choice==("shatterstar"):
			attack=250
			speed+=20
			MonsterHealth-=250
			SoldierHealth-=250
			OfficerHealth-=250
			AvagadroHealth-=250
		elif choice==("grenade"):
			attack=200
			MonsterHealth-=200
			SoldierHealth-=200
			OfficerHealth-=200
			AvagadroHealth-=200
		
	
#attack = random.randrange(0,1)
		print(" You hit the enemy for" , attack, "damage!")
		MonsterHealth -= attack
		print("MonsterHealth:",MonsterHealth)
		print("PlayerHealth:", PlayerHealth)
		print()
		input("Press any button to continue")
		PlayerHealth = PlayerHealth
		#use items
		choice == input (" What item do you want to use? ")
		if choice in inventory:
			if choice == " ammo ":
				print("You have added 180 rounds to your spare ammo count")
				ammo += 180
				inventory.remove("ammo")
			elif choice == "medkit":
				print('you have used a medkit, you are back to full health')
				PlayerHealth += 100
				inventory.remove("medkit")
			elif choice=="rations":
				print("You have used some rations. This restored some health")
				PlayerHealth+=25
				inventory.remove(rations)
			else:
				print("sorry bud, you dont have this item")
		
#search list inventory
def search_item(inventory, item):
	for i in range(len(inventory)):
		if inventory[i] == item:
			return true
		return false
#shopping system 
def shop(Points):
	choice = "Frogs"
	print()
	Print("-----------------------------------------------")
	print("Use buy Stations to purchase equipment")
	while choice != " quit":
		print("You have ", Points,"points left")
		print(" press 1 to purchase ammo +180 rounds(50pts), 2 to purchase grenades +2grenades(25pts), 3 to purchase rations +4 rations(15pts), 4 to purchase a medkit +1 medkit(65pts), morphine +1 (30pts), or type quit to quit")
		if choice == "1":
			if points >= 50:
				print("+180 ammo")
				points -=50

			else:
				print("I do not understand that")

			
		elif choice == "2":
			print("You bought 2 grenades ")

		elif choice == "3":
			print(" You bought 4 rations ")

		elif choice == "4":
			print(" You bought a medkit ")
			
		elif choice == "quit":
			print(" Dont die on me, I need your money! Bye now !")

		else:
			print("I dont know what that means")

	return Points
	print("-----------------------------------------")
	print() 

#game variables 
inventory = ["Knife", "Grenades", "Medkit", "Rations", " ", " ", " "," ", " "," ", " "]
#storyline 
debreifing = input("Look over the misson file? y/n")
if debreifing == 'y':
	print('')
	print('Mission name: Operation Mincemeat')
	print('')
	print('Briefing: You are an allied soldier infiltrating a highly dangerous German scientific research division headquarters')
	pause()
	print('Your mission is to find a captured allied scientist, any intel on what they are doing at this research facility, and a wonder weapon')
	print('')
	pause()
	print('Mission Bonuses:extract with a captured soldier or scientist, have over 50 hp when extracting, or bring back a bottle of wine.')
	pause()
	print(' Good Luck Soldier! Make sure you come back home.')
if debreifing == 'n':
	print('Not a smart move on your part, but hey if you want to go in blind it is cool with us')

#Game loop is everything below this!-----------------------------------------------------------------------------
#MonsterGen
def monsterGen(Points):
	num = random.randrange(0, 100)
	if num < 20:#20% chance 
		print("a Ememy Soilder has spotted you! ")
		Battle(30, 0, 100, Points,PlayerHealth)
	elif num < 50:#30% chance 
		print(" a Hostile officer has found you!")
		Battle(150, 0, 100, Points, PlayerHealth)

	elif num < 52:#10% chance 
		print("an avagadro has come for you! ")
		Battle(200, 0, 100, Points, PlayerHealth)
	else:#40% chance 
		return 0 

items = []
#mysterybox 
def itemDropper():
	num = random.randrange(1,100)
	
	if num < 25:#25% chance 
		items.append("pistol ")
		print ("You get a starter pistol !")
		inventory[4]= "pistol"
		itemDropper=True
	
	elif num < 50:#25 % chance 
		items.append("smg")
		print ("You get a smg")
		inventory[5]="smg"
		itemDropper=True
	
	elif num < 60:#10% chance 
		items.append("Ballistic knife ")
		print( "You got a Ballistic Knife ! ")
		inventory[6]="ballistic knife"
		itemDropper=True
	
	elif num < 61:#1%
		items.append("Ray Gun")
		print("You Got a Ray Gun !!!!!!")
		inventory [7]= "Ray gun"
		wonderweapon=True
		itemDropper=True
	elif num < 62:
		items.append("Shatter Star")
		print("You got a Shatter star!!!!")
		inventory[8] = "Shatter star "
		wonderweapon=True
		itemDropper=True
	else:# anything else 
		print("You got the teddy bear! The box will now respawn elsewhere .......")
		itemDropper=False 
#while(1):
	#itemDropper()
	#input()
#Rooms 1-13
PlayerHealth -= monsterGen(Points)

while choice != "quit" and PlayerHealth > 0:
	if inventory == "exfil flare" and "captured scientist" and "wonder weapon" and "intel documents":
		canleave=True
	#Room 1 (The starter Room)
	if room == 1:
		print("You are in the starting room.The mystery box may be in here. You can go east or south ( Press i to use Inventory Item.")
		if boxchance == room:
			print("You found the mystery Box")
			itemDropper()
		choice = input("")
		if choice == "east":
			room = 2
		elif choice == "south":
			for i in range(len (inventory)):
				if inventory[i] == 'office key':
					room = 4 
		else:
			print("I do not understand that " )
	#Room 2 ( The Vehicle bay) 
	elif room == 2:
		PlayerHealth = monsterGen(Points)
		choice = input("You are in The vehicle bay. The sounds of engines ideling and the smell of oil flood you senses, You can go east, south, or west .")
		if boxchance == room:
			print("You found the mystery Box")
			itemDropper()
		if choice == "east":
		   room = 3
		elif choice == "south":
		   room = 5
		elif choice == "west":
		   room = 1
		else:
		   print("I do not understand that ")
	#Room 3 (The power Station) Head researcher key in here 
	elif room == 3:
		print("Electricty surges all around you.The sound of generators fills your ears. The head reseachers office key is sitting on a generator")
		choice = input("You are in The Power Station. You can go south or west.")
		if boxchance == room:
			print("You found the mystery Box, spin it till you get the prefered weapon! ")
			itemDropper()
		if choice == "south":
		   room = 6
		elif choice == "west":
		   room = 2
		if choice == "key" or choice == "get key":
			inventory[0] = "office key"
			print("You picked up the office key")
		else:
		   print("I do not understand that ")
	#Room 4 (The Head Reasearchers office) need head researchers key to enter 
	elif room == 4:
		if inventory[0]!= "office key":
			print(" you need a key to enter here ")
			room = 1
		monsterGen(Points)
		if inventory[0]=="office key":
			room=4
			print("You unlocked the Head Researchers Office")
			inventory[0]=" "
		else:
			print("the office is locked. Try to find the key")
		choice = input("You are in The head Researchers office.You dont see anything of importance for some reason. You can go east or south.")
		print("The bunker key is on the desk")
		if boxchance == room:
			print("You found The mystery Box")
			itemDropper()
		if choice == "east":
			room = 5
		elif choice == "south":
			room = 7
		if choice == "pick up key" or choice =="key" or choice == "grab the key":
			inventory[0]="key"
			print("You picked up the key to the Bunker")
		else:
			print("I do not understand that ")
	#Room 5 (The Clearing) exfil point must have required items 
	elif room == 5:
		choice = input("You are in The clearing.The tree look as if they had been pushed apart by some giant hands. You can go north, east, south, or west. If you have required items you may exfil.")
		if choice == "east":
			room = 6
		elif choice == "south":
			if inventory[0]==" Bunker key":
				room = 8
				print("You unlocked the bunker with the key")
				inventory[0]=" "
			if inventory[0]!="bunker key":
				print("You need a key to enter the bunker")
		elif choice =="north":
			room = 2
		elif choice =="west":
			room = 4 
		elif choice == "exfil":
			print("exfil bird incoming")
			canleave=True

		else:
			print("I do not understand that ")
	#Room 6 (The Breifing room) buy station in here 
	elif room == 6:
		choice = input("You are in The Breifing Room. paper scattered around the room. There is a board with target for german assults.You can go north, south, or west. There is a Buy station in this room. Purchase some supplies if needed ")
		if choice == "north":
			room = 3
		elif choice == "west":
			room = 5
		elif choice == "south":
			if inventory[0]==" Bunker key":
				room = 8
				print("You unlocked the bunker with the key")
				inventory[0]=" "
			if inventory[0]!="bunker key":
				print("you need the bunker key to enter")
		if choice == " Shop":
			Shop = Shop(points)
		else:
			print("I do not understand that ")
	#Room 7 and 8 (The Sebastian Monumnet and The Bunker ) key needed to enter the bunker
	elif room == 7:
		monsterGen()
		choice = input("You are near the sebastian Monument.This monument stands for the tryharding that germans are doing across thei facility. You can go east or north.")
		if choice == "east":
			if inventory[0]==" Bunker key":
				room = 8
				print("You unlocked the bunker with the key")
				inventory[0]=" "

			if inventory[0]!="bunker key":
				print("you need the bunker key to enter")
			else:
					print("the door is locked")
					print(" You need a bunker key to enter The Bunker")
		elif choice == "north":
			room = 4
		else:
			print("I do not understand that ")
	#Room 8
		if room == 8:
			choice = input("You are in The Bunker. You can go east,south, west, or north.")
		if choice == "east":
			room = 6
		elif choice == "south":
			room = 10
		elif choice == "north":
			room = 5
		elif choice == "west":
			room = 7
		else:
			print("I do not understand that ")
	#Room 9 ( The testing Facility ) prison key here 
	elif room == 9:
		choice = input("You Have arrived to the Testing Facility.test tubes and vats of acid fill the area,the smell of chemicals is strong. You can go north or east.")
		print("The the Prison key on the floor")
		if choice == "east":
			room = 10
		elif choice == "north":
			room = 7
		elif choice.find("key"):
			inventory[1] = " Prison key"
			print("You picked up the Prison key")
		else:
			print("I do not understand that ")
	#Room 10 ( The Club) booty warroir boss fight here 
	elif room == 10:
		monsterGen()
		choice = input("You are in The Club. There is a half beaten sign hanging on the wall. It reads: BeWare The Booty Warrior!. You can go north or west.")
		if choice == "north":
			if inventory[0]==" Bunker key":
				room = 8
				print("You unlocked the bunker with the key")
				inventory[0]=" "

			if inventory[0]!="bunker key":
				print("you need the bunker key to enter")
		elif choice == " west":
			room = 9
		elif choice == "east":
			room = 11
		else:
			print("I do not understand that ")

#Room11(the Prison) rescue the captive here 
	elif room == 11:
		choice = input ("You are in the Prison Area.The captured scientist you need to extract is in the jail cell. Use the key to unlock the cell and carry him out   You can go either west(the club) or east(the gym).")
		monsterGen(Points)
		if inventory[3]=="prison key":
					room = 11
					print("you unlocked the jail cell and rescused the scientist ")
					inventory[3]="scientist  "
					speed-=3
		if choice == "west":
				room = 10
		elif choice == "east":
				room = 12
		elif inventory !=("prison key"):
			print("the door is locked")
			print(" You need a prison key to enter The jail cell ")

		else:
			print(" I do not copy, please repeat that")
#the room 12  The gym 
	if room == 12:
		choice = input ("You are in the Gym. You can exercise to gain more physical strength. Or you could go north or west")
		if choice == "north":
			room = 13
			if inventory[4]==" Basement key":
				room = 13
				print("You unlocked the basement with the key")
				inventory[4]=" "
		elif choice == "west":
				room = 11
		elif choice == "workout":
			strength+=1
			speed+=1
		else:
				print("I dont copy, please repeat")
#room 13 the basement 
	if room == 13:
		choice = input("You have found the basement. You can only go south. There is a mysterybox, a buy station and a exfil flare on the shelf.")
		if choice == "south":
			room = 12
		elif choice == ("use buy station"):
			shop = shop(Points)
			boxchance=room
		elif choice.find("key"):
			inventory[1] = " exfil flare"
			print("You picked up an exfil flare")
		if inventory ==("wonderweapon"):
			damage+=100
		
	
			
			
			
			
#end of game loop 
		# Need to add exfil requirnments and what items you exfil with
	if PlayerHealth <=0:
		print(" You died, restart to try again")	
	elif choice=="exfil":
		print ("you made it out soilder, Good work ")

