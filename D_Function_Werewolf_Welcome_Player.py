min_roles = [
    "- 🏹 Hunter",
    "- 🔮 Seer",
    "- 🛡️ Bodyguard",
    "- 👨‍🌾 Villager"]

##############################################################################
# CHECK PLAYER COUNT

def check_player_count(player_count) :
    if player_count < 5:
        print ("❌ Not enough players. Get minimum of 5 players to start the game")

        # Return False, inform the systems that condition is FALSE and NOT MET, and the FALSE output can be used because of the return statement
        return False


    elif player_count > 7:
        print ("❌ Too many players. The game can only support 5-7 players for now.")
        return False

    return True

##############################################################################
# TRY AGAIN

def try_again ():

    input_tryagain = str(input("Try again? Type [Y] for YES or [N] for NO: "))

    if input_tryagain.upper() == "Y":
        return True

    elif input_tryagain.upper() == "N":
        print ("Exiting the system ...")
        return False

    else:
        print ("Oops! That was not a valid character.")
        return try_again () 
    
##############################################################################
# WOLF COUNTER

def wolfcounter (playercount):
    if playercount == 5 or playercount == 6:
        wolfcount = 1
        return wolfcount
    
    elif playercount == 7:
        wolfcount = 2
        return wolfcount

##############################################################################
# ROLE IDENTIFICATION AND PRINTING


def role_identification(playercount, wolfcount):
    villagers = min_roles.copy()
    wolf = []

    additional_villagers = playercount - len(min_roles) - wolfcount

    #Add Villager
    for everyadditionalvillage in range (additional_villagers):
        villagers.append("- 👨‍🌾 Villager")

    #Add Werewolf
    for everyadditionalwerewolf in range (wolfcount):
        wolf.append("- 🐺 Werewolf") 

    return villagers, wolf

##############################################################################
# Game Setup
def gamesetup ():
    while True:
        try:
            input_playercount = int(input("Enter player count:"))

            
            
            if check_player_count (input_playercount):
                print ("Entering to the game ... ")

                print ("Counting the number of wolf ...")
                wolfcount = wolfcounter (input_playercount)

                print ("Identifying the roles ...  ")
                villagers, wolf = role_identification(input_playercount, wolfcount)

                print ("Entering the game with ...")
                print (f"Villager: {len(villagers)} | Werewolf {len(wolf)}\n")

                print ("Roles:")
                for item_no, role in enumerate(villagers + wolf, start = 1):
                #"enumerate" lets you loop through a list while keeping track of both the item and its number (index) at the same time
                    
                    print (f"{item_no}. {role}") 

                break

            if not try_again ():
                break

        except ValueError:
            print ("Oops! That was not a valid number.")
            
            if not try_again ():
                break



gamesetup ()