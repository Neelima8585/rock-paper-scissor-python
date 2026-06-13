import random

def get_choice():
    player_choice=input("enter your choice (rock,paper,scissor):")
    if player_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice! Defaulting to rock.")
        player_choice = "rock"
    computer_choice =random.choice(["paper","rock","scissor"])
    choice={"player":player_choice,"computer":computer_choice}
    return choice

def check_win(player,computer):
    print( f"you choose {player} ,computer choose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissor. you win!"
        else:
            return "paper covers rock. you lose!"

    elif player == "paper":
        if computer == "scissor":
            return "scissor cuts paper. you lose!"
        else:
            return "paper covers rock. you win!"

    elif player == "scissor":
        if computer == "rock":
            return "rock smashes scissor. you lose!"
        else:
            return "scissor cuts paper. you win!"                                

while True:
    choices=get_choice()
    result = check_win(choices["player"],choices["computer"])
    print(result)    
    play_again = input("\nPlay again? (y/n): ").lower().strip()
    if play_again != 'y':
        print("Thanks for playing!")
        break
