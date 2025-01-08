#PunchBros Vol. 1
#Game Designed & Code Written by Matthew Rivers, CSC 101

#imports all neccesary source files
from time import sleep
from Room import Room
from Death import death
from boxingMatch import boxingFight
from boxersClass import Boxer

#all the fighters and attributes (name, health, power, defense buffer)
hank = Boxer("Hank The Tank", 100, 25, 15)
chip = Boxer("Tortilla Chip Jones", 150, 70, 80)
speedy = Boxer("Speedy Gonzalez", 275, 80, 30)
doctor = Boxer("Doctor Punch Ya Face", 320, 99, 40)
kokraig = Boxer("K.O. Kraig The Killer Kroc", 420, 135, 50)
tike = Boxer("Tike Myson", 500, 199, 65)
#user fighter
player = Boxer("Player 1", 150, 50, 20)

#action words and 'quit' to end the game
ACTIONS = ["fight", "go", "take", "look", "happy", "use"]
QUITCOMM = ["quit"]

#creates all the rooms, using alphabetical order as directions. A=North, B=East, C=South, D=West (See Map)
#also shows what rooms have the fighters/where they are
def createRooms():
    rooms = []
    r1 = Room("Room 1")
    r2a = Room("Room 2-A", hank)
    r3a = Room("Room 3-A")
    r4a = Room("Room 4-A", kokraig)
    r5a = Room("Room 5-A")
    r6a = Room("Room 6-A", tike)
    r7a = Room("Room 7-A")
    r8a = Room("Room 8-A")
    r9a = Room("Room 9-A", doctor)
    r2b = Room("Room 2-B", speedy)
    r3b = Room("Room 3-B")
    r2c = Room("Room 2-C")
    r3c = Room("Room 3-C")
    r4c = Room("Room 4-C", chip)
    r2d = Room("Room 2-D")
    r3d = Room("Room 3-D")
    r4d = Room("Room 4-D")
    r5d = Room("Room 5-D")
    r6d = Room("Room 6-D")
    r7d = Room("Room 7-D")
    r8d = Room("Room 8-D")
    
    r1.description = "You look around the empty room. Nothing seems to be in here for you."
    r1.addExit("north", r2a)
    r1.addExit("east", r2b)
    r1.addExit("south", r2c)
    r1.addExit("west", r2d)
    rooms.append(r1)

    #when you 'look' at a fighter, like hank here for example, it will detail his difficulty rating so user can decide if they are ready
    r2a.description = "Hank The Tank! Oh man, this guy is huge!"
    r2a.addExit("east", r3a)
    r2a.addExit("south", r1)
    r2a.addItem("hank", "Better prepare yourself cause he's ready to fight! Difficulty: 1/6 ")
    rooms.append(r2a)

    r3a.description = "This room smells awful. You look around and see some rocks."
    r3a.addExit("north", r4a)
    r3a.addExit("west", r2a)
    r3a.addItem("rocks", "The rocks are in the shape of...a...crocodile?")
    rooms.append(r3a)

    r4a.description = "So that's what the smell was. Great. K.O. Kraig The Killer Kroc is standing \nin front of you and he's not too happy to see you."
    r4a.addExit("north", r6a)
    r4a.addExit("east", r5a)
    r4a.addExit("south", r3a)
    r4a.addItem("ko-kraig", "Beware! Kraig is the strongest of the swamp! Tread lightly. Difficulty: 5/6")
    rooms.append(r4a)

    r5a.description = "You take a gaze across the rocks, not seeing anything really."
    r5a.addExit("west", r4a)
    rooms.append(r5a)

    r6a.description = "Is that...boxing legend Tike Myson?!?!"
    r6a.addExit("south", r4a)
    r6a.addExit("west", r7a)
    r6a.addItem("tike-myson", "Uh Oh! Looking straight at you is the ruthless warrior Tike Myson \nhimself. The strongest of Punch Dungeon. Difficulty: 6/6")
    rooms.append(r6a)

    r7a.description = "You look around and see a box in the middle of the room, unopened."
    r7a.addExit("east", r6a)
    r7a.addExit("south", r8a)
    r7a.addExit("west", r9a)
    r7a.addItem("box", "You open the box, and there is an ancient \nmusic box inside. It's playing a song called 'CIPHER' by Kevin MacLeod. Maybe this \ncould be a sign? What could this mean?")
    rooms.append(r7a)

    r8a.description = "You don't see anything when you look around."
    r8a.addExit("north", r7a)
    rooms.append(r8a)

    r9a.description = "This room looks like an clinic of some sort...GAH! It's Doctor PunchYaFace!"
    r9a.addExit("east", r7a)
    r9a.addItem("doctor-punch-ya-face", "He may be a doctor, but he's not really into healing. Better be \ncareful, this doctors dangerous. Difficulty: 4/6")
    rooms.append(r9a)

    r2b.description = "You spot in the corner a short guy, and he's rapidly punching \n the wall. That's Speedy Gonzalez!"
    r2b.addExit("south", r3b)
    r2b.addExit("west", r1)
    r2b.addItem("speedy-gonzalez", "The quickest of the cave, he may not be strong but \nhe's hard to catch up with. Difficulty: 3/6")
    rooms.append(r2b)

    r3b.description = "You see some ancient hieroglyphics written on the wall."
    r3b.addExit("north", r2b)
    r3b.addItem("hieroglyphics", "Ax qgm sjw jwsvafy lzak...Qgm'jw ljmdq sf wpuwhlagfsd xa \nyzlwj. Lzw osq gml ak wskq...tml A vgf'l zsnw lzw sfkowj. Gfw gx \nlzw kcwdwlgfk vgwk...Al'k sulmsddq gfw gx qgmj gdv xjawfvk. Zak fsew ak bsuc, tml zw zsk vwewflas sfv lzafck wnwjqvsq lzsl al'k \nzak tajlzvsq? Bmkl yg gnwj lg zae sfv oakz zae s zshhq tajlzvsq. Yggv dmuc.")
    rooms.append(r3b)

    r2c.description = "You quietly watch as two skeleton creatures are boxing. Might wanna give \nthem some space."
    r2c.addExit("north", r1)
    r2c.addExit("south", r3c)
    r2c.addItem("battling-skeletons", "They threaten to punch you if you don't leave the room immediately. That could've \ngotten pretty ugly!")
    rooms.append(r2c)

    r3c.description = "In the corner, there appears to be two knights throwing \nuppercuts at each other. Better walk on your tip-toes as to not be heard."
    r3c.addExit("north", r2c)
    r3c.addExit("south", r4c)
    r3c.addItem("battling-knights", "The knights spared your life as they were \ntoo busy trying to take each others. You were lucky.")
    rooms.append(r3c)

    r4c.description = "As you look around, you spot the king of the ring \nin mexico, Tortilla 'Chip' Jones."
    r4c.addExit("north", r3c)
    r4c.addItem("tortilla-chip-jones", "He's a good fighter, but tends to get distracted with \nthoughts of his favorite mexican resteraunts. Difficulty: 2/6")
    rooms.append(r4c)

    r2d.description = "You don't see anything, but you can smell something lovely."
    r2d.addExit("north", r3d)
    r2d.addExit("east", r1)
    rooms.append(r2d)

    #has a potion that grants +HP
    r3d.description = "There seems to be some sort of garden in here. Also in the corner you \nsee what appears to be...golden gloves!"
    r3d.addExit("north", r6d)
    r3d.addExit("east", r5d)
    r3d.addExit("south", r2d)
    r3d.addExit("west", r4d)
    r3d.addItem("garden", "There are roses, poppys, and sunflowers...somehow?")
    r3d.addGrabbable("golden-gloves")
    rooms.append(r3d)

    r4d.description = "You look around, and see a dead centaur with his boxing gloves \nstrangely still on his hands and hooves."
    r4d.addExit("north", r7d)
    r4d.addExit("east", r3d)
    r4d.addItem("dead-centaur", "How did this guy even lose?!?! He's \acentaur for crying out loud!")
    rooms.append(r4d)

    #room where player will later find the obsidian key for the obsidian door
    r5d.description = "In the center of the room lies a skeleton, probably belonging \nto a soldier who died in combat."
    r5d.addExit("west", r3d)
    r5d.addItem("dead-skeleton", "Man, this guy really went through some battle. Wonder who he was.")
    rooms.append(r5d)

    r6d.description = "You don't see anything in here. Although, you do \nsense some smell...ashy."
    r6d.addExit("north", r8d)
    r6d.addExit("west", r7d)
    rooms.append(r6d)

    r7d.description = "You spot a wooden chair in the middle of the room. Oddly enough, it's rocking"
    r7d.addExit("east", r6d)
    r7d.addExit("south", r4d)
    r7d.addItem("chair", "You sit on the chair and break it. Nice going.")
    rooms.append(r7d)

    #room where player can use the obsidian-key to escape and win
    r8d.description = "You look around and see...What the-"
    r8d.addExit("south", r6d)
    r8d.addItem("?", "It's a door! Seems to be made of obsidian. It's locked.")
    r8d.opened = False
    rooms.append(r8d)

    currentRoom = r1

    return rooms, currentRoom

inventory = []
rooms, currentRoom  = createRooms()

#beginning credits/initial directions and tips
print("Welcome To Punch Dungeon!")
print("Manuever your way around Punch Dungeon, boxing foes and finding clues to escape.")
print("Remember to 'look' at your opponents to scout them before picking a 'fight', to view")
print("their difficulty. Also, you cannot fight wounded/dead fighters, that's unfair.")
print("Good luck fighter, and if at any moment you are feeling wimpy, enter 'quit' to end")
print("your pathetic boxing career. Shameful. Anyways, go get 'em tiger!")
print("=" * 82)
print("You arise and notice you're wearing boxing gloves. You're ready for your journey!")

#function to unlock door and win game
def useKeyOnDoor():
    print("You insert the key into the obsidian door...")
    sleep(3)
    print("*Click!*")
    sleep(2)
    print("The door slowly creaks open...")
    sleep(3)
    print("Freedom! You've escaped punch dungeon, congratulations fighter!")
    sleep(3)

#function to drink potion and add HP
def equipGloves():
    global inventory 
    if "golden-gloves" in inventory:
        player.power += 25
        print("You equipped the golden gloves. Strength increased by 25!")
        sleep(3)
        print("Mmmm...tasty...")
        sleep(1)
        print("Darn it. Drank it all and now it's gone...oh well...")
        sleep(2)
        inventory.remove("golden-gloves")
    else:
        print("You don't have any golden gloves in your inventory.")
    
while (True):
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    if (currentRoom == None):
        death()
        break

    print("=" * 82)
    print(status)

    #shows user the potion can be grabbed and used later as it will be added to inventory if picked up using 'take'
    if "golden-gloves" in currentRoom.grabbables and noun not in inventory:
        print("You can equip these shiny beasts by taking them from the garden: 'golden-gloves'\n")

    #same thing as potion above ^
    if "obsidian-key" in currentRoom.grabbables and noun not in inventory:
        print("Hey! There's that obsidian-key that he told me to take!: 'obsidian-key'")

    action = input("What would you like to do? ")
    action = action.lower().strip()


    if (action in QUITCOMM):
        break
    
    response = "Be sure to use a valid action. Valid actions are fight, go, take, look, and use."
    words = action.split()

    if (len(words) == 2):
        verb = words[0].strip()
        noun = words[1].strip()

        if (verb in ACTIONS):

            if (verb == "go"):
                response = "You can't go this way."
                if (noun in currentRoom.exits):
                    i = currentRoom.exits.index(noun)
                    currentRoom = currentRoom.exitLocations[i]
                    response = "You walk {} and enter another room.".format(noun)

            #if user inputs use obsidian-key while it's in their inventory, it will unlock the door, winning game. break to officially end.
            elif (verb == "use"): 
                if "obsidian-key" in inventory and noun == "obsidian-key":
                    useKeyOnDoor()
                    break
                #removes the potion from being able to be picked up again after being consumed 1x time
                elif (noun == "golden-gloves"):
                    equipGloves()
                    currentRoom.removeItem("golden-gloves")
                else:
                    print("You don't have that item, Or are not able to use it right now.")

            elif (verb == "look"):
                if (noun in currentRoom.items):
                    i = currentRoom.items.index(noun)
                    response = currentRoom.itemDescriptions[i]
                else:
                    response = "You don't see that item."
            
            #code for what happens when an item like potion/obsidian-key is picked up by the user
            elif (verb == "take"):
                if (noun == "golden-gloves" and noun not in inventory):
                    i = currentRoom.grabbables.index(noun)
                    inventory.append(currentRoom.grabbables[i])
                    response = "You take the Golden Gloves. You can use these to boost your punching power."
                elif (noun == "obsidian-key" and noun not in inventory):
                    i = currentRoom.grabbables.index(noun)
                    inventory.append(currentRoom.grabbables[i])
                    response = "You take the obsidian key. Wonder where this might provide some use..."
                else:
                    response = "You don't see anything available to take, Or you already have that item."

            #when you wish the skeleton happy birthday (no noun=birthday because users may say happy bday or happy brithday for example)
            elif (verb == "happy"):
                print("Oh wow! You remembered...")
                sleep(3)
                print("I never had the guts for punch dungeon...")
                sleep(1)
                print("But...")
                sleep(3)
                print("It seems like you did...")
                sleep(3)
                print("I don't have the strength to get out...But you do!")
                sleep(2)
                print("Here, take this key...I found it a while ago but collapsed in here")
                print("on my way to use it...")
                sleep(3)
                #adds the obsidian-key that can now be picked up and used
                currentRoom.addGrabbable("obsidian-key")
                sleep(1)
                
            #code for fighting enemies: must be in the room and not yet defeated to be able to fight.
            elif (verb == "fight"):
                response = "Either you've already knocked that fighter out, or they're not in here!"
                if (noun in currentRoom.items):
                    if noun == "hank" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent1 = hank
                        response = boxingFight(player, opponent1)
                        currentRoom.fighter = opponent1
                        opponentName = "hank"
                    elif noun == "tortilla-chip-jones" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent2 = chip
                        response = boxingFight(player, opponent2)
                        currentRoom.fighter = opponent2
                        opponentName = "tortilla-chip-jones"
                    elif noun == "speedy-gonzalez" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent3 = speedy
                        response = boxingFight(player, opponent3)
                        currentRoom.fighter = opponent3
                        opponentName = "speedy-gonzalez"
                    elif noun == "doctor-punch-ya-face" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent4 = doctor
                        response = boxingFight(player, opponent4)
                        currentRoom.fighter = opponent4
                        opponentName = "doctor-punch-ya-face"
                    elif noun == "ko-kraig" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent5 = kokraig
                        response = boxingFight(player, opponent5)
                        currentRoom.fighter = opponent5
                        opponentName = "ko-kraig"
                    elif noun == "tike-myson" and currentRoom.fighter and not currentRoom.fighter.knockedOut:
                        opponent6 = tike
                        response = boxingFight(player, opponent6)
                        currentRoom.fighter = opponent6
                        opponentName = "tike-myson"
                    #easter egg: if you try to fight the skeletons or the knights on the south pathway, they will kill you and game ends.
                    elif noun == "battling-skeletons" or noun == "battling-knights":
                        print("They warned you...but you decided to fight them...")
                        sleep(3)
                        print("*BAM*")
                        sleep(1.5)
                        print("*BOOM*")
                        sleep(1.5)
                        print("*POW*")
                        sleep(2)
                        print("Now they're both towering over you...uh oh...")
                        sleep(3)
                        death()
                        break

                    #if you look at a fighter after you've defeated them, it will detail how/why they can no longer fight.
                    if opponentName and currentRoom.fighter.knockedOut:
                        defeated_description = f"{currentRoom.fighter.name} lies here, knocked out cold."
                        currentRoom.updateItemDescriptions(opponentName, defeated_description)

                    #drops the scribe message that is used to help decipher the hieroglyphics in room 3B (which the user must infer from 'julius caeser' and the song 'cipher' playing in one of the other rooms)
                    if all(f.knockedOut for f in [hank, chip, speedy, doctor, kokraig, tike]):
                        print("You've defeated all the fighters! Now find your way out of here!")
                        sleep(3)
                        print("Huh? What's this? A scribe has fallen from the ceiling!")
                        sleep (3)
                        print("It reads: Julius 'CAESAR' was named dictator perpetuo in the year -44.")
                        sleep(3)
                        print("Hmmmmm...what might this be used for...")
                        sleep(4)

    #if the player is knocked out, meaning they lost a fight, the games over.
    if (currentRoom != None):
        print("=" * 82)
        print(response)
    if player.knockedOut:
        break






























































