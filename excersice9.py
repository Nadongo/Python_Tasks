#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, 
#then tell them whether they guessed too low, too high, or exactly right.

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken
#and when the game ends, print this out.

import random

def main():
    numb = random.randint (1,9)
    counter = 0
    guess = ""

    print("Enter a guess number of below 9 or Exit to end")

    while True:
        guess = input ("Enter your guess:")

        if guess.lower() == 'exit':
            break
        try:
            guess = int(guess)
            counter += 1
            
            if guess < 1 or guess > 9:
                print("Please enter a number between 1 and 9")
                continue
            
            if numb == guess:
                print(f'You guessed it right')
                break
        
            elif numb > guess:
                print("You guessed too low, Try again!")

            else:
                print("Your guess is too High,Try again!")

        except ValueError:
            print("Invalid input, Try Again!")

    print(f"Game over! You made {counter} {'guesses' if counter != 1 else 'guess'}.")

if __name__ == "__main__":
    main()