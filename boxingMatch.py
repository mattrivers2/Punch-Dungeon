#Boxing Match
#Code Written by Matthew Rivers, CSC 101

#imports all neccesary source files
import random
from Death import death
from time import sleep

fightNumber = 1

def boxingFight(user_boxer, computer_boxer):

    global fightNumber
    user_boxer.health = 150 + (fightNumber - 1) * 50
    #starts the fight with some organized formatting of = characters
    print("=" * 60)
    print(f"Ding Ding Ding! Ladies and Gentleman: {user_boxer.name} vs. {computer_boxer.name}!")
    

    #fight goes on while both fighters have health
    while user_boxer.health > 0 and computer_boxer.health > 0:

        #displays each fighters current HP during the fight
        print(f"\n{user_boxer.name} Health: {user_boxer.health} | {computer_boxer.name} Health: {computer_boxer.health}")
        print("=" * 60)

        #asks user if they want to either punch or defend
        user_move = input("Choose your move (punch or defend): ").lower()
        while user_move not in ["punch", "defend"]:
            user_move = input("Invalid choice. Choose 'punch' or 'defend': ").lower()

        #computer fighter selects to punch or defend randomly every turn
        computer_move = random.choice(["punch", "defend"])
        print(f"{computer_boxer.name} chooses to {computer_move}!")

        #if both punch, both deal damage according to their power
        if user_move == "punch" and computer_move == "punch":
            user_boxer.takeDamage(computer_boxer.power)
            computer_boxer.takeDamage(user_boxer.power)
            print("Both fighters exchanged punches!")
        #if one punches and one defends, the one who defends has their damage reduced by whatever their defense buffer is
        elif user_move == "punch" and computer_move == "defend":
            reduced_damage = max(0, user_boxer.power - computer_boxer.defense)
            computer_boxer.takeDamage(reduced_damage)
            print(f"{user_boxer.name}'s punch is reduced by {computer_boxer.name}'s defense!")
        elif user_move == "defend" and computer_move == "punch":
            reduced_damage = max(0, computer_boxer.power - user_boxer.defense)
            user_boxer.takeDamage(reduced_damage)
            print(f"{computer_boxer.name}'s punch is reduced by {user_boxer.name}'s defense!")
        #only other combination is if both fighters decide to defend, resulting in no damage dealt or taken
        else:
            print("Both fighters defended. No damage this round.")

        #if computer HP falls below 0, user wins and they lose
        if computer_boxer.health <= 0 and user_boxer.health > 0:
            fightNumber += 1
            computer_boxer.defeat()
            print(f"{computer_boxer.name} has been defeated!")
            print(f"\n{user_boxer.name} wins the fight by KO!")
            #user is granted +50 health, +25 strength, and +10 defense buffer every win they achieve
            user_boxer.power += 25
            user_boxer.defense += 10
            #details the above-mentioned new attributes for the user
            if fightNumber == 2:
                print("Player 1's health increased by 50! New HP: 200")
            elif fightNumber == 3:
                print("Player 1's health increased by 50! New HP: 250")
            elif fightNumber == 4:
                print("Players 1's health increased by 50! New HP: 300")
            elif fightNumber == 5:
                print("Player 1's health increased by 50! New HP: 350")
            elif fightNumber == 6:
                print("Player 1's health increased by 50! New HP: 400")
            elif fightNumber == 7:
                print("Player 1's health increased by 50! New HP: 450")
            print(f"{user_boxer.name}'s defense increased by 10! New Defense Buffer: {user_boxer.defense}")
            print(f"{user_boxer.name}'s power increased by 25! Now your punches will deal {user_boxer.power} damage. Keep on striking!")
            sleep(6)
            break

        #if user loses the fight, they die and game is over
        elif user_boxer.health <=0 and computer_boxer.health > 0:
            print(f"\n{computer_boxer.name} wins the fight by KO!")
            user_boxer.defeat()
            sleep(4)
            #user dies, ending game
            death()
            break

    

    
        