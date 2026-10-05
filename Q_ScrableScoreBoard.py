#Parent Class
class Player ():
    def __init__(self, name):
        self.name = name

#Child Class
class ScrablePlayers (Player):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

######################################
# 1. Ask the number of players
def playerCount ():
    print ()
    print ("--- Scrabble Point Counter ---")
    print ("Enter the number of players: ")
    print ("Note: Min of 2 ; Max of 4 players")
    print ("You can also team up")
    input_playerCount = int(input("Your Answer: "))

    if input_playerCount >1 and input_playerCount <5:
        print ()
        return input_playerCount

    else:
        print (f"Sorry you cannot play with {input_playerCount}.")
        return False
    
player_count = playerCount ()
######################################
# 2. Ask the names of the players, create child player, and append

playerList = []
score = 0

def askNames (player_count):
    print ("Collecting Player Names...")
    for i in range (player_count):

        #Ask the name
        name = str(input(f"Enter player {i + 1}'s name: "))

        #Create the class? or child class?
        player_name = ScrablePlayers (name.title(), score)

        #Append the player
        playerList.append (player_name)

askNames (player_count)
print()
##########################################
# 3. Printing names for verification

def player_names (playerList):
    print ("Entering the game with these player ...")
    for everyPlayer in playerList:
        print (f"Player {everyPlayer.name} | Score: {everyPlayer.score}")

player_names (playerList)
print()
print ("Entering the game ...")
print()
##########################################
# End Turn
def endGame ():
    input_tryAgain = input("End Game? Type [Y] for Yes or [N] for No: ")

    if input_tryAgain.upper() == "Y":
        return True

    elif input_tryAgain.upper() == "N":
        return False

    else:
        print ("Oops! That's an invalid input")
        return False

print ()
##########################################
# 4. Entering the games and scoring

def scoring ():
    while True:

        for i, everyPlayer in enumerate(playerList):
            #Current Player's Turn
            print (f"Current Player: Player-{i + 1} {everyPlayer.name}")

            # Ask the word score
            word_points = int(input(f"Enter the score: "))

            # Adding the word score
            everyPlayer.score = everyPlayer.score + word_points

            # Printing the updated score:
            for everyPlayer in playerList:
                print (f"Player {everyPlayer.name} | Score: {everyPlayer.score}")
                print ()

            # Ask if game should end
            if endGame ():
                print ("Tallying Score ...")
                print ("Game Over!")
                break

        else:
            # Runs if the FOR loops fnishes normally
            print ()
            continue

        # Breaks the while loop
        break

scoring ()

################################################
# Score Comparison
def winner ():
    for everyPlayer in playerList:
        print (f"Player {everyPlayer.name} | Score: {everyPlayer.score}")

    print ("The winner is ...")

    highest_score = 0
    winner_player = None

    # Compare Score
    for everyPlayer in playerList:
        if everyPlayer.score > highest_score:
            highest_score = everyPlayer.score
            winner_player = everyPlayer
    
    # Announce Winner
    print (f"------- Winner {winner_player.name} | {winner_player.score} points -------")



winner ()
          







# def tryAgain ():
#     input_tryAgain = input("Enter player count again? Type ")

#     if input_tryAgain.upper() == "Y":
#         print ("Returning back to the menu ...")
#         return True

#     elif input_tryAgain.upper() == "N":
#         print("Exiting the system ...")
#         return False

#     else:
#         print ("Oops! That's an invalid input")
#         return False