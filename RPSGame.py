import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("type rock/paper/scissors or q to quit ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        print("please type a correct input")
        continue
    rand_nums = random.randint(0,2) #where rock = 0, paper = 1, scissors = 2
    computer_pick = options[rand_nums]
    print("Computer picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == "scissors":
        print("you won!")
        user_wins+=1
    elif user_input == 'paper' and computer_pick == "rock":
        print("you won!")
        user_wins+=1
    elif user_input == 'paper' and computer_pick == "rock":
        print("you won!")
        user_wins+=1
    else:
        print("You Lost!")
        computer_wins +=1

print("you won", user_wins, " times")
print("I won ", computer_wins, " times")
print("Game Over")   
