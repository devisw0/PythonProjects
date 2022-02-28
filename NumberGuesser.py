import random

top = input("type a number:")

if top.isdigit():
    top = int(top)

    if top <= 0:
        print('number is 0 or lower. It must be higher! ')
        quit()
else:
    print('Please type in a digit ')
    quit()
num_guesses = 0
num = random.randrange(0,top) #Number to guess
print(num)

while True: 
    num_guesses +=1
    guess = input("make a guess ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print('please type a number ')
        continue

    if guess == num:
        print("you got it, nice job! ")
        break
    
    elif guess > num:
        print("you were above the number")
    else:
        print("you were below the number")

print("you got it in ", num_guesses, "guesses")