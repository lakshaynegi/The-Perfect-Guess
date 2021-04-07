import random
randNumber = random.randint(1,100)
# print (randNumber)
userGuess = None 
guesses= 0
while(userGuess != randNumber):
    userGuess = int(input ("Enter your guess: "))
    guesses +=1
    if (userGuess==randNumber):
        print ("You Guessed it Right!")
    else:
        if (userGuess>randNumber):
            print ("You Guessed it Wrong! Enter a smaller number")
        else:
            print ("you guessed it Wrong! Enter a larger number")
    



print (f"You guessed the number in {guesses} guesses")
