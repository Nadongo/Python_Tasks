import random

ran = random.randint (1,9)
counter = 0
guess = 0

print ("Try and guess a number below 9 and enter Exit to stop")

while counter >= 0 and guess != 'exit':

    try:
        guess = input ("Enter your guess :")
        if guess == "exit":
            break

        counter += 1

        guess = int(guess)
        if ran == guess:
            print ("You guessed it right \n it took you :",counter,"Tries only!")
            break

        elif ran > guess:
            print ("Your guess is too low, try again!")

        else:
            print("Too high, Try again")

    except ValueError:
        print("Invalid input")


