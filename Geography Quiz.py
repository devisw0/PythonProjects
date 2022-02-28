print("Hello and welcome to this Geography quiz!")

begin = input("Begin game? Type yes to begin! ")

if begin.lower() != "yes":
    print("ok goodbye :(")
    quit()
else: 
    print("Very well, lets begin!")
score = 0

answer = input("What country's capital is La Paz? ")

if answer.lower() != "bolivia":
    print("wrong, sorry it was Bolivia!")
    score = 0
else:
    print("Correct!")
    score +=1

answer = input("What Continent contains the Sahara Desert? ")

if answer.lower() != "africa":
    print("wrong, sorry it was Africa!")

else:
    print("Correct!")
    score +=1


answer = input("What continent is the Danube river located in? ")

if answer.lower() != "europe":
    print("wrong, sorry it was Europe!")
else:
    print("Correct!")
    score +=1

answer = input("Bonus Question: (Extra point) What country borders Denmark, Poland and France? ")

if answer.lower() != "germany":
    print("wrong, sorry it was Germany, Netherlands/Holland or Luxembourg!")
    print("you got " + str(score) + "questions correct or " + str(score/4 *100) + "percent on the quiz!")
    quit()

else:
    score +=2
    print("Correct! Unfortunately this is the end. Goodbye!")
    print("you got " + str(score) + " questions correct or " + str(score/4 *100) + " percent on the quiz!")
    quit()