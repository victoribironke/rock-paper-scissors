import random

choices = ['scissors', 'paper', 'rock']

# Code words
paper = "paper"
scissors = "scissors"
rock = "rock"

# Time for the players to enter their names
player_one = input("Player One, enter your name: ")
print(f"This is a 'rock paper scissors' game between {player_one.upper()} and the computer.\nBEGIN!!!")

# Number of rounds to go and the score counter
rounds_to_go = 5
player_one_score = 0
computer_score = 0

# While loop and conditionals for the game
while rounds_to_go != 0:
    print(f"{rounds_to_go} rounds to go.")
    # Loop to check the value of player one's play. If it's invalid, the loop continues.
    while True:
        player_one_play = input(f"{player_one.upper()}, play: ")
        if player_one_play not in choices:
            print(f"Please choose from any of these: {choices}")
        else:
            break
    comp_play = random.choice(choices)
    print(f"COMPUTER, play: {comp_play}\n")

    rounds_to_go -= 1

    if player_one_play == paper and comp_play == rock:
        print(f"{player_one.upper()} wins this round. Paper covers rock.")
        player_one_score += 1
    elif player_one_play == rock and comp_play == paper:
        print(f"Computer wins this round. Paper covers rock.")
        computer_score += 1
    elif player_one_play == paper and comp_play == scissors:
        print(f"Computer wins this round. Scissors cuts paper.")
        computer_score += 1
    elif player_one_play == scissors and comp_play == paper:
        print(f"{player_one.upper()} wins this round. Scissors cuts paper.")
        player_one_score += 1
    elif player_one_play == rock and comp_play == scissors:
        print(f"{player_one.upper()} wins this round. Rock crushes scissors.")
        player_one_score += 1
    elif player_one_play == scissors and comp_play == rock:
        print(f"Computer wins this round. Rock crushes scissors.!")
        computer_score += 1
    elif player_one_play == comp_play:
        print(f"TIE!")

    # Display of the score if each player after every round
    print(f"{player_one.upper()}: {player_one_score} Computer: {computer_score}\n")
    

if player_one_score > computer_score:
    print(f"{player_one.upper()} wins the tournament.")
    print(f"Final Score:\n{player_one}: {player_one_score}\nComputer: {computer_score}")
elif player_one_score == computer_score:
    print("The tournament ends in a TIE")
    print(f"Final Score:\n{player_one}: {player_one_score}\nComputer: {computer_score}")
else:
    print(f"Computer wins the tournament.")
    print(f"Final Score:\n{player_one}: {player_one_score}\nComputer: {computer_score}")
