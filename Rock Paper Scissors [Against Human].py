# Code words
paper = "paper"
scissors = "scissors"
rock = "rock"
choices = [rock, paper, scissors]

# Time for the players to enter their names
player_one = input("Player One, enter your name: ")
player_two = input("Player Two, enter your name: ")
print(f"This is a 'rock paper scissors' game between {player_one.upper()} and {player_two.upper()}.\nBEGIN!!!")

# Number of rounds to go and the score counter
rounds_to_go = 5
player_one_score = 0
player_two_score = 0

# While loop and conditionals for the game
while rounds_to_go != 0:
    print(f"{rounds_to_go} rounds to go.")
    
    # Loop to check the value of player one's play. If it's invalid, the loop continues.
    while True:
        player_one_play = input(f"{player_one.upper()}, play: ")
        if player_one_play not in choices:
            print(f"{player_one.upper()}, please choose from any of these: {choices}")
        else:
            break
    
    # Loop to check the value of player two's play. If it's invalid, the loop continues.
    while True:
        player_two_play = input(f"{player_two.upper()}, play: ")
        if player_two_play not in choices:
            print(f"{player_two.upper()}, please choose from any of these: {choices}")
        else:
            break

    rounds_to_go -= 1

    if player_one_play == paper and player_two_play == rock:
        print(f"{player_one.upper()} wins this round. Paper covers rock.")
        player_one_score += 1
    elif player_one_play == rock and player_two_play == paper:
        print(f"{player_two.upper()} wins this round. Paper covers rock.")
        player_two_score += 1
    elif player_one_play == paper and player_two_play == scissors:
        print(f"{player_two.upper()} wins this round. Scissors cuts paper.")
        player_two_score += 1
    elif player_one_play == scissors and player_two_play == paper:
        print(f"{player_one.upper()} wins this round. Scissors cuts paper.")
        player_one_score += 1
    elif player_one_play == rock and player_two_play == scissors:
        print(f"{player_one.upper()} wins this round. Rock crushes scissors.")
        player_one_score += 1
    elif player_one_play == scissors and player_two_play == rock:
        print(f"{player_two.upper()} wins this round. Rock crushes scissors.")
        player_two_score += 1
    elif player_one_play == player_two_play:
        print(f"TIE!")

    # Display of the score if each player after every round
    print(f"{player_one.upper()}: {player_one_score} {player_two.upper()}: {player_two_score}")


if player_one_score > player_two_score:
    print(f"{player_one.upper()} wins the tournament.")
    print(f"Final Score:\n{player_one.upper()}: {player_one_score}\n{player_two.upper()}: {player_two_score}")
elif player_one_score == player_two_score:
    print("The tournament ends in a TIE!")
    print(f"Final Score:\n{player_one.upper()}: {player_one_score}\n{player_two.upper()}: {player_two_score}")
else:
    print(f"{player_two.upper()} wins the tournament.")
    print(f"Final Score:\n{player_one.upper()}: {player_one_score}\n{player_two.upper()}: {player_two_score}")
