"""
Stuff to do:
- Let the players input their names (DONE)
- After every game, ask if they want to start a new game, if yes, continue, if no, break (DONE)
- After 5 games(tournament), tell the players how many times someone won and tell the final winner. (DONE)
"""

# Introduction to the game
print("                                           RULES OF THE GAME                                                 ")
print("You have five rounds. Whoever wins 3 out of the 5 rounds, wins the tournament.")
print("Code words: 'scissors', 'rock', and 'paper', in that form.")
print("After every game, the players must swap positions. The previous 'player one' becomes the current 'player two'.")

# Code words
paper = "paper"
scissors = "scissors"
rock = "rock"

# Check to see if they understood the rules
def understood():
    while True:
        answer = input("Understood? Yes or No: ")
        if answer == "yes" or answer == "Yes":
            print("Alright. Let's Begin.")
            break
        else:
            continue

understood()

# Time for the players to enter their names
player_one = input("Player One, enter your name: ")
player_two = input("Player Two, enter your name: ")
print(f"This is a 'rock paper scissors' game between {player_one.upper()} and {player_two.upper()}.\nBEGIN!!!")

# Number of rounds done and number of rounds to go
rounds = 0
rounds_to_go = 4
player_one_score = 0
player_two_score = 0

# While loop and conditionals for the game
while rounds <= 4:
    player_one_play = input(f"{player_one.upper()}, play: ")
    player_two_play = input(f"{player_two.upper()}, play: ")

    round = "rounds"
    if rounds_to_go <= 1:
        round.replace("rounds", "round")

    if player_one_play == paper and player_two_play == rock:
        print(f"{player_one} wins this round. Paper covers rock. {rounds_to_go} {round} to go!")
        player_one_score += 1
    elif player_one_play == rock and player_two_play == paper:
        print(f"{player_two} wins this round. Paper covers rock. {rounds_to_go} {round} to go!")
        player_two_score += 1
    elif player_one_play == paper and player_two_play == scissors:
        print(f"{player_two} wins this round. Scissors cuts paper. {rounds_to_go} {round} to go!")
        player_two_score += 1
    elif player_one_play == scissors and player_two_play == paper:
        print(f"{player_one} wins this round. Scissors cuts paper. {rounds_to_go} {round} to go!")
        player_one_score += 1
    elif player_one_play == rock and player_two_play == scissors:
        print(f"{player_one} wins this round. Rock crushes scissors. {rounds_to_go} {round} to go!")
        player_one_score += 1
    elif player_one_play == scissors and player_two_play == rock:
        print(f"{player_two} wins this round. Rock crushes scissors. {rounds_to_go} {round} to go!")
        player_two_score += 1
    elif player_one_play == player_two_play:
        print(f"TIE! {rounds_to_go} {round} to go!")

    # Display of the score if each player after every round
    print(f"{player_one}: {player_one_score} {player_two}: {player_two_score}")

    # Increment and reduction of the rounds
    rounds += 1
    rounds_to_go -= 1

    # Ask the players if they want the next round
    next_round = input("Next Game? ")
    if next_round == "yes":
        continue
    else:
        break


if player_one_score > player_two_score:
    print(f"{player_one} wins the tournament.")
    print(f"Final Score:\n{player_one}: {player_one_score}\n{player_two}: {player_two_score}")
elif player_one_score == player_two_score:
    print("The tournament ends in a TIE!")
    print(f"Final Score:\n{player_one}: {player_one_score}\n{player_two}: {player_two_score}")
else:
    print(f"{player_two} wins the tournament.")
    print(f"Final Score:\n{player_one}: {player_one_score}\n{player_two}: {player_two_score}")
