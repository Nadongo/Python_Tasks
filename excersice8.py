#Make a two-player Rock-Paper-Scissors game. 
#(Hint: Ask for player plays (using input), compare them,
#print out a message of congratulations to the winner
#and ask if the players want to start a new game)

import sys

user1 = input("What is your name: ")
user2 = input(" Player 2 tell us your name: ")
print("Welcome to Rock, Paper, Scissors Game!")

user1_ans = input("%s, Choose one: rock, paper, scissors :" % user1)
user2_ans = input("%s, Choose one: rock, papers, scissors :" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a Tie!!!")
    
    elif u1 == "rock": 
        if u2 == "scissors":
            return("Rock wins!")
        else:
            return("Paper wins!")
    
    elif u1 == "scissors":
        if u2 == "paper":
            return("Scissors wins!")
        else:
            return("Rock wins!")
    elif u1 == "paper":
        if u2 == "rock":
            return("Paper wins!")
        else:
            return("Scissors wins!")
        
    else:
        return("Invalid input! Try again correctly.")
        sys.exit()


print(compare (user1_ans, user2_ans))