import random
answer = input("Hi do you want to play rock paper scissors? Y/N: ").strip().upper()
choices = ["Rock", "Paper", "Scissors"]
userScore = 0
computerScore = 0

if answer.startswith("Y"):
    print("Great lets get started!")
    while userScore < 3 and computerScore < 3:
        computerAction = random.choice(choices)
    
        userAction = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()
        print(f"I chose {computerAction}.")

        if userAction not in choices:
            print("Invalid choice, make sure to pick Rock, Paper, or Scissors")
            continue
    
        if userAction == computerAction:
            print("Its a draw! Lets try again")
        elif userAction == "Rock" and computerAction == "Paper" or userAction == "Paper" and computerAction == "Scissors" or userAction == "Scissors" and computerAction == "Rock":
            print("Oh you lost, better luck next time!")
            computerScore += 1
        else:
            print("You won!!")
            userScore += 1
    if userScore == 3:
        print("You won the game!")
    else:
        print("The computer won the game!")
        
               
else:
    print("Ok bye")


