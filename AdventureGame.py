from tkinter.messagebox import YES
from token import SOFT_KEYWORD
import random

Looter_health = 100
user = input("Input your username ")
print("Welcome ", user, "to this RPG game")

begin = input("would you like to begin? ").lower()


if begin =="yes":

    answer = input("When you first leave your childhood town where you come across a fork in the road. Which side will you choose? (left or right) ").lower()
    if answer == "left":
        print("Unfortunately the left path takes you to a dead end, and there is a den of wolves in front of you. The wolves deplete you of your health. Game Over ")
        quit()
    elif answer == "right":
        print("You come accross a sword and pick it up. Good to have a weapon for the future!")
        print("There is an armed man yelling at you from a couple feet away. He is trying to rob you of you posessions. You decide to... (fight or give posessions")
        
        choice = input("will you surrender or fight? ").lower()
        if choice == "surrender":
            print("While you are handing over your possessions he notices you have a sword. Alarmed he attacks and you lose your life. Game Over. ")
            quit()
        elif choice == "fight":
            print("you chose fight! ")

            while Looter_health > 0:
                num = random.randrange(0,100)
                if Looter_health <= 0:
                    print(" Congratulations, you defeated the looter! ")
                    exp = random.randrange(7,15)
                    print("You gained ", exp, " experience points!")
                    levtwo = 100

                    if exp <= 100:
                        untill2 = 100-exp
                    quit()
                    
            attack = input(" would you like to swing or thrust? ").lower()

            if attack == "thrust": #this inside while loop
                print(" oops since this sword is not meant for thrusting, it did barely any damage. You are easily overwhelmed and ended. Game Over.") #this inside while loop
                quit() #this inside while loop
            elif attack == "swing": #this inside while loop
                damage = num #this inside while loop
                Looter_health = Looter_health - damage #this inside while loop
                print("Looter has ", Looter_health, " hp left!") #this inside while loop
            


else:
    print("ok, goodbye! ")
    quit()

#Will come back to this at a later date and make an actual story, much more locations (map), inventory system 
#and capability to fight multiple enemies, experience system, abilities etc.
