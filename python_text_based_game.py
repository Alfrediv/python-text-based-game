room = 1
choice = "potatoes"
print ("Welcome to Sweet tooth, 1945!")
import random 

def monsterGen():
    num = random.randrange(0, 100)
    if num < 20:#20% chance 
        print("a zombie apears ")
        return 10#attack damage 
    elif num < 50:#30% chance 
        print(" a challenger aproaches")
        return 5
    elif num < 60:#10% chance 
        print("a booty warrior appears ")
        return 8 
    else:#40% chance 
        return 0 


playerHealth = 100 

playerHealth -= monsterGen()
while choice != "quit": 
    #room 1 
    if room == 1:
        choice = input("You are in the starting room. You can go eitehr east or south.")
        if choice == "east":
            room = 2
        elif choice == "south":
            room = 4 
        else:
            print("I do not understand that " )
    #room 2 
    elif room == 2:
       choice = input("You are in Room 2. You can go east, south, or west .")
       if choice == "east":
           room = 3
       elif choice == "south":
           room = 5
       elif choice == "west":
           room = 1
       else:
           print("I do not understand that ")
    #room 3
    elif room == 3:
       choice = input("You are in Room 3. You can go south or west.")
       if choice == "south":
           room = 6
       elif choice == "west":
           room = 2
       else:
           print("I do not understand that ")
    #room 4 
    elif room == 4:
       choice = input("You are in Room 4. You can go east or south.")
       if choice == "east":
           room = 5
       elif choice == "south":
           room = 7
       else:
           print("I do not understand that ")
    #room 5
    elif room == 5:
       choice = input("You are in Room 5. You can go north, east, south, or west .")
       if choice == "east":
           room = 3
       elif choice == "south":
           room = 5
       elif choice =="north":
           room = 2
       elif choice =="west":
           room = 4 

       else:
           print("I do not understand that ")
     #room 6 
    elif room == 6:
       choice = input("You are in Room 6. You can go north, south, or west.")
       if choice == "north":
           room = 3
       elif choice == "west":
           room = 5
       elif choice == "south":
           room = 9
       else:
           print("I do not understand that ")
      #room 7 
    elif room == 7:
       choice = input("You are in Room 7. You can go east or north.")
       if choice == "east":
           room = 8
       elif choice == "north":
           room = 4
       else:
           print("I do not understand that ")
    elif room == 8:
       choice = input("You are in Room 8. You can go east or south.")
       if choice == "east":
           room = 3
       elif choice == "south":
           room = 5
       else:
           print("I do not understand that ")

    elif room == 9:
       choice = input("You are in Room 9. You can go west or north.")
       if choice == "east":
           room = 3
       elif choice == "south":
           room = 5
       else:
           print("I do not understand that ")

    elif room == 10:
       choice = input("You are in Room 10. You can go north .")
       if choice == "north":
           room = 9
       
       else:
           print("I do not understand that ")